import math
import struct
import array
import subprocess
import os

src_path = "../resources/usc/strands"
dst_path = "../resources/hair.mcur"
hair_radii = 0.0015

def calc_local_radii(v, len):
    return hair_radii * (1.0 - 1.0 * math.sqrt(v / len))

def get_5dig_str(i):
    st = str(i)
    while(len(st)<5):
        st = '0'+st
    return st

for t in range (66, 514):
    path = src_path+get_5dig_str(t)+".data"

    if not os.path.isfile(path):
        continue

    fin = open(path, "rb")
    fout = open(dst_path, "w")

    num_strands = struct.unpack('<i', fin.read(4))[0]

    for s in range(66, num_strands):  
        num_verts = struct.unpack('<i', fin.read(4))[0]

        verts = array.array('f') 
        verts.fromfile(fin, 3 * num_verts)

        if (num_verts < 2):  # skip empty roots
            continue

        for v in range(1, num_verts):
            current_radii = calc_local_radii(v, num_verts)
            
            fout.write(f"{verts[(v - 1) * 3]} {verts[(v - 1) * 3 + 1]} {verts[(v - 1) * 3 + 2]} {current_radii}\n")
        
        fout.write("\n")

    fin.close()
    fout.close()

    print(f"USC2MitsubaCurve : {path} -> {dst_path}")
    subprocess.call(["python3", "render.py", get_5dig_str(t)])
