import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create()

def buildBridge(BLOCK):
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x,pos.y-1,pos.z)
    if b == block.AIR.id or b == block.WATER_STATIONARY.id or b == block.WATER.id:
        mc.setBlock(pos.x,pos.y-1,pos.z,BLOCK)

while True:
    block_name = random.randint(1,4)
    buildBridge(block_name)