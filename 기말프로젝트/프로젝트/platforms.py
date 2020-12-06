import gfw
from pico2d import *
import gobj
import game_state

POTALON = False
POTAL_TO_NEXT = False
class Platform:
    def __init__(self,count, x, y):
        self.wall = load_image('res/block_grass.png')
        self.wall_last = load_image('res/block_wall.png')
        self.potal = load_image('res/potal_c.png')
        self.stage = count
        self.pos = x,y
        self.potal_pos = get_canvas_width()//2,80
        self.rad = 0
    def draw(self):
        if game_state.count == 4:
            self.wall_last.draw(*self.pos)
        else:
            self.wall.draw(*self.pos)
    def update(self):
        global POTALON
        if gfw.world.count_at(gfw.layer.en) == 0 and POTALON == False:
            potal = Potal()
            gfw.world.add(gfw.layer.potal,potal)
            POTALON = True
    def get_bb(self):
         x,y = self.pos
         return x - self.wall.w//2, y - self.wall.h//2, x + self.wall.w//2,  y +self.wall.h//2

class Potal:
    def __init__(self):
        layer = list(gfw.world.objects_at(gfw.layer.player))
        self.target = layer[0]

        self.image = load_image('res/potal_c.png')
        self.pos = get_canvas_width()//2,80
        self.rad =0
    def draw(self):
        global POTALON
        if POTALON:
            self.rad += 1
            self.image.composite_draw(self.rad, 'w', *self.pos)
    def update(self):
        global POTALON , POTAL_TO_NEXT
        if POTALON:
            if gobj.collides_box(self, self.target):
                POTAL_TO_NEXT = True
            else:
                POTAL_TO_NEXT = False
    def get_bb(self):
        x, y = self.pos
        return x - self.image.w // 2, y - self.image.h // 2, x + self.image.w // 2, y + self.image.h // 2


class Grass:
    def __init__(self):
        self.image = load_image('res/grass_ground.png')
        self.image_last = load_image('res/wallground.png')
        self.pos = 600,20
        self.rad = 0
    def draw(self):
        if game_state.count == 4:
            self.image_last.draw(*self.pos)
        else:
            self.image.draw(*self.pos)
    def update(self):
        pass
    def get_bb(self):
        x,y = self.pos
        return x - 1000, y - 100, x + 1000, y + 28