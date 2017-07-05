import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
mc.postToChat('Hello Minecraft!')

pos = mc.player.getTilePos()
mc.postToChat('X=%d, Y=%d, Z=%d' % (pos.x, pos.y, pos.z))
print('X=%d, Y=%d, Z=%d' % (pos.x, pos.y, pos.z))

mc.setBlock(pos.x+3, pos.y, pos.z, block.STONE.id)


