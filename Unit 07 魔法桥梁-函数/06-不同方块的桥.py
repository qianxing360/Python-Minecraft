# -*- coding: UTF-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
import random

mc = minecraft.Minecraft.create()


def build_bridge(BLOCK):
    pos = mc.player.getTilePos()  # 获取自己的坐标
    b = mc.getBlock(pos.x,pos.y-1,pos.z)  # 获取自己脚下的方块类型
    # 判断方块的类型是否为空气、静态的水或者流动的水
    if b == block.AIR.id or b == block.WATER_STATIONARY.id or b == block.WATER.id:
        # 如果是，就在脚下放置一个方块
        mc.setBlock(pos.x,pos.y-1,pos.z,BLOCK)

while True:
    block_name = random.randint(1,4)  # 生成一个1-4的随机数，用来代替方块
    build_bridge(block_name)
