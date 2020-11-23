from pico2d import *
import gfw
import gobj
import player
import random
MOVE_PPS = 200

GET_BULLET_TYPE = 0
GET_COUNTER_ATTACK = False

class Player_bullet:
    def __init__(self,type,dir):
        self.plant = gfw.image.load('../res/plant_bullet.png')
        self.tree = gfw.image.load('../res/tree_bullet.png')
        self.bomb_pig = gfw.image.load('../res/bomb.png')
        layer = list(gfw.world.objects_at(gfw.layer.player))
        self.type = type
        self.fl = dir
        self.player = layer[0]
        self.pos = self.player.pos
        self.target = player.target
        x, y = self.target
        a, b = self.pos
        self.delta = x - a, y - b
        self.bomdelta = x - a + random.randint(-10, 10), 8
        self.rad = 0
        self.sx =0

    def update(self):
        global x,y
        # x,y = self.pos
        # dx,dy = self.delta
        # x += dx * gfw.delta_time
        # y += dy * gfw.delta_time
        # self.pos = x,y
        if self.type == 1:
            x,y = self.plant_bullet()
        elif self.type == 2:
            x,y = self.Tree_bullet()
        elif self.type ==3:
            x,y = self.Bomb_bullet()
        if x > get_canvas_width() or x< 0 or y > get_canvas_height() or y < 0:
            self.remove()

    def handle_event(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN:
            self.target = (e.x ,get_canvas_height() - e.y - 1)  #화면 밖 제거
            print(self.target)
            x, y = self.target
            a,b = self.pos
            self.delta = x-a, y-b

    def draw(self):
        if self.type == 1:
            self.plant.draw(*self.pos)
        elif self.type == 2:
            self.tree.composite_draw(0, self.fl, *self.pos)
        elif self.type == 3:
            self.sx += 52
            self.rad += 0.2
            self.bomb_pig.clip_composite_draw(self.sx, 0, 52, 52, self.rad, self.fl, *self.pos, 104, 104)
            if self.sx == 208: self.sx =0
    def plant_bullet(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx * gfw.delta_time
        y += dy * gfw.delta_time
        self.pos = x,y
        return self.pos

    def Tree_bullet(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx * gfw.delta_time
        y += dy * gfw.delta_time
        self.pos = x,y
        return self.pos

    def Bomb_bullet(self):
        x, y = self.pos
        dx, dy = self.bomdelta
        x += dx * gfw.delta_time
        y += dy
        gravity = 0.3
        dy -= gravity
        self.pos = x, y
        self.bomdelta = dx, dy
        return self.pos
    def remove(self):
        gfw.world.remove(self)

class Enemy_bullet:
    SIZE = 60
    def __init__(self,pos,type,dir):
        self.type = type
        self.pos = pos
        self.fl = dir
        self.plant = gfw.image.load('../res/plant_bullet.png')
        self.tree = gfw.image.load('../res/tree_bullet.png')
        self.bomb_pig = gfw.image.load('../res/bomb.png')
        layer = list(gfw.world.objects_at(gfw.layer.player))
        self.target = layer[0]
        x, y = self.target.pos
        a, b = self.pos
        self.delta = x-a, y-b
        self.bomdelta = x-a + random.randint(-10,10),8
        self.mouse_target = 0,0
        self.sx =0
        self.rad = 0
    def update(self):
        global x, y
        # x,y = self.pos
        # dx,dy = self.delta
        # x += dx * gfw.delta_time
        # y += dy * gfw.delta_time
        # self.pos = x,y
        if self.type == 1:
            x,y = self.plant_bullet()
        elif self.type == 2:
            x,y = self.Tree_bullet()
        elif self.type ==3:
            x,y = self.Bomb_bullet()

        if gobj.collides_box(self, self.target):        #플레이어 or 쉴드 충돌
            if player.Player.checkShiled(self.target):  #쉴드 충돌
                self.remove()
                global GET_BULLET_TYPE , GET_COUNTER_ATTACK
                GET_BULLET_TYPE = self.type
                GET_COUNTER_ATTACK = True
            else:                                       #플레이어 충돌
                self.remove()
        if x > get_canvas_width() or x< 0 or y > get_canvas_height() or y < 0: #화면 밖 제거
            self.remove()

    def draw(self):
        if self.type == 1:
            self.plant.draw(*self.pos)
        if self.type == 2:
            #self.tree.draw(*self.pos)
            self.tree.composite_draw(0,self.fl, *self.pos)
        if self.type == 3:
            self.sx += 52
            self.rad += 0.2
            self.bomb_pig.clip_composite_draw(self.sx, 0, 52, 52, self.rad, self.fl, *self.pos, 104, 104)
            if self.sx == 208: self.sx =0

    def get_bb(self):
        x,y = self.pos
        return x - 4, y - 4, x + 4, y + 4

    def remove(self):
        gfw.world.remove(self)

    def plant_bullet(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx * gfw.delta_time
        y += dy * gfw.delta_time
        self.pos = x,y
        return self.pos

    def Tree_bullet(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx * gfw.delta_time
        y += dy * gfw.delta_time
        self.pos = x,y
        return self.pos

    def Bomb_bullet(self):
        x, y = self.pos
        dx, dy = self.bomdelta
        x += dx * gfw.delta_time
        y += dy
        gravity = 0.3
        dy -= gravity
        self.pos = x, y
        self.bomdelta = dx, dy
        return self.pos


