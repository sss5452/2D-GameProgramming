import gfw
from pico2d import *
from setting import *
import game_state
import player
import random

RES_DIR = '../res'

def init(count):
    global stage, wall,potal
    wall = load_image(RES_DIR + '/wall.png')
    potal = load_image(RES_DIR + '/potal.png')
    stage = count
def draw():
    global stage
    #self.image.draw(*PLATFORM_LISTX[0])
    #self.image.draw(*PLATFORM_LISTX[1])
    if stage == 1:
        for (x,y) in ST1_PLATFORM_LIST:
            wall.draw(x,y)
            potal.draw(100,70)
    if stage == 2:
        for (x,y) in ST2_PLATFORM_LIST:
            wall.draw(x,y)
def update():
    pass
