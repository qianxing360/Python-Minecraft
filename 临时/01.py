list_a = [[0,1,0,0], [0,1,0,0], [0,1,1,1], [0,1,0,0]]


for i in range(0, 4):
    print list_a[i]  # list_a[1]
    for j in range(0, 4):
        print list_a[i][j]  # list_a[0][3]

        if list_a[i][j] == 1:
            mc.setBlock(x+i, y, z+j,block.STONE.id)
        else:
            mc.setBlock(x+i, y, z+j, block.STONE.id)