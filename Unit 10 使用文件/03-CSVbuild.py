# -*- coding:utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

ROAD = block.AIR.id  # 使用空气当做迷宫的道路
WALL = block.STONE.id  # 使用石头当做迷宫的墙
FLOOR = block.GRASS.id  # 使用草地当做迷宫的地板

# 获取自己的坐标
pos = mc.player.getTilePos()
x = pos.x+3
y = pos.y
z = pos.z+3

# 打开maze.csv文件
file = open("maze.csv", "r")

for line in file.readlines():
    print line
    date = line.split(",")
    print date
    for i in range(len(date)):
        if date[i] == "0":
            BLOCK = ROAD
        else:
            BLOCK = WALL
        mc.setBlock(x+i, y, z, BLOCK)
        mc.setBlock(x+i, y+1, z, BLOCK)
        mc.setBlock(x+i, y-1, z, FLOOR)
    z = z+1

file.close()

