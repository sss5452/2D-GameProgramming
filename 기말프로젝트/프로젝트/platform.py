import gfw
from pico2d import *
from setting import *
import gobj
import game_state
import player
import random

RES_DIR = '../res'
POTALON = False
class Platform:
    def __init__(self,count, x, y):
        layer = list(gfw.world.objects_at(gfw.layer.player))
        self.target = layer[0]
        self.wall = load_image(RES_DIR + '/block_grass.png')
        self.potal = load_image(RES_DIR + '/potal_c.png')
        self.stage = count
        self.pos = x,y
        self.map = False
        self.potal_pos = 100,80
        self.rad = 0
    def draw(self):
        self.wall.draw(*self.pos)
        if self.map:
            self.rad+= 1
            self.potal.composite_draw(self.rad,'w',*self.potal_pos)
    def update(self):
        global POTALON

        if POTALON:
            self.map = True
        elif POTALON == False:
            self.map = False

        if gfw.world.count_at(gfw.layer.en) == 0:
            self.map = True
            if gobj.collides_box(self,self.target):
                POTALON =True
    def get_bb(self):
         if self.map:
             x,y =self.potal_pos
             return x - self.potal.w//2, y - self.potal.h//2, x + self.potal.w//2,  y +self.potal.h//2
         x,y = self.pos
         return x - self.wall.w//2, y - self.wall.h//2, x + self.wall.w//2,  y +self.wall.h//2

class Grass:
    def __init__(self):
        self.image = load_image(RES_DIR + '/grass_ground.png')
        self.pos = 600,20
        #self.wall = load_image(RES_DIR + '/wall.png')
    def draw(self):
        self.image.draw(*self.pos)
        #self.wall.draw(setting.PLATFORM_LIST2[0],setting.PLATFORM_LIST2[1])
    def update(self):
        pass
    def get_bb(self):
        x,y = self.pos
        return x - 1000, y - 100, x + 1000, y + 28