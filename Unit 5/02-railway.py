# -*- coding: UTF-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
'''
x = pos.x+2
y = pos.y
z = pos.z
'''
x = 0
y = 0
z = 0

for i in range(0, 100):
    mc.setBlock(x+i, y-1, z, 152)
    mc.setBlock(x+i, y, z, 27)
    time.sleep(0.02)

for i in range(0, 100):
    mc.setBlock(x+100, y-1, z+i, 152)
    mc.setBlock(x+100, y, z+i, 27)
    time.sleep(0.02)

for i in range(0, 100):
    mc.setBlock(x, y-1, z+i, 152)
    mc.setBlock(x, y, z+i, 27)
    time.sleep(0.02)

for i in range(0, 100):
    mc.setBlock(x+i, y-1, z+100, 152)
    mc.setBlock(x+i, y, z+100, 27)
    time.sleep(0.02)
