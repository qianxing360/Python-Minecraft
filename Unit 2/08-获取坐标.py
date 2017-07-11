import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getTilePos()
    playerPos_x = pos.x
    playerPos_y = pos.y
    playerPos_z = pos.z

    print 'x=', playerPos_x
    print 'y=', playerPos_y
    print 'z=', playerPos_z

    mc.postToChat('x='+str(playerPos_x) + ' y='+str(playerPos_y) + ' z='+str(playerPos_z))

    time.sleep(1)