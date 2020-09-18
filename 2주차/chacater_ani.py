from pico2d import *

open_canvas()

image = load_image('../res/run_animation.png')
grass = load_image('../res/grass.png')

frame = 0

for x in range(0,800,2):
    clear_canvas()

    grass.draw(400, 30)
    image.clip_draw(frame * 100,0,100,100,x, 80)

    frame = (frame + 1) % 8

    update_canvas()
    get_events()
    delay(0.01)

delay(1)
close_canvas()