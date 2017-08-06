# -*- coding:utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time

mc = minecraft.Minecraft.create()

# 设计jack模型的形状
jackBlocks = [minecraftstuff.ShapeBlock(0, 0, 0, 1),
              minecraftstuff.ShapeBlock(0, 1, 0, 86),
              minecraftstuff.ShapeBlock(1, 0, 0, 89),
              minecraftstuff.ShapeBlock(-1, 0, 0, 89),
              minecraftstuff.ShapeBlock(0, 0, 1, 89),
              minecraftstuff.ShapeBlock(0, 0, -1, 89),
              minecraftstuff.ShapeBlock(0, -1, 0, 89)]

pos = mc.player.getTilePos()
pos.y = pos.y + 1
pos.z = pos.z + 1  # 修改pos.z坐标，防止模型生成在玩家身上

# 建造Jack
jackShape = minecraftstuff.MinecraftShape(mc, pos, jackBlocks)

# 让Jack动起来
for count in range(0, 20):
    time.sleep(1)
    jackShape.moveBy(0, 0, 1)

# 清除jack模型
jackShape.clear()
