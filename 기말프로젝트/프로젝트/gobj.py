import random
from pico2d import *
import gfw
import setting

RES_DIR = '../res'


def res(file):
	return RES_DIR + file

def point_add(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    return x1+x2, y1+y2

def rand(val):
    return val * random.uniform(0.9, 1.1)

class Grass:
    def __init__(self):
        self.image = load_image(RES_DIR + '/wallground.png')
        #self.wall = load_image(RES_DIR + '/wall.png')
    def draw(self):
        self.image.draw(600,20)
        #self.wall.draw(setting.PLATFORM_LIST2[0],setting.PLATFORM_LIST2[1])
    def update(self):
        pass

def collides_box(a, b):
	(la, ba, ra, ta) = a.get_bb()
	(lb, bb, rb, tb) = b.get_bb()
	if la > rb: return False
	if ra < lb: return False
	if ba > tb: return False
	if ta < bb: return False

	return True
def draw_collision_box():
	for obj in gfw.world.all_objects():
		if hasattr(obj, 'get_bb'):
			draw_rectangle(*obj.get_bb())