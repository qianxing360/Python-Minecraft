import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    mc.postToChat('X='+str(pos.x) + ' Y='+str(pos.y) + ' Z='+str(pos.z))
    print 'X='+str(pos.x) + ' Y='+str(pos.y) + ' Z='+str(pos.z)
    time.sleep(1)
