import gfw
from pico2d import *
import game_state
import ranking_state

fidx = 0
player_x = 0
start_rad = 0
rad_bool = True
def enter():
    global ButtonSound , BackSound
    BackSound = load_music('../res/MainMusic.wav')
    ButtonSound = load_wav('../res/ButtonSound.wav')
    hide_cursor()
    global image, wall , player ,fidx , player_x, start , target , rank
    image = load_image('../res/title_counter.png')
    wall = load_image('../res/wallground.png')
    player = load_image('../res/title_player.png')
    start = load_image('../res/GAMESTART.png')
    rank = load_image('../res/RANKING.png')
    target = load_image('../res/target.png')

    BackSound.repeat_play()
def update():
    global fidx , player_x , start_rad , rad_bool
    fidx += 1
    player_x +=5
    if rad_bool == True:
        start_rad += 0.01
    elif rad_bool == False:
        start_rad -= 0.01

    if start_rad == 0.02:
        rad_bool = False
    if start_rad == -0.02:
        rad_bool = True

    if fidx == 6:
        fidx = 0

def draw():
    global sx ,target_pos
    image.draw(600, 400)
    wall.draw(600,20)
    #start.draw(612,400)
    start.composite_draw(start_rad,'m',612,400)
    rank.composite_draw(start_rad, 'm',612,330)
    sx = fidx * 32
    player.clip_draw(sx,0,32,32,300+player_x,64)
    target.draw(*target_pos)
def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(game_state)

    global target_pos ,ButtonSound
    if e.type == SDL_MOUSEMOTION:
        target_pos = (e.x ,get_canvas_height() - e.y - 1)
        x, y = target_pos
        if x > 500 and x < 720 and y >390 and y < 410:
            ButtonSound.play()
        elif x > 500 and x < 720 and y >320 and y < 340:
            ButtonSound.play()
    if e.type == SDL_MOUSEBUTTONDOWN:
        x, y = target_pos
        if x > 500 and x < 720 and y >390 and y < 410:
            gfw.push(game_state)
        elif x > 500 and x < 720 and y >320 and y < 340:
            gfw.push(ranking_state)
def exit():
    global image, wall , player ,fidx
    del image, wall , player ,fidx
    global ButtonSound,BackSound
    del ButtonSound
    del BackSound
def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
