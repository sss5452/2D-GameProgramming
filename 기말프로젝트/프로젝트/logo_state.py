import gfw
import main_state

logo_time =0
image =None
def enter():
    global image, elapsed
    image = gfw.load_image('res/logo.png')
    elapsed = 0
def update():
    global elapsed
    elapsed += gfw.delta_time
    print(elapsed)
    if elapsed> 2.2:
        gfw.change(main_state)
def draw():
    global image
    image.draw(gfw.get_canvas_width()//2,gfw.get_canvas_height()//2)
def exit():
    global image
    del image
def handle_event(e):
    pass
def pause():
    pass
def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()
