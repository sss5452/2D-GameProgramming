import gfw
from pico2d import *
import game_state

fidx = 0
player_x = 0
start_rad = 0
rad_bool = True
def enter():
    global image, wall , player ,fidx , player_x, start
    image = load_image('../res/title_counter.png')
    wall = load_image('../res/wallground.png')
    player = load_image('../res/title_player.png')
    start = load_image('../res/press_start.png')
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
    delay(0.03)
def draw():
    global sx
    image.draw(600, 400)
    wall.draw(600,20)
    #start.draw(612,400)
    start.composite_draw(start_rad,'m',612,400)
    sx = fidx * 32
    player.clip_draw(sx,0,32,32,300+player_x,64)
def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(game_state)
def exit():
    global image, wall , player ,fidx
    del image, wall , player ,fidx

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
