# -*- coding:utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x+2
y = pos.y
z = pos.z

# 把图形文件用列表的形式表示
list_a = [[0,1,0,0], [0,1,0,0], [0,1,1,1],[0,1,0,0]]

# 用嵌套循环获取列表里面的元素，并建造对应的方跨
for i in range(0, len(list_a)):
    for j in range(0, len(list_a[i])):
        if list_a[i][j] == 1:
            mc.setBlock(x+i, y, z+j, block.STONE.id)
        else:
            mc.setBlock(x+i, y, z+j, block.AIR.id)
