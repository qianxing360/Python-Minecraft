# -*- coding:utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

pos = mc.player.getTilePos()
x = pos.x+2
y = pos.y
z = pos.z

# 建造垂直圆
#mcdrawing.drawCircle(x, y, z, 20, block.WOOL.id, 3)
# 建造水平圆
mcdrawing.drawHorizontalCircle(x, y, z, 20, block.WOOL.id, 3)
