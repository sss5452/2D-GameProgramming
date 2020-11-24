import gfw
import random
from pico2d import *
import gobj
from player import Player
from platform import Platform, Grass
from background import Background
from collison_image import Collsion
import enemy
from setting import *


def enter():
    gfw.world.init(['bg','plat','obj_dead','player','grass','en','b','p'])
    #gfw.world.add(gfw.layer.bg , bg)
    global grass, player ,platform, bg ,count ,en ,plat, obj_dead
    bg = Background('/background.png')
    grass = Grass()
    gfw.world.add(gfw.layer.grass, grass)

    player = Player()
    gfw.world.add(gfw.layer.player,player)
    count = player.st
    for (x,y) in STAGE_LIST[count]:
        plat =Platform(count,x,y)
        gfw.world.add(gfw.layer.plat,plat)

    for x in ST1_MONSTER_PLANT:
        en = enemy.Enemy((x,400),3)
        gfw.world.add(gfw.layer.en, en)

    for x in ST1_MONSTER_TREE:
        en = enemy.Enemy((x,400),2)
        gfw.world.add(gfw.layer.en, en)
    # for (x, y) in ST2_PLATFORM_LIST:
    #     wall.draw(x, y)
    #gfw.world.add(gfw.layer.p,p)
    hide_cursor()
def updateMap():
    global count ,plat
    count += 1
    print(player.st)
    gfw.world.clear_at(gfw.layer.plat)
    for (x, y) in STAGE_LIST[count]:
        plat = Platform(count, x, y)
        gfw.world.add(gfw.layer.plat, plat)

def update():
    global player, count
    gfw.world.update()
def draw():
    bg.draw()
    gfw.world.draw()
    #gobj.draw_collision_box()

def handle_event(e):
    global player, stage
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        # if e.key == SDLK_LSHIFT:
        #     updateMap()
    player.handle_event(e)
    #Boy.handle_event(boy, e)

    # print(balls)
def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
