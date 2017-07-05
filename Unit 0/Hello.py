import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

for i in range(0, 1000):
    mc.setBlock(x+i, y, z, block.STONE.id)
    time.sleep(0.01)

