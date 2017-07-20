# -*- coding:utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff
import mcpi.block as block
import time
import math

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

playerPos = mc.player.getTilePos()
friendPos = mc.player.getTilePos()
friendPos.x = friendPos.x+5


def distanceBetweenPoints(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    distance = math.sqrt((xd*xd) + (yd*yd) + (zd*zd))

    return distance


def jackBlock():
    jackBlocks = [minecraftstuff.ShapeBlock(0, 0, 0, 89),
                   minecraftstuff.ShapeBlock(0, 1, 0, 89),
                   minecraftstuff.ShapeBlock(0, 2, 0, 89),
                   minecraftstuff.ShapeBlock(-1, 2, 0, 46),
                   minecraftstuff.ShapeBlock(1, 2, 0, 46),
                   minecraftstuff.ShapeBlock(0, 3, 0, 86)]

    pos = mc.player.getTilePos()
    pos.z = pos.z + 1

    # 建造Jack
    jackShape = minecraftstuff.MinecraftShape(mc, pos, jackBlocks)

    return jackShape

friend = jackBlock()

for count in range(1,20):
    time.sleep(1)
    friend.moveBy(0,0,1)

friend.clear()