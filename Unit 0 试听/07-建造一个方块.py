import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
mc.postToChat('Hello Minecraft!')

pos = mc.player.getTilePos()


mc.setBlock(pos.x+3, pos.y, pos.z, block.STONE.id)


