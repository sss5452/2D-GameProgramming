from pico2d import *
import gfw
import gobj
import player
MOVE_PPS = 200

GET_BULLET_TYPE = 0
GET_COUNTER_ATTACK = False

class Player_bullet:
    def __init__(self,type):
        self.image = gfw.image.load('../res/plant_bullet.png')
        layer = list(gfw.world.objects_at(gfw.layer.player))
        self.player = layer[0]
        self.pos = self.player.pos
        self.delta =0,0
        self.target = player.target
        x, y = self.target
        a, b = self.pos
        self.delta = x - a, y - b
    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx * gfw.delta_time
        y += dy * gfw.delta_time
        self.pos = x,y
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
        self.image.draw(*self.pos)

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
        layer = list(gfw.world.objects_at(gfw.layer.player))
        self.target = layer[0]
        x, y = self.target.pos
        a, b = self.pos
        self.delta = x-a, y-b
        self.mouse_target = 0,0
    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx * gfw.delta_time
        y += dy * gfw.delta_time
        self.pos = x,y

        if gobj.collides_box(self, self.target):#플레이어 or 쉴드 충돌
            if player.Player.checkShiled(self.target):  #쉴드 충돌
                self.remove()
                global GET_BULLET_TYPE , GET_COUNTER_ATTACK
                GET_BULLET_TYPE = 1
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
    def get_bb(self):
        x,y = self.pos
        return x - 4, y - 4, x + 4, y + 4
    def remove(self):
        gfw.world.remove(self)

