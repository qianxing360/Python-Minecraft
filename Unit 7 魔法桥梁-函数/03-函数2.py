# -*- coding: UTF-8 -*-


# 将打印星号的代码变成一个函数，注意第二行前空四格
def get_stars():
    for i in range(3):
        for j in range(5):
            print '*',
        print

#在需要的时候使用函数名调用函数
get_stars()

