import gfw
from pico2d import *
from player import Player
from platform import Platform, Grass
from background import Background
import ranking_state
import enemy
from setting import *
import highscore
import random

score = 0

def endGame():
    global music_bg, gameover, score
    gameover = True
    music_bg.stop()
    return True

def sound_wav(type):
    global wav_attack ,wav_bomb, wav_shield_sound, wav_bullet, wav_hit, wav_die, hit
    if type == 1:
        wav_attack.play()
    elif type == 2:
        wav_bomb.play()
    elif type == 3:
        wav_bullet.play()
    elif type == 4:
        hit_c = random.randint(0,2)
        hit[hit_c].play()
    elif type == 5:
        wav_shield_sound.play()
    elif type == 6:
        wav_die.play()

def enter():
    #--------------------------------------------------------------------------#
    gfw.world.init(['bg', 'plat', 'grass', 'obj_dead', 'en', 'player', 'b', 'p', 'ui']) #월드 init
    global grass, player, platform, bg, count, en, plat, obj_dead
    bg = Background('/background_grass.png')
    grass = Grass()
    gfw.world.add(gfw.layer.grass, grass)
    player = Player()
    gfw.world.add(gfw.layer.player, player)
    count = 0
    for (x, y) in STAGE_LIST[count]:
        plat = Platform(count, x, y)
        gfw.world.add(gfw.layer.plat, plat)

    for x in PLNAT_MONSTER_LIST[count]:
        en = enemy.Enemy((x, 400), 1)
        gfw.world.add(gfw.layer.en, en)

    for x in TREE_MONSTER_LIST[count]:
        en = enemy.Enemy((x, 400), 2)
        gfw.world.add(gfw.layer.en, en)

    for x in BOMB_MONSTER_LIST[count]:
        en = enemy.Enemy((x, 800), 3)
        gfw.world.add(gfw.layer.en, en)
    #--------------------------------------------------------------------------#
    global gameover_img,gameover
    gameover = False
    gameover_img = gfw.image.load('../res/gameover.png')
    #--------------------------------------------------------------------------#
    global music_bg,wav_attack ,wav_bomb, wav_shield_sound, wav_bullet, wav_hit1, wav_hit2, wav_hit3 ,wav_die, hit
    wav_attack = load_wav('../res/shoot.ogg')
    wav_bomb = load_wav('../res/bomb.wav')
    wav_bullet = load_wav('../res/bullet.ogg')
    wav_hit1 = load_wav('../res/pain1.wav')
    wav_hit2 = load_wav('../res/pain2.wav')
    wav_hit3 = load_wav('../res/pain3.wav')
    hit = [wav_hit1,wav_hit2,wav_hit3]
    wav_die = load_wav('../res/die.wav')
    wav_shield_sound = load_wav('../res/shield_sound.wav')
    music_bg = load_music('../res/map.wav')
    #--------------------------------------------------------------------------#
    global font ,score , score_pos
    font = gfw.font.load('../res/Pixel.ttf',38)
    score = 0
    score_pos = 30 , get_canvas_height() - 30
    #--------------------------------------------------------------------------#
    highscore.load()
    music_bg.repeat_play()

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

def updateScore():
    global score
    score +=150

def update():
    global gameover
    if gameover:
        return
    gfw.world.update()
def draw():
    global shield_bar , shield_gauge, gameover_img ,font, score ,score_pos
    bg.draw()
    gfw.world.draw()
    font.draw(*score_pos, 'SCORE: %.0F' % score, (255, 255, 255))
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
    global music_bg, wav_attack,wav_bomb, wav_shield_sound, wav_bullet,wav_hit1, wav_hit2, wav_hit3, wav_die
    del wav_attack
    del wav_bomb
    del wav_shield_sound
    del wav_bullet
    del wav_hit1
    del wav_hit2
    del wav_hit3
    del wav_die

def pause():
    pass


def resume():
    pass


