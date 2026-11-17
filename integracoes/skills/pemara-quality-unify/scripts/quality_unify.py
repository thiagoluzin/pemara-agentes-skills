#!/usr/bin/env python3
"""Auditoria determinística de qualidade, integridade e Unicode do ecossistema Pemara."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import tempfile
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence


SCHEMA_VERSION = 1
TOOL_VERSION = "1.0.1"
IGNORED_DIRS = {
    ".git",
    ".turbo",
    ".venv",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "site-packages",
    "venv",
}
TEXT_EXTENSIONS = {
    ".bat",
    ".cjs",
    ".cmd",
    ".css",
    ".csv",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".jsonl",
    ".md",
    ".mjs",
    ".ps1",
    ".py",
    ".sh",
    ".sql",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
SECRET_NAMES = {
    ".env",
    "auth.json",
    "credentials.json",
    "id_rsa",
    "id_ed25519",
    "secrets.json",
}
SECRET_SUFFIXES = {".key", ".p12", ".pfx", ".pem"}
MOJIBAKE_PATTERNS = (
    re.compile(r"\u00C3[\x80-\xBF\u00A3-\u00BF]"),
    re.compile(r"\u00C2[\x80-\xBF]"),
    re.compile(r"\u00E2(?:\u20AC|\u201E|\u2122|\u0153|\u017E|\u2020|\u2021|\u02C6|\u2030|\u0160|\u2039|\u0152|\u017D|\u0161|\u203A|\u0178)"),
    re.compile(r"(?:\u00F0\u0178|\u00EF\u00B8|\u00EF\u00BB\u00BF)"),
    re.compile("\N{REPLACEMENT CHARACTER}"),
)
PRIVATE_KEY_PATTERN = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
FRONTMATTER_PATTERN = re.compile(r"\A---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|\Z)", re.DOTALL)
FRONTMATTER_FIELD = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$")


def configure_utf8_console() -> None:
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name)
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    message: str
    fixable: bool = False


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def is_link(path: Path) -> bool:
    try:
        info = path.lstat()
    except FileNotFoundError:
        return False
    return stat.S_ISLNK(info.st_mode) or bool(
        getattr(info, "st_file_attributes", 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT
    )


def plain_path(path: Path, within: Path | None = None) -> Path:
    # Check ancestors before normalizing away any ".." component.
    raw = path.expanduser().absolute()
    for part in (*reversed(raw.parents), raw):
        if is_link(part):
            raise ValueError(f"link ou ponto de reanálise fora de escopo: {part}")
    result = Path(os.path.abspath(raw))
    if within is not None:
        result.resolve().relative_to(within)
    return result


def iter_files(root: Path) -> Iterable[Path]:
    root = plain_path(root).resolve(strict=True)
    for current, dirs, files in os.walk(root, followlinks=False):
        current_path = plain_path(Path(current), root)
        dirs[:] = sorted(d for d in dirs if d not in IGNORED_DIRS and not is_link(current_path / d))
        for name in sorted(files):
            path = current_path / name
            if not is_link(path) and stat.S_ISREG(path.lstat().st_mode):
                yield path


def replace_bytes(path: Path, data: bytes, within: Path, original: bytes | None = None) -> None:
    # Atomic replacement also avoids in-place writes through a shared hard link.
    path = plain_path(path, within)
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else None
    temp = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".pqu-", delete=False) as stream:
            temp = Path(stream.name)
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        plain_path(temp, within)
        if mode is not None:
            temp.chmod(mode)
        plain_path(path, within)
        if original is not None and path.read_bytes() != original:
            raise ValueError(f"arquivo alterado durante o reparo: {path}")
        plain_path(path.parent, within)
        os.replace(temp, path)
    finally:
        if temp is not None:
            plain_path(temp.parent, within)
            temp.unlink(missing_ok=True)


def is_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTENSIONS or path.name in {
        "AGENTS.md",
        "FIXLOG.md",
        "LICENSE",
        "RULES.md",
        "SKILL.md",
    }


def mojibake_score(text: str) -> int:
    return sum(len(pattern.findall(text)) for pattern in MOJIBAKE_PATTERNS)


def decode_utf8(path: Path) -> tuple[str | None, str | None, bool]:
    data = path.read_bytes()
    has_bom = data.startswith(b"\xef\xbb\xbf")
    try:
        return data.decode("utf-8-sig"), None, has_bom
    except UnicodeDecodeError as error:
        return None, str(error), has_bom


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = FRONTMATTER_PATTERN.search(text)
    if not match:
        return None
    fields: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        if not raw_line.strip() or raw_line.startswith((" ", "\t", "#")):
            continue
        field = FRONTMATTER_FIELD.match(raw_line)
        if field:
            fields[field.group(1)] = field.group(2).strip().strip('"\'')
    return fields


def validate_skill(path: Path, text: str, root: Path, names: dict[str, Path]) -> list[Finding]:
    findings: list[Finding] = []
    rel = relative(path, root)
    frontmatter = parse_frontmatter(text)
    if frontmatter is None:
        return [Finding("error", "skill.frontmatter", rel, "SKILL.md sem frontmatter YAML válido.")]
    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        findings.append(Finding("error", "skill.frontmatter", rel, "Campo name ausente ou fora de kebab-case."))
    if not description or description.startswith("[TODO"):
        findings.append(Finding("error", "skill.frontmatter", rel, "Campo description ausente ou incompleto."))
    if name:
        previous = names.get(name)
        if previous is not None and previous != path:
            findings.append(
                Finding(
                    "error",
                    "skill.duplicate_name",
                    rel,
                    f"Nome de skill duplicado; primeira ocorrência em {relative(previous, root)}.",
                )
            )
        else:
            names[name] = path
    line_count = len(text.splitlines())
    signature = path.parent / "skill.oms.sig"
    signed_vendor_skill = not is_link(signature) and signature.is_file()
    if line_count > 500 and not signed_vendor_skill:
        findings.append(Finding("warning", "skill.oversized", rel, f"SKILL.md possui {line_count} linhas; preferir referências."))
    return findings


def validate_plugin_manifest(path: Path, text: str, root: Path) -> list[Finding]:
    rel = relative(path, root)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        return [Finding("error", "plugin.manifest", rel, f"JSON inválido: {error}")]
    findings: list[Finding] = []
    for field in ("name", "version", "description", "author", "interface"):
        if not data.get(field):
            findings.append(Finding("error", "plugin.manifest", rel, f"Campo obrigatório ausente: {field}."))
    if data.get("name") and path.parent.parent.name != data["name"] and data["name"] not in path.parts:
        findings.append(Finding("error", "plugin.manifest", rel, "Nome do plugin difere do diretório raiz."))
    return findings


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_package_manifest(manifest_path: Path, root: Path) -> list[Finding]:
    rel = relative(manifest_path, root)
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        return [Finding("error", "manifest.invalid", rel, f"Manifesto inválido: {error}")]
    findings: list[Finding] = []
    packages = manifest.get("packages")
    if not isinstance(packages, list):
        return [Finding("error", "manifest.invalid", rel, "Campo packages deve ser uma lista.")]
    for index, package in enumerate(packages):
        if not isinstance(package, dict):
            findings.append(Finding("error", "manifest.invalid", rel, f"Pacote {index} não é um objeto."))
            continue
        declared = package.get("path")
        category = package.get("category")
        expected = package.get("sha256")
        if not declared or not category:
            findings.append(Finding("error", "manifest.invalid", rel, f"Pacote {index} sem path ou category."))
            continue
        if not isinstance(declared, str):
            findings.append(Finding("error", "manifest.path", rel, "Caminho do pacote deve ser texto."))
            continue
        try:
            target = plain_path(root / declared, root.resolve())
        except ValueError:
            findings.append(Finding("error", "manifest.path", declared, "Caminho escapa da raiz do bundle."))
            continue
        if not target.is_file():
            findings.append(Finding("error", "manifest.path", declared, "Arquivo declarado não existe."))
        elif expected and sha256(target).lower() != str(expected).lower():
            findings.append(Finding("error", "manifest.checksum", declared, "SHA-256 diverge do manifesto."))
    return findings


def scan(root: Path, manifest: Path | None) -> tuple[dict[str, int], list[Finding]]:
    findings: list[Finding] = []
    counts = {"files": 0, "text_files": 0, "skills": 0, "plugins": 0}
    root = plain_path(root).resolve(strict=True)
    skill_names: dict[str, Path] = {}
    for path in iter_files(root):
        counts["files"] += 1
        rel = relative(path, root)
        lowered = path.name.lower()
        if lowered in SECRET_NAMES or path.suffix.lower() in SECRET_SUFFIXES:
            findings.append(Finding("error", "security.secret_file", rel, "Arquivo potencialmente secreto incluído."))
        if not is_text_file(path):
            continue
        counts["text_files"] += 1
        text, decode_error, has_bom = decode_utf8(plain_path(path, root))
        if decode_error:
            findings.append(Finding("error", "unicode.invalid_utf8", rel, decode_error, True))
            continue
        assert text is not None
        score = mojibake_score(text)
        if score:
            findings.append(Finding("error", "unicode.mojibake", rel, f"{score} sequência(s) suspeita(s) de mojibake.", True))
        if "\x00" in text:
            findings.append(Finding("error", "unicode.nul", rel, "Arquivo textual contém byte NUL."))
        if path.suffix.lower() == ".ps1" and not has_bom and any(ord(char) > 127 for char in text):
            findings.append(Finding("warning", "unicode.powershell_bom", rel, "PowerShell com não ASCII e sem BOM; Windows PowerShell 5.1 pode interpretar como ANSI."))
        if PRIVATE_KEY_PATTERN.search(text):
            findings.append(Finding("error", "security.private_key", rel, "Conteúdo de chave privada detectado."))
        if len(text) > 2_000_000:
            findings.append(Finding("warning", "text.oversized", rel, f"Arquivo textual possui {len(text)} caracteres."))
        if path.name == "SKILL.md":
            counts["skills"] += 1
            findings.extend(validate_skill(path, text, root, skill_names))
        if path.name == "plugin.json" and path.parent.name == ".codex-plugin":
            counts["plugins"] += 1
            findings.extend(validate_plugin_manifest(path, text, root))
    if manifest:
        findings.extend(validate_package_manifest(plain_path(manifest), root))
    return counts, findings


def repair_text(text: str) -> str | None:
    original_score = mojibake_score(text)
    if original_score == 0:
        return None
    candidates: list[str] = []
    for encoding in ("cp1252", "latin-1"):
        try:
            candidates.append(text.encode(encoding).decode("utf-8"))
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass
    improved = [candidate for candidate in candidates if "\ufffd" not in candidate and mojibake_score(candidate) < original_score]
    if not improved:
        return None
    return min(improved, key=mojibake_score)


def repair_unicode(root: Path, apply: bool, backup_root: Path | None) -> tuple[list[Path], list[Finding]]:
    root = plain_path(root).resolve(strict=True)
    changed: list[Path] = []
    findings: list[Finding] = []
    if apply:
        if backup_root is None:
            raise ValueError("--backup-root é obrigatório com --apply")
        backup_root = plain_path(backup_root).resolve()
        if backup_root.is_relative_to(root) or root.is_relative_to(backup_root):
            raise ValueError("--backup-root e --root devem ser árvores separadas")
    for path in iter_files(root):
        if not is_text_file(path):
            continue
        text, decode_error, has_bom = decode_utf8(plain_path(path, root))
        rel = relative(path, root)
        if decode_error:
            findings.append(Finding("error", "unicode.invalid_utf8", rel, decode_error))
            continue
        assert text is not None
        repaired = repair_text(text)
        if repaired is None:
            continue
        if apply:
            assert backup_root is not None
            encoding = "utf-8-sig" if has_bom else "utf-8"
            original = text.encode(encoding)
            backup = plain_path(backup_root / rel, backup_root)
            backup.parent.mkdir(parents=True, exist_ok=True)
            plain_path(backup, backup_root)
            try:
                with backup.open("xb") as stream:
                    stream.write(original)
                    stream.flush()
                    os.fsync(stream.fileno())
            except FileExistsError:
                findings.append(Finding("error", "repair.backup_exists", rel, "Backup já existe; use uma nova pasta de backup."))
                continue
            replace_bytes(path, repaired.encode(encoding), root, original)
        changed.append(path)
    return changed, findings


def build_report(root: Path, counts: dict[str, int], findings: Sequence[Finding], fail_on_warning: bool) -> dict[str, object]:
    errors = sum(item.severity == "error" for item in findings)
    warnings = sum(item.severity == "warning" for item in findings)
    passed = errors == 0 and (warnings == 0 or not fail_on_warning)
    return {
        "schema_version": SCHEMA_VERSION,
        "tool": "pemara-quality-unify",
        "tool_version": TOOL_VERSION,
        "generated_at": utc_now(),
        "root": str(root),
        "verdict": "PASS" if passed else "FAIL",
        "counts": {**counts, "errors": errors, "warnings": warnings},
        "findings": [asdict(item) for item in findings],
    }


def write_report(report: dict[str, object], destination: Path | None) -> None:
    payload = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if destination:
        destination = plain_path(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)
        replace_bytes(destination, payload.encode("utf-8"), plain_path(destination.parent).resolve())
    print(payload, end="")


def resolve_root(value: str) -> Path:
    root = plain_path(Path(value)).resolve()
    if not root.is_dir():
        raise argparse.ArgumentTypeError(f"raiz inexistente: {root}")
    return root


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Audita qualidade, skills, manifests e Unicode.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    scan_parser = subparsers.add_parser("scan", help="Varre sem alterar arquivos.")
    scan_parser.add_argument("--root", required=True, type=resolve_root)
    scan_parser.add_argument("--manifest", type=Path)
    scan_parser.add_argument("--report", type=Path)
    scan_parser.add_argument("--fail-on-warning", action="store_true")
    repair_parser = subparsers.add_parser("repair-unicode", help="Simula ou aplica reparações seguras de mojibake.")
    repair_parser.add_argument("--root", required=True, type=resolve_root)
    repair_parser.add_argument("--apply", action="store_true")
    repair_parser.add_argument("--backup-root", type=Path)
    repair_parser.add_argument("--report", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    configure_utf8_console()
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "scan":
            manifest = plain_path(args.manifest) if args.manifest else None
            if manifest and not manifest.is_file():
                parser.error(f"manifesto inexistente: {manifest}")
            counts, findings = scan(args.root, manifest)
            report = build_report(args.root, counts, findings, args.fail_on_warning)
            write_report(report, args.report)
            if report["counts"]["errors"]:
                return 1
            if args.fail_on_warning and report["counts"]["warnings"]:
                return 2
            return 0
        changed, findings = repair_unicode(args.root, args.apply, args.backup_root)
        report = {
            "schema_version": SCHEMA_VERSION,
            "tool": "pemara-quality-unify",
            "tool_version": TOOL_VERSION,
            "generated_at": utc_now(),
            "root": str(args.root),
            "mode": "apply" if args.apply else "dry-run",
            "changed": [relative(path, args.root) for path in changed],
            "errors": [asdict(item) for item in findings],
        }
        write_report(report, args.report)
        return 1 if findings else 0
    except (OSError, ValueError) as error:
        print(f"ERRO: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
