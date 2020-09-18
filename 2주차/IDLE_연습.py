Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pico2d
Pico2d is prepared.
>>> pico2d.open_canvas()
>>> pico2d.close_canvas()
>>> import pico2d as p
>>> p.open_canvas()
p
>>> p.close_canvas()
>>> open_canvas()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    open_canvas()
NameError: name 'open_canvas' is not defined
>>> from random import randint
>>> randint(1,6)
2
>>> 
>>> 
>>> randint(1,6)
5
>>> randint(1,6)
1
>>> from random import randint as ri
>>> ri(1,6)
6
>>> from random import *
>>> uniform(1,2)
1.0964769400655285
>>> randrange(10,20)
12
>>> pico2d.open_canvas()
>>> p.close_canvas()
>>> from pico2d import *
>>> open_canvas()
>>> close_canvas()
>>> import ds
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    import ds
ModuleNotFoundError: No module named 'ds'
>>> import os
>>> os.getcwd()
'C:\\Users\\82109\\AppData\\Local\\Programs\\Python\\Python38'
>>> os.listdr()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    os.listdr()
AttributeError: module 'os' has no attribute 'listdr'
>>> os.listdir()
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python38.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll', 'vcruntime140_1.dll']
>>> open_canvas()
>>> image = load_image('C:\Users\82109\Desktop\2D-GameProgramming')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> image = load_image('C:\\Users\\82109\\Desktop\\2D-GameProgramming')
cannot load C:\Users\82109\Desktop\2D-GameProgramming
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    image = load_image('C:\\Users\\82109\\Desktop\\2D-GameProgramming')
  File "C:\Users\82109\AppData\Local\Programs\Python\Python38\lib\site-packages\pico2d\pico2d.py", line 340, in load_image
    raise IOError
OSError
>>> os.getcwd()
'C:\\Users\\82109\\AppData\\Local\\Programs\\Python\\Python38'
>>> os.chdir('C:\Users\82109\Desktop\2D-GameProgramming')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.chdir('C:/Users/82109/Desktop/2D-GameProgramming')
>>> os.listdir()
['.git', '.gitignore', '0908', '1주차과제', 'gird', 'README.md', '도열이형이준거.py']
>>> os.chdir('C:\Users\82109\Desktop\강상준 학교\2학년 2학기\2D 게임프로그래밍\res')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.chdir('C:/Users/82109/Desktop/강상준 학교/2학년 2학기/2D 게임프로그래밍/res')
>>> os.listdir()
['animation_sheet.png', 'character.png', 'grass.png', 'run_animation.png']
>>> os.listdir()
['animation_sheet.png', 'character.png', 'grass.png', 'run_animation.png', 'turtle_name.PNG']
>>> image=load_image('turtle_name.PNG')
>>> image=load_image('turtle_name.PNG')
>>> image=load_image('character.pgn')
cannot load character.pgn
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    image=load_image('character.pgn')
  File "C:\Users\82109\AppData\Local\Programs\Python\Python38\lib\site-packages\pico2d\pico2d.py", line 340, in load_image
    raise IOError
OSError
>>> image=load_image('character.png')
>>> image=load_image('turtle_name.PNG')
>>> img.draw_now(200,300)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    img.draw_now(200,300)
NameError: name 'img' is not defined
>>> image.draw_now(200,300)
>>> close_canvase
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    close_canvase
NameError: name 'close_canvase' is not defined
>>> close_canvas
<function close_canvas at 0x000002804A3464C0>
>>> open_canvas()
