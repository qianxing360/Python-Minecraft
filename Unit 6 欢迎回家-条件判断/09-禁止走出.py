import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

#mc.player.setTilePos(0, 10, 0)
mc.setBlocks(-5,-1,-5,5,1,5,0)
mc.setBlocks(-5,-1,-5,5,-1,5,152)
mc.setBlocks(-4,-1,-4,4,-1,4,block.STONE.id)

while True:
    pos = mc.player.getTilePos()
    if not ((-5<= pos.x <= 5) and (-5<= pos.z <= 5)):
        mc.player.setTilePos(0, pos.y, 0)

        mc.setBlocks(-5, -1, -5, 5, -1, 5, 152)
        mc.setBlocks(-4, -1, -4, 4, -1, 4, block.STONE.id)
        time.sleep(1)
