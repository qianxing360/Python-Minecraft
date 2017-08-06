# -*- coding:utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
from PIL import Image
import time

'''
需要 pillow 模块，可以用Pycharm自动下载。
使用windows自带的画图软件，调整好大小后（推荐200*200），用铅笔工具画图，
最后保存为.png文件，文件名最好不要用中文，将图片文件放在.py所在目录，运行程序
'''

mc = minecraft.Minecraft.create()

# 用元组定义颜色对应的RGB，这里使用windows自带的画图软件里面默认的色彩
white = (255, 255, 255)
black = (0, 0, 0)
gray = (127, 127, 127)
brown = (136, 0, 21)
red = (237, 28, 36)
orange = (255, 127, 39)
yellow = (255, 242, 0)
green = (34, 177, 76)
light_blue = (0, 162, 232)
blue = (63, 72, 204)
purple = (163, 73, 164)

# 将颜色和对应的方块对应起来，这里使用羊毛，因为羊毛有多种颜色
BLOCKS = {white: (35, 0),
          black: (35, 15),
          gray: (35, 8),
          brown: (35, 12),
          red: (35, 14),
          orange: (35, 1),
          yellow: (35, 4),
          green: (35, 13),
          light_blue: (35, 3),
          blue: (35, 11),
          purple: (35, 10)}

pos = mc.player.getTilePos()

im = Image.open('01.png')  # 使用open( )函数加载图片，文件名需要自己修改
rgb_im = im.convert('RGB')  # 将图片转换为RGB模式，“RGB” 表示真彩色图像
rows, columns = rgb_im.size  # 获取图片的行和列的长度，并保存在rows和columns里
print rows, columns
for r in range(rows):
    for c in range(columns):
        rgb = rgb_im.getpixel((r, c))  # 获取(r, c)坐标点像素的RGB值
        if rgb in BLOCKS:  # 如果颜色的RGB在BLOCKS里面，就放置对应的方块
            mc.setBlock(pos.x+r, pos.y, pos.z+c, BLOCKS[rgb][0], BLOCKS[rgb][1])
        else:  # 如果颜色不在上面的BLOCKS里面，使用白色（背景色）代替
            mc.setBlock(pos.x+r, pos.y, pos.z+c, block.WOOL.id, 0)
        time.sleep(0.001)
