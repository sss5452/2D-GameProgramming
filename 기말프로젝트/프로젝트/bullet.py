from pico2d import *
import gfw
import gobj
import player
MOVE_PPS = 200

class Plant_bullet:
    SIZE = 60
    def __init__(self,pos,type):
        self.pos = pos
        self.image = gfw.image.load('../res/plant_bullet.png')
        layer = list(gfw.world.objects_at(gfw.layer.player))
        self.type = type
        self.target = layer[0]
        x, y = self.target.pos
        a, b = self.pos
        self.delta = x-a, y-b
    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx * gfw.delta_time
        y += dy * gfw.delta_time
        self.pos = x,y

        if gobj.collides_box(self, self.target):#플레이어 or 쉴드 충돌
            if player.Player.checkShiled(self.target):  #쉴드 충돌
                gfw.world.remove(self)
                self.blocked()
            else:                                       #플레이어 충돌
                gfw.world.remove(self)
        # if not self.in_boundary():
        #     gfw.world.remove(self)
        #self.pos = x,y
    def draw(self):
        diameter = 2 * 2
        self.image.draw(*self.pos)
    def get_bb(self):
        x,y = self.pos
        return x - 4, y - 4, x + 4, y + 4
    def blocked(self):
        return True