# -*- coding: UTF-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create(address = "localhost", name = 'I_eat_potato')

pos = mc.player.getTilePos()
# mc.player.setTilePos(0, 5, 0)

mc.setBlock(0, 0, 0, 66)

for i in range(0, 120):
    mc.setBlock(1 + i, -1, 0, 152)   # 建造x轴红石地基
    mc.setBlock(0, -1, 1 + i, 152)  # 建造z轴红石地基

    time.sleep(0.02)

for i in range(0, 120):
    mc.setBlock(0, 0, 1 + i, 27)  # 建造z轴红石铁路
    mc.setBlock(1 + i, 0, 0, 27)  # 建造x轴红石铁路

    time.sleep(0.02)

