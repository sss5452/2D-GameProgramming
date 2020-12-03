
import gfw
class Collsion:
    def __init__(self,pos, type, fl,bullet = None):
        self.pos  = pos
        self.type = type
        self.bullet = bullet
        self.fl = fl
        self.plant = gfw.image.load('../res/plant_dead.png')
        self.plant_bullet = gfw.image.load('../res/plant_bullet_dead.png')
        self.tree = gfw.image.load('../res/tree_dead.png')
        self.tree_bullet = gfw.image.load('../res/tree_bullet_dead.png')
        self.bomb_pig = gfw.image.load('../res/pig_dead.png')
        self.bomb = gfw.image.load('../res/Boooooom.png')
        self.fidx = 0
        self.time = 0
        self.max = 0
        self.max_count =0
    def update(self):
        self.time += gfw.delta_time
        frame = self.time * 15

        if self.bullet:
            if self.type == 3:
                self.max = 30
            else: self.max = 15
        else:
            self.max = 5
        self.fidx = int(frame) % self.max
        self.max_count+=1
        if self.max_count == self.max:
            gfw.world.remove(self)
    def draw(self):
        if self.type == 1:
            sx = self.fidx * 44
            if self.bullet:
                self.plant_bullet.composite_draw(sx, self.fl, *self.pos)
            else:
                self.plant.clip_composite_draw(2 + sx, 0, 44, 42, 0, self.fl, *self.pos, 44, 42)
        elif self.type == 2:
            sx = self.fidx * 64
            if self.bullet:
                self.tree_bullet.composite_draw(sx, self.fl, *self.pos)
            else:
                self.tree.clip_composite_draw(2 + sx, 0, 64, 32, 0, self.fl, *self.pos, 64, 32)
        elif self.type == 3:
            if self.bullet:
                sx = self.fidx * 52
                self.bomb.clip_composite_draw(sx, 0, 52, 56, 0, self.fl, *self.pos, 52, 56)
            else:
                sx = self.fidx * 34
                self.bomb_pig.clip_composite_draw(sx, 0, 34, 28, 0, self.fl, *self.pos, 52, 52)