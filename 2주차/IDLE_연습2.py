Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pico2d import *
Pico2d is prepared.
>>> open_canvas()
>>> import os
>>> os.chdir('C:/Users/82109/PycharmProjects/res')
>>> os.listdir()
['animation_sheet.png', 'character.png', 'grass.png', 'run_animation.png', 'turtle_name.PNG']
>>> img = load_image('character.png')
>>> 
>>> img_draw_now(300,200)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    img_draw_now(300,200)
NameError: name 'img_draw_now' is not defined
>>> img.draw_now(300,200)
>>> img.draw_now(400,300)
>>> for x in range(100,701,100):
	img.draw_now(x.500)
	
SyntaxError: invalid syntax
>>> for x in range(100,701,100):
	img.draw_now(x,500)

	
>>>  for x in range(100,701,30):
	img.draw_now(x,100)
	
SyntaxError: unexpected indent
>>> 
>>> for x in range(100,701,30):
	img.draw_now(x,100)

	
>>> clear_canvas_now()
>>> for y in range(100,501,80):
	for x in range(100,701,35):
		image.draw_now(x,y)

		
Traceback (most recent call last):
  File "<pyshell#21>", line 3, in <module>
    image.draw_now(x,y)
NameError: name 'image' is not defined
>>> for y in range(100,501,80):
	for x in range(100,701,35):
		imag.draw_now(x,y)

		
Traceback (most recent call last):
  File "<pyshell#23>", line 3, in <module>
    imag.draw_now(x,y)
NameError: name 'imag' is not defined
>>> for y in range(100,501,80):
	for x in range(100,701,35):
		img.draw_now(x,y)

		
>>> for y in range(100,501,60):
	for x in range(100,701,25):
		img.draw_now(x,y)

		
>>> import os
>>> os.chdir(C:/Users/82109/PycharmProjects/res)
SyntaxError: invalid syntax
>>> os.chdir('C:/Users/82109/PycharmProjects/res')
>>> os.listdir()
['animation_sheet.png', 'character.png', 'grass.png', 'run_animation.png', 'turtle_name.PNG']
>>> load_image('character.png')
<pico2d.pico2d.Image object at 0x000001EB5EC88FA0>
>>> image.draw_now(300,200)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    image.draw_now(300,200)
NameError: name 'image' is not defined
>>> load_image('grass.png')
<pico2d.pico2d.Image object at 0x000001EB5EC88E50>
>>> grass.draw_now(400,90)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    grass.draw_now(400,90)
NameError: name 'grass' is not defined
>>> grass.draw_now(400,90)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    grass.draw_now(400,90)
NameError: name 'grass' is not defined
>>> img.draw_now(400,30)
>>> close_canvas
<function close_canvas at 0x000001EB5F2164C0>
>>> close_canvas()
>>> grass = load_image('grass.png')
cannot load grass.png
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    grass = load_image('grass.png')
  File "C:\Users\82109\AppData\Local\Programs\Python\Python38\lib\site-packages\pico2d\pico2d.py", line 340, in load_image
    raise IOError
OSError
>>> os.listdir
<built-in function listdir>
>>> os.listdir()
['animation_sheet.png', 'character.png', 'grass.png', 'run_animation.png', 'turtle_name.PNG']
>>> grass = load_image('grass.png')
cannot load grass.png
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    grass = load_image('grass.png')
  File "C:\Users\82109\AppData\Local\Programs\Python\Python38\lib\site-packages\pico2d\pico2d.py", line 340, in load_image
    raise IOError
OSError
>>> gr = load_image('grass.png')
cannot load grass.png
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    gr = load_image('grass.png')
  File "C:\Users\82109\AppData\Local\Programs\Python\Python38\lib\site-packages\pico2d\pico2d.py", line 340, in load_image
    raise IOError
OSError
>>> open_canvas()
>>> gr = load_image('grass.png')
>>> gr.draw_now(400,90_
	    
SyntaxError: invalid decimal literal
>>> gr.draw_now(400,90)
>>> grass.clip_draw_now(400,190)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    grass.clip_draw_now(400,190)
NameError: name 'grass' is not defined
>>> grass.clip_draw(400,190,0,0,150,50)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    grass.clip_draw(400,190,0,0,150,50)
NameError: name 'grass' is not defined
>>> gr.clip_draw(400,190,0,0,150,50)
>>> update_canvas()
>>> 