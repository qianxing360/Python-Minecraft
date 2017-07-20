# -*- coding:utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

pos = mc.player.getTilePos()
x = pos.x+25
y = pos.y
z = pos.z

mcdrawing.drawSphere(x, y, z, 20, block.WOOL.id, 3)
