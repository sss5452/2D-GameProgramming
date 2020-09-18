from pico2d import *

open_canvas()

image = load_image('../res/character.png')
grass = load_image('../res/grass.png')

for x in range(0,800,2):
    print("Clearing Canvas")
    clear_canvas()

    print("Drawing Grass")
    grass.draw(400, 30)

    print("Drawing Character")
    image.draw(x, 80)
    update_canvas()
    delay(0.01)

delay(1)
close_canvas()