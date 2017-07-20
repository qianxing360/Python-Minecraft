# -*- coding:utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

pos = mc.player.getTilePos()

x1, y1, z1 = (pos.x, pos.y, pos.z)
x2, y2, z2 = (pos.x+20, pos.y, pos.z)
x3, y3, z3 = (pos.x+20, pos.y+20, pos.z)
x4, y4, z4 = (pos.x, pos.y+20, pos.z)

points=[]
points.append(minecraft.Vec3(x1, y1, z1))
points.append(minecraft.Vec3(x2, y2, z2))
points.append(minecraft.Vec3(x3, y3, z3))
points.append(minecraft.Vec3(x4, y4, z4))

mcdrawing.drawFace(points, True, block.WOOL.id, 2)


