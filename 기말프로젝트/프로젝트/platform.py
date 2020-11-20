import gfw
from pico2d import *
from setting import *
import game_state
import player
import random

RES_DIR = '../res'
class Platform:
    def __init__(self,count, x, y):
        self.wall = load_image(RES_DIR + '/wall.png')
        self.potal = load_image(RES_DIR + '/potal.png')
        self.stage = count
        self.pos = x,y
    def draw(self):
        self.wall.draw(*self.pos)
    def update(self):
        pass
    def get_bb(self):
         x,y = self.pos
         return x - self.wall.w//2, y - self.wall.h//2, x + self.wall.w//2,  y +self.wall.h//2

class Grass:
    def __init__(self):
        self.image = load_image(RES_DIR + '/wallground.png')
        self.pos = 600,20
        #self.wall = load_image(RES_DIR + '/wall.png')
    def draw(self):
        self.image.draw(*self.pos)
        #self.wall.draw(setting.PLATFORM_LIST2[0],setting.PLATFORM_LIST2[1])
    def update(self):
        pass
    def get_bb(self):
        x,y = self.pos
        return x - 1000, y - 30, x + 1000, y + 30