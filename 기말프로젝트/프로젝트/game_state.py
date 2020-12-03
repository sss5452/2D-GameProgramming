import gfw
import random
from pico2d import *
import gobj
from player import Player
from platform import Platform, Grass
from background import Background
import ranking_state
from collison_image import Collsion
import enemy
from setting import *

def endGame():
    global music_bg, gameover
    gameover = True
    music_bg.stop()
    return True

def sound_wav(type):
    global wav_attack ,wav_bomb, wav_shield_sound, wav_bullet, wav_hit
    if type == 1:
        wav_attack.play()
    elif type == 2:
        wav_bomb.play()
    elif type == 3:
        wav_bullet.play()
    elif type == 4:
        wav_hit.play()
    elif type == 5:
        wav_shield_sound.play()
def enter():
    global gameover_img,gameover
    gameover = False
    gameover_img = gfw.image.load('../res/gameover.png')
    global music_bg,wav_attack ,wav_bomb, wav_shield_sound, wav_bullet, wav_hit
    wav_attack = load_wav('../res/shoot.ogg')
    wav_bomb = load_wav('../res/bomb.wav')
    wav_bullet = load_wav('../res/bullet.ogg')
    wav_hit = load_wav('../res/frog_hit.ogg')
    wav_shield_sound = load_wav('../res/shield_sound.wav')
    music_bg = load_music('../res/map.wav')

    global font ,score
    font = gfw.font.load('../res/Pixel.ttf',38)
    score = 0
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
    global gameover
    if gameover:
        return
    global score
    score += gfw.delta_time
    gfw.world.update()
def draw():
    global shield_bar , shield_gauge,gameover_img
    bg.draw()
    gfw.world.draw()
    score_pos = 30 , get_canvas_height() - 30
    font.draw(*score_pos, 'TIME: %.1F' % score, (255, 255, 255))
    if gameover:
        center = get_canvas_width() // 2, get_canvas_height() * 2 // 3
        gameover_img.draw(*center)
    #gobj.draw_collision_box()

def handle_event(e):
    global player, stage
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        if e.key == SDLK_RETURN and gameover:
            gfw.push(ranking_state)
    player.handle_event(e)
    #Boy.handle_event(boy, e)

    # print(balls)
def exit():
    global music_bg, wav_attack,wav_bomb, wav_shield_sound, wav_bullet, wav_hit ,font
    del music_bg
    del wav_attack
    del wav_bomb
    del wav_shield_sound
    del wav_bullet
    del wav_hit
    del font

def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    gfw.run_main()
