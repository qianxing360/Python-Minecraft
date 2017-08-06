import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    mc.postToChat('x='+str(pos.x) + ' y='+str(pos.y) + ' z='+str(pos.z))
    time.sleep(1)