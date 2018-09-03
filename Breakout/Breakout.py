from Blocks import *

jmss = Graphics(width = 800, height = 600, title = "Game" , fps = -1)
block = blockFunctions()

block_list = []

def Draw():
    jmss.clear()
    for i in range(0, len(block_list)):
        jmss.drawImage(B_image1, block_list[i].x, block_list[i].y)

@jmss.mainloop
def Game():
    for h in range(0,7):
        for w in range(0,7):
            block.spawnBlock(h, w, 1, block_list)

    Draw()

jmss.run()
