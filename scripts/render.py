import mitsuba as mi
import sys

args = sys.argv

mi.set_variant('cuda_ad_rgb')

scene = mi.load_file("scene.xml")

image = mi.render(scene)

mi.util.write_bitmap("sample.png", image)