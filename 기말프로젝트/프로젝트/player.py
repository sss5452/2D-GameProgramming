import random
from pico2d import *
import gfw_image
from gfw import *
from gobj import *
from platform import Platform
import enum
from setting import *
import pygame as pg
vec = pg.math.Vector2

pg.init()
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

class player(pg.sprite.Sprite):
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
        self.pos = vec(200,200)
        self.attack_pos =vec(0,0)
        self.target = None
        self.action = 3
        self.delta = 0, 0
        self.fidx = random.randint(0, 7)
        self.speed = 0
        self.m = 1
        self.acc = vec(0,0)
        self.vel = vec(0,0)
        self.state = State.Idle
        self.fl = 'w'
        self.land = False
        self.land_y = 0
        self.landon =False
        self.shieldon = False
        self.shieldrad = 0
        # set Animation
        player.image[State.Idle.name] = gfw_image.load(RES_DIR + '/frog_idle.png')
        player.image[State.Move.name] = gfw_image.load(RES_DIR + '/frog_move.png')
        player.image[State.Jump.name] = gfw_image.load(RES_DIR + '/frog_jump.png')
        player.image[State.Fall.name] = gfw_image.load(RES_DIR + '/frog_fall.png')
        player.image[State.Attack.name] = gfw_image.load(RES_DIR + '/frog_attack.png')
        player.shield_image = gfw_image.load(RES_DIR + '/s225.png')
        player.target_image = gfw_image.load(RES_DIR + '/target.png')
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
           self.target_image.clip_draw(0, 0, 54, 54, *self.target, 50, 50)
        if self.shieldon == True:
            self.shield_image.clip_composite_draw(0, 0,225,225,self.shieldrad,self.fl, *self.pos,50,50)
            self.shieldrad +=0.2
            if self.shieldrad == 20:
                self.shieldrad =0
    def update(self):
        dx, dy = self.delta
        self.acc = vec(0, -PLAYER_GRAVITY)
        self.acc.x = dx

        for (x,y) in PLATFORM_LIST:
            if self.pos.y > y+25 and self.pos.y <y+32 and self.pos.x >x-48 and self.pos.x < x+48 and self.vel.y<0:
                self.land_y = y
                self.pos.y = self.land_y+36
                self.acc.y = 0
                self.landon = True
                if self.acc.x != 0:
                    self.state = State.Move
                else:
                    self.state = State.Idle

        if self.pos.y > 70 and self.landon == False:
            if self.vel.y < 0:
                self.state = State.Fall
            if self.pos.y < 75:
                self.state = State.Idle

        elif self.pos.y < 70:  # 땅
            self.pos.y = 80
            self.acc.y =0
            self.landon = True


        if self.acc.x < 0:
            self.fl = 'h'
            if self.pos.y < 81 and self.landon == True:              # 땅기준으로 바꿧는데 수정해야됨
                self.state = State.Move
        if self.acc.x > 0:
            self.fl = 'w'
            if self.pos.y < 81 and self.landon == True:
                self.state = State.Move

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel +  self.acc * delta_time
    #새위치 = 이전위치 + 속도 * 시간(프레임타임)
    # 애니메이션 작동 이미지 8장
        self.fidx = (self.fidx + 1) % 8

    def landing(self):
        for (x,y) in PLATFORM_LIST:
            if self.pos.y > y+25 and self.pos.y <y+32 and self.pos.x >x-48 and self.pos.x < x+48 and self.vel.y<0:
                self.land_y = y
                print(x,y)
                return True
            else:
                return False
    #def shield(self):

    def ballDelta(self):
        dxs = [ -3, 3, -1, 1 ]
        mag = dxs[self.action]
        dx,dy = self.delta
        return rand(mag+dx), rand(2+dy)
    def jump(self):
        self.vel.y = 10.5
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
        if pair in player.KEY_MAP:
            if e.type == SDL_KEYDOWN:
                    self.state = State.Move
            if e.type == SDL_KEYUP:
                    self.state = State.Idle
            self.delta = point_add(self.delta, self.KEY_MAP[pair])
            #self.updateDelta(*Boy.KEY_MAP[pair])

        elif pair == player.KEYDOWN_SPACE:
            self.jump()
            self.state = State.Jump
        elif pair == player.KEYDOWN_SHIFT:
            #self.shield()
            self.state = State.Attack
            self.shieldon = True
        elif e.type == SDL_MOUSEBUTTONDOWN:
            self.state = State.Attack
            self.attack_pos = (e.x, e.y)
            #self.shield()
        elif pair == player.KEYDOWN_SHIFTOFF:
            self.shieldon = False
        if e.type == SDL_MOUSEMOTION:
            self.target = (e.x ,get_canvas_height() - e.y - 1)