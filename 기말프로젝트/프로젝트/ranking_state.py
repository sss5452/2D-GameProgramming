import gfw
from pico2d import *
import main_state
import game_state
import highscore

start_rad = 0
rad_bool = True
def enter():
    print("RankingState Enter")
    global ButtonSound , BackSound
    BackSound = load_music('res/RankMusic.mp3')
    ButtonSound = load_wav('res/ButtonSound.wav')

    global ranking_back ,target ,target_pos ,back ,gotomain ,quit_game

    if main_state.CheckGame: highscore.add(game_state.score)

    #gfw.world.add(gfw.layer.ui,highscore)
    back = gfw.load_image('res/background.png')
    ranking_back = gfw.load_image('res/rk.png')
    target = load_image('res/target.png')
    target_pos = 0,0
    gotomain = load_image('res/gotomain.png')
    quit_game = load_image('res/quit.png')
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
    global ranking_back ,back , gotomain ,quit_game
    back.draw(get_canvas_width()//2,get_canvas_height()//2)
    ranking_back.draw(get_canvas_width()//2,get_canvas_height()//2)
    highscore.draw()

    gotomain.composite_draw(start_rad, 'm', 1000, 150)
    quit_game.composite_draw(start_rad, 'm', 1000, 110)
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
        elif x > 1000 - quit_game.w//2 and x< 1000+quit_game.w//2 and y >110 - quit_game.h//2 and y<110+quit_game.h//2:
            ButtonSound.play()
    if e.type == SDL_MOUSEBUTTONDOWN:
        x, y = target_pos
        if x > 1000 - gotomain.w//2 and x< 1000+gotomain.w//2 and y >150 - gotomain.h//2 and y<150+gotomain.h//2:
            if game_state.Soundon:
                game_state.deadmusicstop()
            gfw.change(main_state)
        elif x > 1000 - quit_game.w//2 and x< 1000+quit_game.w//2 and y >110 - quit_game.h//2 and y<110+quit_game.h//2:
            gfw.quit()
def exit():
    global ranking_back ,target ,back ,gotomain ,quit_game
    del ranking_back ,target ,back ,gotomain ,quit_game

    global ButtonSound, BackSound
    del ButtonSound
    del BackSound
    print('RankingState Exit')
def pause():
    pass


def resume():
    pass


