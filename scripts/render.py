import mitsuba as mi
import sys

args = sys.argv

mi.set_variant('cuda_ad_rgb')

scene = mi.load_file("scene.xml")

image = mi.render(scene)

if(len(args)>1):
	mi.util.write_bitmap(args[1]+".png", image)
else:
	mi.util.write_bitmap("sample.png", image)