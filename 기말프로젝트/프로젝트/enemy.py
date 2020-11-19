from pico2d import *
import gfw
import random
import gobj
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import player

class Plant:
    ACTIONS = ['Attack', 'Dead', 'Idle']
    CHASE_DISTANCE_SQ = 250 ** 2
    def __init__(self,pos):
        self.pos = pos
        self.image = gfw.image.load('../res/plant_idle.png')
        self.fl = 'h'
        self.fidx = random.randint(0, 7)
        self.time = 0
        self.action = 'Idle'
        self.patrol_order = -1
        #self.build_behavior_tree()
        layer = list(gfw.world.objects_at(gfw.layer.player))
        self.player = layer[0]
    def update(self):
        global layer
        self.time += gfw.delta_time
        frame = self.time *15
        self.fidx = int(frame)%11
        self.find_player()
    def draw(self):
        sx = self.fidx * 44
        self.image.clip_composite_draw(2+sx, 0, 44, 44, 0, self.fl, *self.pos, 44, 44)
    def find_player(self):
        dist_sq = gobj.distance_sq(self.player.pos,self.pos)
        if dist_sq < Plant.CHASE_DISTANCE_SQ:
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