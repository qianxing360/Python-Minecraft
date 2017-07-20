import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x+2
y = pos.y
z = pos.z

for i in range(0, 10):
    mc.setBlock(x+i, y, z, block.STONE.id)


for i in range(0, 5):
    for j in range(0, 10):
        mc.setBlock(x+i, y+j, z, block.STONE.id)