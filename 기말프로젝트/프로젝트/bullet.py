from pico2d import *
import gfw
import gobj
import player
import random
import enemy
import game_state
from collison_image import Collsion
MOVE_PPS = 200

GET_BULLET_TYPE = 0
GET_COUNTER_ATTACK = False

class Player_bullet:
    def __init__(self,type,dir):
        global layer , en_layer
        en_layer = list(gfw.world.objects_at(gfw.layer.en))
        self.en = en_layer[0]
        back = list(gfw.world.objects_at(gfw.layer.grass))
        self.back = back[0]

        self.plant = gfw.image.load('res/plant_bullet.png')
        self.tree = gfw.image.load('res/tree_bullet.png')
        self.bomb_pig = gfw.image.load('res/bomb.png')
        layer = list(gfw.world.objects_at(gfw.layer.player))
        self.type = type
        self.fl = dir
        self.player = layer[0]
        self.pos = self.player.pos
        self.target = player.target
        x1, y1 = self.target
        x2, y2 = self.pos
        self.delta = x1 - x2, y1-y2
        self.bomdelta = x1 - x2 + random.randint(-10, 10), 8
        self.rad = 0
        self.sx =0

    def update(self):
        global x,y
        if self.type == 1:
            x,y = self.plant_bullet()
        elif self.type == 2:
            x,y = self.Tree_bullet()
        elif self.type ==3:
            x,y = self.Bomb_bullet()
        if x > get_canvas_width() or x< 0 or y > get_canvas_height()+300 or y < 0:
            self.remove()
        global en_layer

        for i in range(len(en_layer)):           #몬스터 충돌
            self.en = en_layer[i]
            if gobj.collides_box(self, self.en):
                enemy.Enemy.remove(self.en)
                game_state.updateScore()
                self.remove()
                if self.type == 3:
                    game_state.sound_wav(2)
                else:
                    game_state.sound_wav(3)
        if gobj.collides_box(self,self.back):
            self.remove()
            if self.type == 3:
                game_state.sound_wav(2)
    def handle_event(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN:
            self.target = (e.x ,get_canvas_height() - e.y - 1)
            x, y = self.target
            a,b = self.pos
            self.delta = x-a, y-b

    def draw(self):
        if self.type == 1:
            self.plant.draw(*self.pos)
        elif self.type == 2:
            self.rad += 0.2
            self.tree.composite_draw(self.rad, self.fl, *self.pos)
        elif self.type == 3:
            self.sx += 52
            self.rad += 0.2
            self.bomb_pig.clip_composite_draw(self.sx, 0, 52, 52, self.rad, 'w', *self.pos, 104, 104)
            if self.sx == 156: self.sx = 0

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
        ddx = 0
        ddy = 0
        if dx >0:
            ddx = abs(dx/dx) * 500
        elif dx <0:
            ddx = abs(dx / dx) * -500
        if dy < 0:
            ddy = abs(dy/dx) * -500
        elif dy > 0:
            ddy = abs(dy/dx) * 500
        x += ddx * gfw.delta_time
        y += ddy * gfw.delta_time
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

    def get_bb(self):
        x,y = self.pos
        if self.type == 3:
            x -=5
            y -=5
            return x - 10, y - 10, x + 10, y + 10
        else:
            return x - 4, y - 4, x + 4, y + 4

    def remove(self):
        obj_dead = Collsion(self.pos,self.type,self.fl,True)
        gfw.world.add(gfw.layer.obj_dead, obj_dead)
        gfw.world.remove(self)

class Enemy_bullet:
    SIZE = 60
    def __init__(self,pos,type,dir):
        layer = list(gfw.world.objects_at(gfw.layer.player))
        self.target = layer[0]
        back = list(gfw.world.objects_at(gfw.layer.grass))
        self.back = back[0]
        self.type = type
        self.pos = pos
        self.fl = dir
        self.plant = gfw.image.load('res/plant_bullet.png')
        self.tree = gfw.image.load('res/tree_bullet.png')
        self.bomb_pig = gfw.image.load('res/bomb.png')
        x, y = self.target.pos
        a, b = self.pos
        self.delta = x - a, y - b
        self.bomdelta = x-a + random.randint(-10,10),8
        self.mouse_target = 0,0
        self.sx =0
        self.rad = 0

    def update(self):
        global x, y

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
                dead = player.Player.decrease_life(self.target)
                if dead:
                    game_state.sound_wav(6)
                    game_state.endGame()
                self.coll_img()
                self.remove()
                if self.type == 3:
                    game_state.sound_wav(2)
        if gobj.collides_box(self,self.back):
            self.coll_img()
            self.remove()
            if self.type == 3:
                game_state.sound_wav(2)
        if x > get_canvas_width() or x< 0 or y > get_canvas_height()+300 or y < 0: #화면 밖 제거
            self.remove()

    def draw(self):
        if self.type == 1:
            self.plant.draw(*self.pos)
        if self.type == 2:
            #self.tree.draw(*self.pos)
            self.rad +=0.2
            self.tree.composite_draw(self.rad,self.fl, *self.pos)
        if self.type == 3:
            self.sx += 52
            self.rad += 0.2
            self.bomb_pig.clip_composite_draw(self.sx, 0, 52, 56, self.rad, self.fl, *self.pos, 104, 112)
            if self.sx == 156: self.sx =0

    def get_bb(self):
        x,y = self.pos
        if self.type == 3:
            x -=5
            y -=5
            return x - 10, y - 10, x + 10, y + 10
        else:
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
        if dx > 0:
            ddx = 500
        else:
            ddx = -500
        x += ddx * gfw.delta_time
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

    def coll_img(self):
        obj_dead = Collsion(self.pos,self.type,self.fl,True)
        gfw.world.add(gfw.layer.obj_dead, obj_dead)


