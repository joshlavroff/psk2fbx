import bpy
import sys
import io_import_scene_unreal_psa_psk_280 as imp
from pathlib import Path
import os 

path='Path to psk files'
pskxFolder=Path(path)
for f in pskxFolder.glob(r"**/*"):
    if f.suffix==".pskx" or f.suffix==".psk":
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
        ctxt = bpy.context
        imp.pskimport(str(f),context=ctxt)
        bpy.ops.object.select_all(action='SELECT')
        outPath=os.path.dirname(f) +'/'+(f.name.split(".")[0]+".fbx")
        bpy.ops.export_scene.fbx(filepath=outPath)