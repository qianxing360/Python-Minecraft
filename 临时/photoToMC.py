import mcpi.minecraft as minecraft
import mcpi.block as block
from PIL import Image
import time

mc = minecraft.Minecraft.create("127.0.0.1", name="I_eat_potato")

white = (255, 255, 255)
black = (0, 0, 0)
gray = (127, 127, 127)
brown = (136, 0, 21)
red = (237, 28, 36)
orange = (255, 127, 39)
yellow = (255, 242, 0)
green = (34, 177, 76)
litblue = (0, 162, 232)
blue = (63, 72, 204)
purple = (163, 73, 164)


Blocks = {white: (35, 0),
          black: (35, 15),
          gray: (35, 8),
          brown: (35, 12),
          red: (35, 14),
          orange: (35, 1),
          yellow: (35, 4),
          green: (35, 13),
          litblue: (35, 3),
          blue: (35, 11),
          purple: (35, 10),
          }

pos = mc.player.getTilePos()

im = Image.open('06.png')
rgb_im = im.convert('RGB')
rows, columns = rgb_im.size
print rows, columns
for r in range(rows):
    for c in range(columns):
        rgb = rgb_im.getpixel((r, c))
        if rgb in Blocks:
            mc.setBlock(pos.x + r, pos.y, pos.z + c, Blocks[rgb][0], Blocks[rgb][1])
            time.sleep(0.001)
        else:
            mc.setBlock(pos.x + r, pos.y, pos.z + c, 35, 2)
            time.sleep(0.001)
