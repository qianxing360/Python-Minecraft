import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

mc.player.setTilePos(0, 10, 0)

while True:
    pos = mc.player.getTilePos()
    if pos.x == 0 and pos.y == 0 and pos.z == 0:
        mc.postToChat('Welcom home!')
    time.sleep(1)
