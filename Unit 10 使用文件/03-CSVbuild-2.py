# -*- coding: cp936 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

ROAD = block.AIR.id
WALL = block.TNT.id
FLOOR = block.GRASS.id

pos = mc.player.getTilePos()
XX = pos.x+3
YY = pos.y
ZZ = pos.z+3

map_file = open("maze1.csv","r")

z = ZZ

for line in map_file.readlines():
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

map_file.close()

