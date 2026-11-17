# Credits and attribution

## The original method — the Gauntlet Loop

The core idea behind this repository — **split a goal into small parts, give each part a specialist builder and a blind critic with a clean context, set a bar the agent cannot argue its way around, and never let the builder grade itself** — comes from:

- **Matt Shumer — "How to Run a Gauntlet Loop: The Prompting Method Behind Claude of Duty"**
  Something Big Is Happening — https://somethingbig.ai/gauntlet-loop
- The author's open-source companion repository: **`mshumer/Claude-of-Duty`** — https://github.com/mshumer/Claude-of-Duty
- Original discussion on X: [@mattshumer_](https://x.com/mattshumer_)

The original article illustrates the method mainly through **building software and games**.

> **Scope and copyright note:** this repository is an **independent adaptation and extension** of the Gauntlet Loop into a multi-domain skill set (coding, writing, design, data analysis, research, prompt evaluation, detection engineering, and authorized security testing). It is **not an official product** of Matt Shumer and is not endorsed by him. The method is **restated and applied with attribution**; no substantial verbatim text is copied from the original article. To learn the method in its original form, read the article directly.

## Security and detection reference frameworks

Used by `security-vuln-gauntlet` and the detection domain file:

- **OWASP Top 10 (2021)** — https://owasp.org/Top10/
- **OWASP Application Security Verification Standard (ASVS)** — https://owasp.org/www-project-application-security-verification-standard/
- **OWASP API Security Top 10 (2023)** — https://owasp.org/API-Security/
- **OWASP Web Security Testing Guide (WSTG)** — https://owasp.org/www-project-web-security-testing-guide/
- **MITRE ATT&CK** — https://attack.mitre.org
- **MITRE CWE** and the **CWE Top 25 Most Dangerous Software Weaknesses** — https://cwe.mitre.org/top25/
- **MITRE CVE** — https://www.cve.org
- **CIS Benchmarks** — https://www.cisecurity.org/cis-benchmarks
- **CVSS (FIRST)** — https://www.first.org/cvss/
- **Atomic Red Team** — https://atomicredteam.io

## Detection tooling and formats

- **Sigma** (portable SIEM detection rule format) — https://github.com/SigmaHQ/sigma
- **Splunk Search Processing Language (SPL)** — https://docs.splunk.com
- **Microsoft Sentinel / Defender — Kusto Query Language (KQL)** — https://learn.microsoft.com/azure/data-explorer/kusto/query/
- **CrowdStrike Falcon** — https://www.crowdstrike.com
- **Elastic Security / ES|QL / EQL** — https://www.elastic.co/security

## License

Released under the **MIT License** (see [LICENSE](LICENSE)). Trademarks, frameworks, and products named above belong to their respective owners and are referenced here for technical purposes only.
