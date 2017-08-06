import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

mc.postToChat('X='+str(pos.x) + ' Y='+str(pos.y) + ' Z='+str(pos.z))
print('X='+str(pos.x) + ' Y='+str(pos.y) + ' Z='+str(pos.z))
