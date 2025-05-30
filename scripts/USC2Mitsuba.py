import math
import struct
import array

src_path = "../resources/strands00001.data"
dst_path = "../resources/hair.mcur"
hair_radii = 0.0015

def calc_local_radii(v, len):
    return hair_radii * (1.0 - 1.0 * math.sqrt(v / len))

fin = open(src_path, "rb")
fout = open(dst_path, "w")

num_strands = struct.unpack('<i', fin.read(4))[0]

for s in range(1, num_strands):  
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

print(f"USC2MitsubaCurve : {src_path} -> {dst_path}")
