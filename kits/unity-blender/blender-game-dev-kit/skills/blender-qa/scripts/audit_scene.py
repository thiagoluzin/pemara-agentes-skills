"""Read-only evaluated mesh inventory. Run in Blender; never saves the scene."""
import argparse
import json
import sys
from pathlib import Path
import bpy


def audit_scene():
    graph = bpy.context.evaluated_depsgraph_get()
    rows = []
    for obj in sorted(bpy.context.scene.objects, key=lambda o: o.name):
        if obj.type != 'MESH':
            continue
        evaluated = obj.evaluated_get(graph)
        mesh = evaluated.to_mesh()
        try:
            mesh.calc_loop_triangles()
            warnings = []
            if not mesh.uv_layers:
                warnings.append('no_uv')
            if obj.matrix_world.determinant() < 0:
                warnings.append('negative_world_scale')
            if not mesh.materials or any(m is None for m in mesh.materials):
                warnings.append('empty_material_slots')
            rows.append(dict(name=obj.name, vertices=len(mesh.vertices), triangles=len(mesh.loop_triangles),
                             dimensions=list(obj.dimensions), warnings=warnings))
        finally:
            evaluated.to_mesh_clear()
    return dict(blenderVersion=bpy.app.version_string, scope='evaluated scene meshes; instances not expanded; no artistic approval',
                unitScale=bpy.context.scene.unit_settings.scale_length, meshes=rows,
                totalTriangles=sum(row['triangles'] for row in rows))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', required=True)
    args = parser.parse_args(sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else [])
    target = Path(args.report)
    # Exclusive create also protects source files from accidental replacement.
    with target.open('x', encoding='utf-8') as stream:
        json.dump(audit_scene(), stream, ensure_ascii=False, indent=2)
