import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create(address="172.29.181.63", name='sasa')

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
mc.player.setTilePos(0,100,0)
'''
for i in range(100):
    mc.setBlock(x+i,y-1, z, 152)
    mc.setBlock(x+i, y, z, 27)
'''