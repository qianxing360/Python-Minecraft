import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x,pos.y-1,pos.z)
    if b == block.AIR.id or b == block.WATER_STATIONARY.id or b == block.WATER.id:
        mc.postToChat('Not safe!')
    else:
        mc.postToChat('Safe!')
    time.sleep(0.5)