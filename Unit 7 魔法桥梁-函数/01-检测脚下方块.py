import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x,pos.y-1,pos.z)
    mc.postToChat(b)
    time.sleep(1)