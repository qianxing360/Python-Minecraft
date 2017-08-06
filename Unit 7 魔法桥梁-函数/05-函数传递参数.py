# -*- coding: UTF-8 -*-


# 定义函数的时候定义参数a和b
def get_stars(a, b):
    for i in range(a):
        for j in range(b):
            print '*',
        print

# 调用函数，并传递参数
get_stars(4, 6)
