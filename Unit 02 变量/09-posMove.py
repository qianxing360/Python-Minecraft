import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
playerPos_x = pos.x
playerPos_y = pos.y
playerPos_z = pos.z

mc.postToChat('x=' + str(playerPos_x) + ' y=' + str(playerPos_y) + ' z=' + str(playerPos_z))

posMove = int(raw_input('enter the pos:'))
mc.player.setTilePos(playerPos_x + posMove, playerPos_y, playerPos_z)