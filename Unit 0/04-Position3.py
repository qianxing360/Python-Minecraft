import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

mc.postToChat('X=%d, Y=%d, Z=%d' % (pos.x, pos.y, pos.z))
mc.player.setTilePos(pos.x, pos.y+10, pos.z)
mc.postToChat('X=%d, Y=%d, Z=%d' % (pos.x, pos.y, pos.z))