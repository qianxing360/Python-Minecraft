import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    mc.postToChat('X=%d, Y=%d, Z=%d' % (pos.x, pos.y, pos.z))
    print('X=%d, Y=%d, Z=%d' % (pos.x, pos.y, pos.z))
    time.sleep(1)