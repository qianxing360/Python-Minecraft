import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

pos = mc.player.getTilePos()
x = pos.x+2
y = pos.y
z = pos.z

mcdrawing.drawLine(x, y, z, x+10, y, z, block.WOOL.id, 1)
mcdrawing.drawLine(x, y, z, x, y+10, z, block.WOOL.id, 1)
mcdrawing.drawLine(x, y, z, x, y, z+10, block.WOOL.id, 1)

