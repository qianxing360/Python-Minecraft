# -*- coding: UTF-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

size = 20
'''
pos = mc.player.getTilePos()
x = pos.x+2
y = pos.y
z = pos.z
'''
x = 0
y = 0
z = 0

midx = x+size/2
midy = y+size/2

# 建造房子主体
mc.setBlocks(x, y, z, x+size, y+size, z+size, block.STONE.id)
mc.setBlocks(x+1, y, z+1, x+size-1, y+size-1, z+size-1, block.AIR.id)

# 建造门
mc.setBlocks(midx-1, y, z, midx+1, y+3, z, block.AIR.id)

# 建造窗户
mc.setBlocks(x+3, midy+3, z, midx-3, y+size-3, z, block.GLASS.id)
mc.setBlocks(midx+3, midy+3, z, x+size-3, y+size-3, z, block.GLASS.id)

# 建造屋顶
mc.setBlocks(x, y+size+1, z, x+size, y+size+1, z+size, block.WOOD.id)

# 建造羊毛地毯
mc.setBlocks(x, y-1, z, x+size, y-1, z+size, block.WOOL.id, 11)
