# -*- coding: UTF-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()  # 获取自己的坐标
    b = mc.getBlock(pos.x,pos.y-1,pos.z)  # 获取自己脚下的方块类型
    # 判断方块的类型是否为空气、静态的水或者流动的水
    if b == block.AIR.id or b == block.WATER_STATIONARY.id or b == block.WATER.id:
        # 如果是，发送不安全
        mc.postToChat('Not safe!')
    else:
        # 否则，发送安全
        mc.postToChat('Safe!')
    time.sleep(0.5)