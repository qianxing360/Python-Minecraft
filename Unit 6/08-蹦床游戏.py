import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create(address="172.29.181.63", name='sasa')

#mc.player.setTilePos(0, 10, 0)

while True:
    pos = mc.player.getTilePos()
    if (-5< pos.x < 5) and pos.y == 0 and (-5< pos.z < 5):
        mc.player.setTilePos(pos.x, pos.y+20, pos.z)
        time.sleep(1)
