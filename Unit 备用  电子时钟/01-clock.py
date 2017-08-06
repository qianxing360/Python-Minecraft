# -*- coding:utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
from datetime import datetime
import time

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x-1
y = pos.y
z = pos.z-5


def build_num(x=0, y=0, z=0, num=0):
    numbers = {0: [(1, 1, 1), (1, 0, 1), (1, 0, 1), (1, 0, 1), (1, 1, 1)],
               1: [(1, 1, 1), (0, 1, 0), (0, 1, 0), (0, 1, 0), (1, 1, 0)],
               2: [(1, 1, 1), (1, 0, 0), (1, 1, 1), (0, 0, 1), (1, 1, 1)],
               3: [(1, 1, 1), (0, 0, 1), (1, 1, 1), (0, 0, 1), (1, 1, 1)],
               4: [(0, 0, 1), (0, 0, 1), (1, 1, 1), (1, 0, 1), (1, 0, 1)],
               5: [(1, 1, 1), (0, 0, 1), (1, 1, 1), (1, 0, 0), (1, 1, 1)],
               6: [(1, 1, 1), (1, 0, 1), (1, 1, 1), (1, 0, 0), (1, 1, 1)],
               7: [(0, 0, 1), (0, 0, 1), (0, 0, 1), (1, 0, 1), (1, 1, 1)],
               8: [(1, 1, 1), (1, 0, 1), (1, 1, 1), (1, 0, 1), (1, 1, 1)],
               9: [(1, 1, 1), (0, 0, 1), (1, 1, 1), (1, 0, 1), (1, 1, 1)]}

    for i in range(0, 5):
        for j in range(0, 3):
            if numbers[num][i][j] == 1:
                mc.setBlock(x+j, y+i, z, block.WOOL.id, 3)
            if numbers[num][i][j] == 0:
                mc.setBlock(x+j, y+i, z, block.AIR.id)

while True:

    today = datetime.now()  # 获取当前的时间
    hour = today.hour  # 获取当前的小时
    minute = today.minute  # 获取当前的分钟
    second = today.second  # 获取当前的秒

    # 建造 ‘时’ 方块
    build_num(x, y, z, hour//10)
    build_num(x+4, y, z, hour % 10)
    # 建造 冒号 方块
    mc.setBlock(x+8, y+1, z, block.WOOL.id, 1)
    mc.setBlock(x+8, y+3, z, block.WOOL.id, 1)
    # 建造 ‘分’ 方块
    build_num(x+10, y, z, minute//10)
    build_num(x+14, y, z, minute % 10)
    # 建造 冒号 方块
    mc.setBlock(x+18, y+1, z, block.WOOL.id, 1)
    mc.setBlock(x+18, y+3, z, block.WOOL.id, 1)
    # 建造 ‘秒’ 方块
    build_num(x+20, y, z, second//10)
    build_num(x+24, y, z, second % 10)

    time.sleep(1)