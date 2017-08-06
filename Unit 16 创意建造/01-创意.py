# -*- coding:utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff
import mcpi.block as block
import time
import math
import random

mc = minecraft.Minecraft.create()

mcdrawing = minecraftstuff.MinecraftDrawing(mc)


class CreateFriend:
    def __init__(self, name, pos):
        self.name = name
        self.x = pos.x
        self.y = pos.y+1
        self.z = pos.z
        mc.setBlock(self.x, self.y, self.z, 86)

    def move_by(self, x, y, z):
        mc.setBlock(self.x, self.y, self.z, block.AIR.id)
        mc.setBlock(self.x+x, self.y+y, self.z+z, 86)
        self.x = self.x+x
        self.y = self.y+y
        self.z = self.z+z

    def move(self, x, y, z):
        mc.setBlock(self.x, self.y, self.z, block.AIR.id)
        mc.setBlock(x, y, z, 86)
        self.x = x
        self.y = y
        self.z = z

    def say(self, word):
        mc.postToChat(self.name + ':')
        mc.postToChat(word)


def getDistance(p1, p2):
    xd = p1.x - p2.x
    yd = p1.y - p2.y
    zd = p1.z - p2.z
    return math.sqrt(xd*xd + yd*yd + zd*zd)

friend_pos = mc.player.getTilePos()

bob = CreateFriend('bob', friend_pos)
print bob.name, bob.x, bob.y, bob.z


while True:
    player_pos = mc.player.getTilePos()

    distance = getDistance(player_pos, bob)
    print distance

    if distance > 10:
        bob.move(player_pos.x-1, player_pos.y, player_pos.z)
        bob.say('Wait me!')

    a = random.randint(-1, 1)
    if a != 0:
        bob.move_by(a, 0, a)
    time.sleep(1)
