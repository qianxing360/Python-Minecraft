# -*- coding:utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

ROAD = block.AIR.id  # 道路
WALL = block.STONE.id  # 墙
FLOOR = block.GRASS.id  # 地板

pos = mc.player.getTilePos()
XX = pos.x+3
YY = pos.y
ZZ = pos.z+3

file = open("maze.csv","r")

z = ZZ

for line in file.readlines():
    date = line.split(",")
    print date
    x = XX
    for cell in date:
        if cell == "0":
            BLOCK = ROAD
        else:
            BLOCK = WALL
        mc.setBlock(x, YY, z, BLOCK)
        mc.setBlock(x, YY+1, z, BLOCK)
        mc.setBlock(x, YY-1, z, FLOOR)
        x = x + 1
    z = z + 1

file.close()

