import gfw
import random
from pico2d import *
import gobj
from player import Player
import platform
from background import Background
import enemy


def enter():
    gfw.world.init(['bg','platform','grass','player','en'])
    #gfw.world.add(gfw.layer.bg , bg)
    global grass, player ,platform,bg ,count ,en
    bg = Background('/background.png')
    grass = gobj.Grass()
    gfw.world.add(gfw.layer.grass, grass)

    player = Player()
    gfw.world.add(gfw.layer.player,player)
    count = player.st

    platform.init(count)
    gfw.world.add(gfw.layer.platform,platform)

    # en = enemy.Plant((500,250))
    # gfw.world.add(gfw.layer.en,en)


    #gfw.world.add(gfw.layer.p,p)
    hide_cursor()
def update():
    global  player
    platform.stage = player.st
    gfw.world.update()
    platform.update()
def draw():
    bg.draw()
    gfw.world.draw()
    gobj.draw_collision_box()

def handle_event(e):
    global player, stage
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
    player.handle_event(e)
    #Boy.handle_event(boy, e)

    # print(balls)
def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
