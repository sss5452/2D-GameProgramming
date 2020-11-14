import gfw
from pico2d import *
from gobj import *
from player import Player
from platform import Platform
from background import Background


def enter():
    gfw.world.init(['bg','p','grass','boy'])
    #gfw.world.add(gfw.layer.bg , bg)
    global grass, boy , p ,bg
    bg = Background('/background.png')
    grass = Grass()
    gfw.world.add(gfw.layer.grass, grass)
    boy = Player()
    gfw.world.add(gfw.layer.boy,boy)
    p = Platform()
    #gfw.world.add(gfw.layer.p,p)
    hide_cursor()
def update():
    gfw.world.update()
def draw():
    bg.draw()
    p.draw()
    gfw.world.draw()


def handle_event(e):
    global boy
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    boy.handle_event(e)
    #Boy.handle_event(boy, e)

    # print(balls)
def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
