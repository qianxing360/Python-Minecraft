# -*- coding: UTF-8 -*-
import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()  # 获取自己的坐标
    b = mc.getBlock(pos.x,pos.y-1,pos.z)  # 获取自己脚下的方块类型(id)
    mc.postToChat(b)  # 向聊天窗口发送方块的id
    time.sleep(1)  # 间隔1秒
