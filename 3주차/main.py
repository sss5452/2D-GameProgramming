from pico2d import *

import gobj

def handle_events():
    global running, dx, x, y  #전역으로 바꿔준다.
    ev= get_events()
    for e in ev:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
            elif e.key == SDLK_LEFT:
                boy.dx -= 1
            elif e.key == SDLK_RIGHT:
                boy.dx += 1
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                boy.dx += 1
            elif e.key == SDLK_RIGHT:
                boy.dx -= 1

open_canvas()

team = [Boy() for i in range(11)]

boy = team[0]
grass = Grass()

running = True
while running:
    clear_canvas()

    grass.draw()
    for b in team:
        b.draw()


    update_canvas()
    handle_events()

    for b in team:
        b.update()

    delay(0.01)


close_canvas()