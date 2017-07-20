import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x+2
y = pos.y
z = pos.z+2

list_a = [[0,0,0,1,0,0,1],
          [0,0,0,1,0,0,1],
          [0,0,0,1,0,0,1],
          [1,1,1,1,1,1,1],
          [0,0,0,1,0,0,1],
          [0,0,0,1,0,0,1],
          [0,0,0,1,0,0,1],
          [1,0,0,1,0,0,1],
          [1,1,1,1,1,1,1]]

for i in range(0, 9):
    for j in range(0, 7):
        if list_a[i][j] == 1:
            mc.setBlock(x+j,y+i,z,block.TNT.id)
        if list_a[i][j] == 0:
            mc.setBlock(x+j,y+i,z,block.STONE.id)
