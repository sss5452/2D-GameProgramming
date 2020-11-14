import gfw
from pico2d import *
from setting import *
from player import *
import random

RES_DIR = '../res'

class Platform:
    def __init__(self):
        self.image = load_image(RES_DIR + '/wall.png')
        self.pt = load_image(RES_DIR + '/potal.png')
        self.stage = 1
    def draw(self):
        #self.image.draw(*PLATFORM_LISTX[0])
        #self.image.draw(*PLATFORM_LISTX[1])
        if self.stage == 1:
            for (x,y) in ST1_PLATFORM_LIST:
                self.image.draw(x,y)
            self.pt.draw(100,70)
        if self.stage == 2:
            for (x,y) in ST2_PLATFORM_LIST:
                self.image.draw(x,y)
    def potal(self):
        self.stage = 2
