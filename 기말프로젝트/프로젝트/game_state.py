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
    gfw.world.init(['bg','plat','grass','obj_dead','en','player','b','p'])
    #gfw.world.add(gfw.layer.bg , bg)
    global grass, player ,platform, bg ,count ,en ,plat, obj_dead
    bg = Background('/background_grass.png')
    grass = Grass()
    gfw.world.add(gfw.layer.grass, grass)
    player = Player()
    gfw.world.add(gfw.layer.player,player)
    count = 0
    for (x,y) in STAGE_LIST[count]:
        plat =Platform(count,x,y)
        gfw.world.add(gfw.layer.plat,plat)

    for x in PLNAT_MONSTER_LIST[count]:
        en = enemy.Enemy((x,400),1)
        gfw.world.add(gfw.layer.en, en)

    for x in TREE_MONSTER_LIST[count]:
        en = enemy.Enemy((x,400),2)
        gfw.world.add(gfw.layer.en, en)

    for x in BOMB_MONSTER_LIST[count]:
        en = enemy.Enemy((x,800),3)
        gfw.world.add(gfw.layer.en, en)
    global music_bg, wav_attack, wav_bomb
    music_bg = load_music('../res/map.wav')
    wav_bomb = load_music('../res/bomb.wav')
    #wav_attack = load_music('../res/shoot.wav')
    music_bg.repeat_play()
    hide_cursor()
def updateMap():
    global count ,plat
    count += 1
    gfw.world.clear_at(gfw.layer.plat)
    for (x, y) in STAGE_LIST[count]:
        plat = Platform(count, x, y)
        gfw.world.add(gfw.layer.plat, plat)
    for x in PLNAT_MONSTER_LIST[count]:
        en = enemy.Enemy((x,400),1)
        gfw.world.add(gfw.layer.en, en)

    for x in TREE_MONSTER_LIST[count]:
        en = enemy.Enemy((x,400),2)
        gfw.world.add(gfw.layer.en, en)

    for x in BOMB_MONSTER_LIST[count]:
        en = enemy.Enemy((x,1000),3)
        gfw.world.add(gfw.layer.en, en)

def update():
    global player, count, en
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
        #      updateMap()
    player.handle_event(e)
    #Boy.handle_event(boy, e)

    # print(balls)
def exit():
    global music_bg
    del music_bg

if __name__ == '__main__':
    gfw.run_main()
