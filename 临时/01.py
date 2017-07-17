import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x+10
y = pos.y
z = pos.z

mc.setBlocks(x, y, z, x+200, y+200, z+200, block.TNT.id)
