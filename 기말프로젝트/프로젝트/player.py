import random
from pico2d import *
import gfw
import gobj
from platform import Platform
import enum
from setting import *
import platform

#프레임당 처리로 바꿔야한다.
#프레임당 처리로 바꾸고 콜리션(바운딩박스)을 프레임당 충돌처리로 바꾸자
#콜리션을 클래스로 만들고 여러개로 바꾸자
class State(enum.Enum):
    Idle = 0
    Move = 1
    Attack = 2
    Counter = 3
    Jump = 4
    Fall = 5
    Shield = 6

class Player():
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_a):      (-PLAYER_ACC,  0 ),
        (SDL_KEYDOWN, SDLK_d):      ( PLAYER_ACC,  0 ),
        (SDL_KEYDOWN, SDLK_DOWN):   ( 0, -1),
        (SDL_KEYDOWN, SDLK_UP):     ( 0,  1),
        (SDL_KEYUP, SDLK_a):        (  PLAYER_ACC,  0),
        (SDL_KEYUP, SDLK_d):        ( -PLAYER_ACC,  0),
        (SDL_KEYUP, SDLK_DOWN):     ( 0,  1),
        (SDL_KEYUP, SDLK_UP):       ( 0, -1),
    }
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    KEYDOWN_SHIFT = (SDL_KEYDOWN, SDLK_LSHIFT)
    KEYDOWN_SHIFTOFF = (SDL_KEYUP, SDLK_LSHIFT)
    # 애니메이션
    image = {}
    state = State.Idle
    #constructor
    def __init__(self, rand_pos=False):
        global  potal
        self.pos = (0,0)
        self.pos_x =50
        self.pos_y =200
        self.attack_pos =(0,0)
        self.time =0
        self.target = None
        self.action = 3
        self.delta = 0, 0
        self.fidx = random.randint(0, 7)
        self.speed = 0
        self.m = 1
        self.acc_x = 0
        self.acc_y = 0
        self.vel_x =0
        self.vel_y =0
        self.state = State.Idle
        self.fl = 'w'
        self.land = False
        self.land_y = 0
        self.landon =False
        self.shieldon = False
        self.shieldrad = 0
        self.stage = ST1_PLATFORM_LIST
        # set Animation
        Player.image[State.Idle.name] = gfw.image.load(gobj.res('/frog_idle.png'))
        Player.image[State.Move.name] = gfw.image.load(gobj.res('/frog_move.png'))
        Player.image[State.Jump.name] = gfw.image.load(gobj.res('/frog_jump.png'))
        Player.image[State.Fall.name] = gfw.image.load(gobj.res('/frog_fall.png'))
        Player.image[State.Attack.name] = gfw.image.load(gobj.res('/frog_attack.png'))
        Player.shield_image = gfw.image.load(gobj.res('/s225.png'))
        Player.target_image = gfw.image.load(gobj.res('/target.png'))
    #구현해야할것
    #character state 적용
    #bounding box
    def draw(self):
        sx = self.fidx * 32
        if self.state == State.Jump or self.state == State.Fall:
            sx = 0
        elif self.state == State.Attack:
            sx = 64
        self.image[self.state.name].clip_composite_draw(sx, 0,32,32,0,self.fl, *self.pos,32,32)
        if self.target is not None:
           self.target_image.clip_draw(0, 0, 54, 54, *self.target, 35, 35)
        if self.shieldon == True:
            self.shield_image.clip_composite_draw(0, 0,225,225,self.shieldrad,self.fl, *self.pos,50,50)
            self.shieldrad +=0.2
            if self.shieldrad == 20:
                self.shieldrad =0
    def update(self):
        dx, dy = self.delta
        self.acc_y=  -PLAYER_GRAVITY
        self.acc_x = dx
        for (x,y) in self.stage:
            if self.pos_y > y+25 and self.pos_y <y+32 and self.pos_x >x-48 and self.pos_x < x+48 and self.vel_y<0:
                self.land_y = y
                self.pos_y = self.land_y+36
                self.acc_y = 0
                self.landon = True
                if self.acc_x != 0:
                    self.state = State.Move
                else:
                    self.state = State.Idle

        if self.pos_y > 70 and self.landon == False:
            if self.vel_y < 0:
                self.state = State.Fall
            if self.pos_y < 75:
                self.state = State.Idle

        elif self.pos_y < 70:  # 땅
            self.pos_y = 80
            self.acc_y =0
            self.landon = True


        if self.acc_x < 0:
            self.fl = 'h'
            if self.pos_y < 81 and self.landon == True:              # 땅기준으로 바꿧는데 수정해야됨
                self.state = State.Move
        if self.acc_x > 0:
            self.fl = 'w'
            if self.pos_y < 81 and self.landon == True:
                self.state = State.Move

        self.acc_x += self.vel_x * PLAYER_FRICTION
        self.vel_x += self.acc_x
        self.vel_y += self.acc_y
        self.pos_x += self.vel_x +  self.acc_x * gfw.delta_time
        self.pos_y += self.vel_y + self.acc_y * gfw.delta_time
        self.pos = self.pos_x ,self.pos_y



    #새위치 = 이전위치 + 속도 * 시간(프레임타임)
    # 애니메이션 작동 이미지 8장
        self.time += gfw.delta_time
        frame = self.time *15
        self.fidx = int(frame)%5

    def landing(self):
        for (x,y) in ST1_PLATFORM_LIST:
            if self.pos_y > y+25 and self.pos_y <y+32 and self.pos_x >x-48 and self.pos_x < x+48 and self.vel_y<0:
                self.land_y = y
                print(x,y)
                return True
            else:
                return False
    #def shield(self):

    def jump(self):
        self.vel_y = 10.5
        self.landon = False
         #self.vel.x = 20
    def updateDelta(self, ddx, ddy):

        self.delta = ddx,ddy
    def updateAction(self, dx, ddx):
        self.action = \
            0 if dx < 0 else \
            1 if dx > 0 else \
            2 if ddx > 0 else 3


    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            if e.type == SDL_KEYDOWN:
                    self.state = State.Move
            if e.type == SDL_KEYUP:
                    self.state = State.Idle
            self.delta = gobj.point_add(self.delta, self.KEY_MAP[pair])
            #self.updateDelta(*Boy.KEY_MAP[pair])

        elif pair == Player.KEYDOWN_SPACE:
            self.jump()
            self.state = State.Jump
        elif pair == Player.KEYDOWN_SHIFT:
            #self.shield()
            self.state = State.Attack
            self.stage = ST2_PLATFORM_LIST
            self.shieldon = True
        elif e.type == SDL_MOUSEBUTTONDOWN:
            self.state = State.Attack
            self.attack_pos = (e.x, e.y)
            #self.shield()
        elif pair == Player.KEYDOWN_SHIFTOFF:
            self.shieldon = False
        if e.type == SDL_MOUSEMOTION:
            self.target = (e.x ,get_canvas_height() - e.y - 1)

        def get_bb(self):
            hw = 20
            hh = 40
            x, y = self.pos
            return x - hw, y - hh, x + hw, y + hh

