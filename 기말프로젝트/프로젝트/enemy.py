from pico2d import *
import gfw
import random
import gobj
from setting import *
import bullet
from collison_image import Collsion
import game_state
import platform
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import player
type = 0
dir = 'h'
DEAD = 0

class Enemy:
    ACTIONS = ['Attack', 'Dead', 'Idle']
    CHASE_DISTANCE_SQ = 500 ** 2
    def __init__(self,pos,type):
        global layer_p, b
        self.type = type
        self.pos = pos
        self.mass = 10
        self.velY = 0
        self.accY = 0
        self.plant = gfw.image.load('../res/plant_idle.png')
        self.tree = gfw.image.load('../res/tree_idle.png')

        self.bomb_pig = gfw.image.load('../res/bomb_pig_idle.png')
        self.bomb_pig_attack = gfw.image.load('../res/bomb_pig_attack.png')

        self.fl = random.choice(['h','w'])
        self.fidx = random.randint(0, 7)
        self.time = 0
        self.action = 'Idle'
        self.patrol_order = -1
        self.fire_count = 0
        self.img_count = 0

        self.dead = 0
        self.coll = 0
        #self.build_behavior_tree()
        layer = list(gfw.world.objects_at(gfw.layer.player))
        self.player = layer[0]
        layer_p = list(gfw.world.objects_at(gfw.layer.plat))
        self.plat = layer_p
        back = list(gfw.world.objects_at(gfw.layer.grass))
        self.back = back[0]
    def update(self):
        global layer, layer_p, back
        layer_p = list(gfw.world.objects_at(gfw.layer.plat))     # 맵이 넘어갈때로 if문 걸었으면 좋겟다
        self.time += gfw.delta_time
        frame = self.time *15
        if self.type == 1 or self.type == 2:
            self.fidx = int(frame) % 11
        elif self.type == 3:
            self.fidx = int(frame) % 5
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
        if self.type == 1:
            sx = self.fidx * 44
            self.plant.clip_composite_draw(2+sx, 0, 44, 42, 0, self.fl, *self.pos, 44, 42)
        elif self.type == 2:
            sx = self.fidx * 64
            self.tree.clip_composite_draw(2 + sx, 0, 64, 32, 0, self.fl, *self.pos, 64, 32)

        elif self.type == 3:
            if self.action == 'Attack':
                sx = self.fidx * 26
                self.bomb_pig_attack.clip_composite_draw(sx, 0, 26, 26, 0, self.fl, *self.pos, 52, 52)
            else:
                sx = self.fidx * 26
                self.bomb_pig.clip_composite_draw(sx, 0, 26, 26, 0, self.fl, *self.pos, 52, 52)
    #def attack(self):
    def fire(self):
        if self.fire_count  == 100:
            b = bullet.Enemy_bullet((self.pos),self.type,self.fl)
            gfw.world.add(gfw.layer.b,b)
            #self.Action_Change()
            self.fire_count = 0
        elif self.fire_count > 0 and self.fire_count < 30:
            self.action = 'Attack'
        else: self.action = 'Idle'
        self.fire_count+=1
    def find_player(self):
        dist_sq = gobj.distance_sq(self.player.pos, self.pos)
        if dist_sq < Enemy.CHASE_DISTANCE_SQ:
            self.fire()
            dir = gobj.direction(self.player.pos, self.pos)
            if dir == True:
                self.fl = 'w'
            else:
                self.fl = 'h'

            if self.patrol_order >= 0:
                self.patrol_order = -1
                #self.action = 'Attack'
    def remove(self):
        obj_dead = Collsion(self.pos,self.type,self.fl)
        gfw.world.add(gfw.layer.obj_dead, obj_dead)
        gfw.world.remove(self)
    def get_bb(self):
        x,y = self.pos
        return x - 20, y - 22, x + 14, y + 14

    def Action_Change(self):
        if self.img_count == 0:
            self.action = 'Attack'
        else:
            self.action = 'Idle'
            self.img_count = 0
        self.img_count += gfw.delta_time
        print(self.img_count,'0')




