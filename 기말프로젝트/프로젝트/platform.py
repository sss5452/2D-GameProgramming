import gfw
from pico2d import *
from setting import *
import random
import game_state
RES_DIR = '../res'

class Platform:
    def __init__(self):
        self.image = load_image(RES_DIR + '/wall.png')
    def draw(self):
        #self.image.draw(*PLATFORM_LISTX[0])
        #self.image.draw(*PLATFORM_LISTX[1])
        for (x,y) in PLATFORM_LIST:
            self.image.draw(x,y)
