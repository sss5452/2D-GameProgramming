# version 2020-0927
import time
from pico2d import *
import random
import gfw.world
import gfw.image
import gfw.font

running = True
runningFinish = 0
isClearCanvas = False
stack = None
frame_interval = 0.01
delta_time = 0

def quit():
    global runningFinish
    runningFinish = -1

def run(start_state):
    global running,runningFinish,isClearCanvas, stack
    running = True
    runningFinish = 0
    stack = [start_state]

    w,h = 1200,800
    if hasattr(start_state, 'canvas_width'): w = start_state.canvas_width
    if hasattr(start_state, 'canvas_height'): h = start_state.canvas_height

    open_canvas(w=w, h=h)

    start_state.enter()

    global delta_time
    last_time = time.time()
    while running:
        runningFinish = 0

        # inter-frame (delta) time
        now = time.time()
        delta_time = now - last_time
        last_time = now

        # event handling
        evts = get_events()
        for e in evts:
            if stack[-1]:
                stack[-1].handle_event(e)

        # game logic
        if stack[-1]:
            stack[-1].update()

        # game rendering
        isClearCanvas = False
        clear_canvas()
        isClearCanvas = True
        if stack[-1]:
            stack[-1].draw()
        update_canvas()

        delay(frame_interval)

        if runningFinish == -1:
            running = False
        runningFinish = 1

    while (len(stack) > 0):
        if stack[-1]:
            stack[-1].exit()
        stack.pop()

    if isClearCanvas:
        close_canvas()

def change(state):
    global stack
    if (len(stack) > 0):
        stack[-1].exit()
        stack.pop()
        #stack.pop().exit()
    stack.append(state)
    state.enter()
    print(len(stack))
def push(state):
    global stack
    if (len(stack) > 0):
        print(len(stack))
        if stack[-1]:
            stack[-1].pause()
    stack.append(state)
    print("append")
    state.enter()
    print("enter")

def pop():
    global stack
    size = len(stack)
    if size == 1:
        quit()
    elif size > 1:
        # execute the current state's exit function
        if stack[-1]:
            stack[-1].exit()
        # remove the current state
        stack.pop()

        # execute resume function of the previous state
        if stack[-1]:
            stack[-1].resume()

def run_main():
    import sys
    main_module = sys.modules['__main__']
    run(main_module)
