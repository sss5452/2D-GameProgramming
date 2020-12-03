import gfw
from pico2d import *
import title_state

fidx = 0
player_x = 0
start_rad = 0
rad_bool = True


def enter():
    pass
def update():
    pass
def draw():
    pass
def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.push(title_state)


def exit():
    pass
def pause():
    pass


def resume():
    pass


if __name__ == '__main__':
    gfw.run_main()
