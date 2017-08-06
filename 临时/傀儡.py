# -*- coding: UTF-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create(address="192.168.1.104", name='I_eat_potato')
'''
x = random.randint(-10, 10)
y = random.randint(0, 10)
z = random.randint(-10, 10)
'''

pos = mc.player.getTilePos()
x = pos.x+2
y = pos.y
z = pos.z


for i in range(0,10,5):
    mc.setBlock(x+i,y+1,z,42)
    mc.setBlock(x+i,y+2,z,42)
    mc.setBlock(x-1+i, y+2, z, 42)
    mc.setBlock(x+1 + i,y +2, z, 42)
    mc.setBlock(x+i,y+3,z,86)
    time.sleep(0.1)

'''
for i in range(0,50,4):
    #建造固定位置
    mc.setBlock(x+i,y-1,z+3,1)
    mc.setBlock(x-1+i,y,z+3,126)
    mc.setBlock(x+1+i,y,z+3,126)
    mc.setBlock(x+i,y,z+2,126)
    mc.setBlock(x+i,y,z+4,126)
    # 建造雪人
    mc.setBlock(x+i,y,z+3,80)
    mc.setBlock(x+i,y+1,z+3,80)
    mc.setBlock(x+i,y+2,z+3,86)
    mc.setBlock(x+i,y+2,z+3,4)
    time.sleep(0.1)
'''