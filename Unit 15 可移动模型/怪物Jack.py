# -*- coding:utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time

# create minecraft and minecraftdrawing objects
mc = minecraft.Minecraft.create()

# create the shape for our flying saucer
jackBlocks = [minecraftstuff.ShapeBlock(0, 0, 0, 89),
               minecraftstuff.ShapeBlock(0, 1, 0, 89),
               minecraftstuff.ShapeBlock(0, 2, 0, 89),
               minecraftstuff.ShapeBlock(-1, 2, 0, 46),
               minecraftstuff.ShapeBlock(1, 2, 0, 46),
               minecraftstuff.ShapeBlock(0, 3, 0, 86)]

#set the horses position
pos = mc.player.getTilePos()
pos.z = pos.z + 1

# 建造Jack
jackShape = minecraftstuff.MinecraftShape(mc, pos, jackBlocks)

# 让Jack动起来
for count in range(1,20):
    time.sleep(1)
    jackShape.moveBy(0,0,1)

jackShape.clear()