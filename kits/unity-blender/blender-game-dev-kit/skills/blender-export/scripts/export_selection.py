"""Static FBX candidate export with explicit objects and restored selection."""
from pathlib import Path
import bpy


def export_static_fbx(objects, destination):
    target = Path(destination).resolve()
    objects = list(objects)
    if target.suffix.lower() != '.fbx' or target.exists():
        raise ValueError('Destination must be a new .fbx file')
    if not target.parent.is_dir():
        raise ValueError('Destination directory must already exist')
    if bpy.context.mode != 'OBJECT' or not objects:
        raise ValueError('Object Mode and nonempty explicit object list required')
    if any(o.type not in {'MESH', 'EMPTY'} or o.name not in bpy.context.view_layer.objects
           or o.hide_get() or o.hide_select or not o.visible_get() for o in objects):
        raise ValueError('Static visible/selectable meshes or empties in current view layer only')
    if not any(o.type == 'MESH' for o in objects):
        raise ValueError('At least one mesh is required')
    selected = list(bpy.context.selected_objects)
    active = bpy.context.view_layer.objects.active
    # Reserve path exclusively to prevent concurrent overwrite.
    with target.open('xb'):
        pass
    try:
        for obj in selected:
            obj.select_set(False)
        for obj in objects:
            obj.select_set(True)
        bpy.context.view_layer.objects.active = objects[0]
        result = bpy.ops.export_scene.fbx(filepath=str(target), check_existing=False,
            use_selection=True, object_types={'MESH', 'EMPTY'}, axis_forward='-Z', axis_up='Y',
            apply_unit_scale=True, add_leaf_bones=False, bake_anim=False, path_mode='AUTO')
        if 'FINISHED' not in result or target.stat().st_size == 0:
            raise RuntimeError('FBX export failed')
    except Exception:
        target.unlink(missing_ok=True)
        raise
    finally:
        for obj in bpy.context.selected_objects:
            obj.select_set(False)
        for obj in selected:
            obj.select_set(True)
        bpy.context.view_layer.objects.active = active
    return target
