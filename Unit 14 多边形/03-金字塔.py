# -*- coding:utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

pos = mc.player.getTilePos()
x = pos.x+30
y = pos.y
z = pos.z

x0, y0, z0 = (x, y+20, z)
x1, y1, z1 = (x-20, y, z-20)
x2, y2, z2 = (x+20, y, z-20)
x3, y3, z3 = (x+20, y, z+20)
x4, y4, z4 = (x-20, y, z+20)

points0=[]
points1=[]
points2=[]
points3=[]
points4=[]

# 建造底面
points0.append(minecraft.Vec3(x1, y1, z1))
points0.append(minecraft.Vec3(x2, y2, z2))
points0.append(minecraft.Vec3(x3, y3, z3))
points0.append(minecraft.Vec3(x4, y4, z4))

# 第一个三角形面
points1.append(minecraft.Vec3(x0, y0, z0))
points1.append(minecraft.Vec3(x1, y1, z1))
points1.append(minecraft.Vec3(x2, y2, z2))

# 第二个三角形面
points2.append(minecraft.Vec3(x0, y0, z0))
points2.append(minecraft.Vec3(x2, y2, z2))
points2.append(minecraft.Vec3(x3, y3, z3))

# 第三个三角形面
points3.append(minecraft.Vec3(x0, y0, z0))
points3.append(minecraft.Vec3(x3, y3, z3))
points3.append(minecraft.Vec3(x4, y4, z4))
# 第四个三角形面
points4.append(minecraft.Vec3(x0, y0, z0))
points4.append(minecraft.Vec3(x4, y4, z4))
points4.append(minecraft.Vec3(x1, y1, z1))

mcdrawing.drawFace(points0, True, block.WOOL.id, 2)
mcdrawing.drawFace(points1, True, block.WOOL.id, 2)
mcdrawing.drawFace(points2, True, block.WOOL.id, 2)
mcdrawing.drawFace(points3, True, block.WOOL.id, 2)
mcdrawing.drawFace(points4, True, block.WOOL.id, 2)


