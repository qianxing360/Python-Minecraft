# -*- coding:utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
from PIL import Image
import time

'''
需要 pillow 模块，可以用Pycharm自动下载。
使用windows自带的画图软件，调整好大小后（推荐100*100），用铅笔工具画图，
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
ching= (0, 162, 232)
blue = (63, 72, 204)
purple = (163, 73, 164)

pos = mc.player.getTilePos()

im = Image.open('01.png')  # 使用open( )函数加载图片，文件名需要自己修改
rgb_im = im.convert('RGB')  # 将图片转换为RGB模式，“RGB” 表示真彩色图像
rows, columns = rgb_im.size  # 获取图片的行和列的长度，并保存在rows和columns里
print rows, columns

for r in range(rows):
    for c in range(columns):
        rgb = rgb_im.getpixel((r, c))  # 获取(r, c)坐标点像素的RGB值
        print rgb
        if rgb == white:  #如果像素点是白色，就用白色羊毛
            mc.setBlock(pos.x + r, pos.y, pos.z + c, block.WOOL.id, 0)
        elif rgb == black:  #如果像素点是黑色，就用黑色羊毛
            mc.setBlock(pos.x + r, pos.y, pos.z + c, block.WOOL.id, 15)
        elif rgb == red:  #如果像素点是红色，就用红色羊毛
            mc.setBlock(pos.x + r, pos.y, pos.z + c, block.WOOL.id, 14)
        else:  # 最后如果像素的颜色上面没有，就用最后的情况
            mc.setBlock(pos.x + r, pos.y, pos.z + c, block.WOOL.id, 0)

        time.sleep(0.001)
