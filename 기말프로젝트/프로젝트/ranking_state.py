import gfw
from pico2d import *
import main_state
import game_state
import highscore

start_rad = 0
rad_bool = True
def enter():
    global ButtonSound , BackSound
    BackSound = load_music('../res/RankMusic.mp3')
    ButtonSound = load_wav('../res/ButtonSound.wav')

    global ranking_back ,target ,target_pos ,back ,gotomain
    highscore.add(game_state.score)
    gfw.world.add(gfw.layer.ui,highscore)
    back = gfw.load_image('../res/background.png')
    ranking_back = gfw.load_image('../res/rk.png')
    target = load_image('../res/target.png')
    target_pos = 0,0
    gotomain = load_image('../res/gotomain.png')
    BackSound.repeat_play()

def update():
    global start_rad, rad_bool
    if rad_bool == True:
        start_rad += 0.01
    elif rad_bool == False:
        start_rad -= 0.01

    if start_rad == 0.02:
        rad_bool = False
    if start_rad == -0.02:
        rad_bool = True
def draw():
    global ranking_back ,back , gotomain
    back.draw(get_canvas_width()//2,get_canvas_height()//2)
    ranking_back.draw(get_canvas_width()//2,get_canvas_height()//2)
    highscore.draw()

    gotomain.composite_draw(start_rad, 'm', 1000, 150)

    target.draw(*target_pos)

def handle_event(e):
    global  target_pos , gotomain ,ButtonSound
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(main_state)
    if e.type == SDL_MOUSEMOTION:
        target_pos = (e.x ,get_canvas_height() - e.y - 1)
        x, y = target_pos
        if x > 1000 - gotomain.w//2 and x< 1000+gotomain.w//2 and y >150 - gotomain.h//2 and y<150+gotomain.h//2:
            ButtonSound.play()

def exit():
    global ButtonSound, BackSound
    del ButtonSound
    del BackSound

def pause():
    pass


def resume():
    pass


