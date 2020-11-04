import gfw
from pico2d import *
from gobj import *
from player import player
import pygame as pg
from platform import Platform
import background

pg.init()

def enter():
    global grass, boy , p
    grass = Grass()
    boy = player()
    p = Platform()

def update():
    boy.update()
    boy.landing()

def draw():
    grass.draw()
    p.draw()
    boy.draw()

def handle_event(e):
    global boy
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    boy.handle_event(e)
    #Boy.handle_event(boy, e)

    # print(balls)
def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
