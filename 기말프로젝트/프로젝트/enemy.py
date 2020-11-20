from pico2d import *
import gfw
import random
import gobj
from setting import *
import bullet
import game_state
import platform
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import player

class Plant:
    ACTIONS = ['Attack', 'Dead', 'Idle']
    CHASE_DISTANCE_SQ = 250 ** 2
    def __init__(self,pos):
        global layer_p, b
        self.pos = pos
        self.mass = 10
        self.velY = 0
        self.accY = 0
        self.image = gfw.image.load('../res/plant_idle.png')
        self.fl = 'h'
        self.fidx = random.randint(0, 7)
        self.time = 0
        self.action = 'Idle'
        self.patrol_order = -1
        self.fire_count = 0
        #self.build_behavior_tree()
        layer = list(gfw.world.objects_at(gfw.layer.player))
        self.player = layer[0]
        layer_p = list(gfw.world.objects_at(gfw.layer.plat))
        self.plat = layer_p[0]
        back = list(gfw.world.objects_at(gfw.layer.grass))
        self.back = back[0]
    def update(self):
        global layer, layer_p, back
        layer_p = list(gfw.world.objects_at(gfw.layer.plat))     # 맵이 넘어갈때로 if문 걸었으면 좋겟다
        self.time += gfw.delta_time
        frame = self.time *15
        self.fidx = int(frame) % 11
        x,y = self.pos

        for i in range(len(layer_p)):           # 벽돌 충돌처리
            self.plat = layer_p[i]
            if gobj.collides_box(self, self.plat):
                y += PLAYER_GRAVITY * self.mass

        if gobj.collides_box(self, self.back):
            y += PLAYER_GRAVITY * self.mass
        y -= PLAYER_GRAVITY * self.mass
        self.pos =(x, y)
        self.find_player()

    def draw(self):
        sx = self.fidx * 44
        self.image.clip_composite_draw(2+sx, 0, 44, 44, 0, self.fl, *self.pos, 44, 44)
    #def attack(self):
    def fire(self):
        if self.fire_count % 100 == 0:
            b = bullet.Plant_bullet((self.pos),1)
            gfw.world.add(gfw.layer.b,b)
        self.fire_count+=1
    def find_player(self):
        dist_sq = gobj.distance_sq(self.player.pos, self.pos)
        if dist_sq < Plant.CHASE_DISTANCE_SQ:
            self.fire()
            dir = gobj.direction(self.player.pos, self.pos)
            if dir == True:
                self.fl = 'w'
            else:
                self.fl = 'h'

            if self.patrol_order >= 0:
                self.patrol_order = -1
                self.action = 'Attack'
    def remove(self):
        gfw.world.remove(self)
    def get_bb(self):
        x,y = self.pos
        return x - 20, y - 22, x + 14, y + 14