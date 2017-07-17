# -*- coding: UTF-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create(address="172.29.181.62", name='sasa1')


while True:
    #pos = mc.player.getTilePos()
    x = random.randint(-100, 100)
    y = random.randint(0, 100)
    z = random.randint(-100, 100)
    mc.player.setTilePos(x,0,z)
    mc.setBlocks(x-1,-2,z-1,x+1,1,z+1,block.TNT.id)
    mc.setBlock(x, 1, z, 152)
    mc.postToChat('aaaaaa....')


    time.sleep(10)
