from JMSSGraphicsV124 import *

height = 600

class Particle():
    def __init__(self, img = None, x = 0, y = 0, hardness = 1):

        self.x = x
        self.y = y

        self.hardness = hardness

block_list = []
B_image1 = "Block.png"

class blockFunctions:
    def spawnBlock(self, row = 0, col = 0, hardness = 1, blist = block_list):

        b = Particle()

        b.x = 50 + 100*col
        b.y = height -100 -50*row
        b.hardness = hardness

        blist.append(b)
