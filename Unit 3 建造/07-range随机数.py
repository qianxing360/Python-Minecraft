import mcpi.minecraft as minecraft
import mcpi.block as block
import random

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x+2
y = pos.y
z = pos.z

random_num = random.randint(0, 15)
mc.setBlocks(x, y, z, x+3, y+4, z+5, block.WOOL.id, random_num)