# goo.su/

import json
from pygame import *
from random import randint
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        # подгружаем переменные
        self.size_x = size_x
        self.size_y = size_y
        self.image = transform.scale(image.load(player_image), (self.size_x, self.size_y))
        self.speed = player_speed
        # получаем хитбокс
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        # вывод на экран
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def before_update(self):
        global p1_last
        # print(p1_last)
        p1_last = 0
        # print(p1_last)
    def update(self, hb_center, hb_h_l, hb_h_r):
        global p1_last
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 10:
            self.rect.x -= self.speed
            hb_center.rect.x -= self.speed
            hb_h_r.rect.x -= self.speed
            hb_h_l.rect.x -= self.speed
            p1_last = -(self.speed)

        if keys[K_d] and self.rect.x < w_width - 110:
            self.rect.x += self.speed
            hb_center.rect.x += self.speed
            hb_h_l.rect.x += self.speed
            hb_h_r.rect.x += self.speed
            p1_last = self.speed
class Player2(GameSprite):
    def before_update(self):
        global p2_last
        # print(p1_last)
        p2_last = 0
        # print(p1_last)
    def update(self, hb_center, hb_h_l, hb_h_r):
        global p2_last
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
            hb_center.rect.x -= self.speed
            hb_h_l.rect.x -= self.speed
            hb_h_r.rect.x -= self.speed
            p2_last = -(self.speed)
        if keys[K_RIGHT] and self.rect.x < w_width - 110:
            self.rect.x += self.speed
            hb_center.rect.x += self.speed
            hb_h_l.rect.x += self.speed
            hb_h_r.rect.x += self.speed
            p2_last = self.speed
class HitboxCenterP1(GameSprite):
    def ball_collide(self, ball):
        global p1_last
        global direction
        global rotation
        direction = 'up'
        ball.rect.y -= 2
        rotation += p1_last * 3
class HitboxCenterP2(GameSprite):
    def ball_collide(self, ball):
        global p2_last
        global direction
        global rotation
        direction = 'down'
        ball.rect.y += 2
        rotation += p2_last * 3
class LHitboxHardP1(GameSprite):
    def ball_collide(self, ball):
        global p1_last
        global direction
        global rotation
        direction = 'up'
        ball.rect.y -= 2
        rotation -= player.speed * 6
class RHitboxHardP1(GameSprite):
    def ball_collide(self, ball):
        global p1_last
        global direction
        global rotation
        direction = 'up'
        ball.rect.y -= 2
        rotation += player.speed * 6
class LHitboxHardP2(GameSprite):
    def ball_collide(self, ball):
        global p2_last
        global direction
        global rotation
        direction = 'down'
        ball.rect.y += 2
        rotation -= player2.speed * 6
class RHitboxHardP2(GameSprite):
    def ball_collide(self, ball):
        global p2_last
        global direction
        global rotation
        direction = 'down'
        ball.rect.y += 2
        rotation += player2.speed * 6
class RWallHitbox(GameSprite):
    def ball_collide(self, ball):
        global rotation
        rotation = -(rotation)
        ball.rect.x += 1
        print(rotation)
class LWallHitbox(GameSprite):
    def ball_collide(self, ball):
        global rotation
        rotation = -(rotation)
        ball.rect.x -= 1
        print(rotation)
class P1WallHitbox(GameSprite):
    def ball_collide(self, ball):
        global rotation
        global direction
        direction = 'up'
        rotation = 0
        ball.restart(w_width/2, w_height/1.5)
class P2WallHitbox(GameSprite):
    def ball_collide(self, ball):
        global rotation
        global direction
        direction = 'down'
        rotation = 0
        ball.restart(w_width/2, w_height/3)
        
class Ball(GameSprite):
    def update(self):
        global game_speed
        global ball_x
        global ball_y
        global rotation
        global direction
        global cooldown
        global restart_flag
        if rotation >= 156:
            rotation = 155
        elif rotation <= -156:
            rotation = -155
        modifier = rotation/180
        final_speed = round(self.speed * modifier)
        if direction == 'up':
            final_v_speed = self.speed * -(1 - abs(modifier))
        else:
            final_v_speed = self.speed * 1 - abs(modifier)
        self.rect.x += final_speed
        # self.rect.y += final_v_speed
        # print(final_v_speed)
        
        self.rect.y += final_v_speed
            
        # -180 - 0 - 180 
        
        self.rect.centerx, self.rect.top
        if restart_flag and cooldown == 180:
            self.speed = game_speed
        elif restart_flag:
            cooldown += 1
    def restart(self, x, y):
        global restart_flag
        global cooldown
        restart_flag = True
        cooldown = 0
        self.speed = 0
        self.rect.x = x
        self.rect.y = y

save = {}
with open('data/data.json', 'r', encoding='utf-8') as file:
    save = json.load(file)
# параметры игры
game_speed = save['game_speed']
ball_size = save['ball_size']
debug = False

ball_x = 0
ball_y = 0
cooldown = 190
restart_flag = False
p1_last = 0
p2_last = 0
rotation = -50
direction = 'down'
w_width = 1000
w_height = 700
player = Player('pngs/player.png', 290, w_height-70, 100, 40, game_speed)
player2 = Player2('pngs/enemy.png', 290, 30, 100, 40, game_speed)
player_hb_center = HitboxCenterP1('pngs/player.png', player.rect.centerx - 30, player.rect.top, 60, 10, 0)
player_hb_hard_l = LHitboxHardP1('pngs/player.png', player.rect.centerx - 50, player.rect.top, 20, 30, 0)
player_hb_hard_r = RHitboxHardP1('pngs/player.png', player.rect.centerx + 30, player.rect.top, 20, 30, 0)
player2_hb_center = HitboxCenterP2('pngs/player.png', player2.rect.centerx - 30, player2.rect.bottom - 10, 60, 10, 0)
player2_hb_hard_l = LHitboxHardP2('pngs/player.png', player2.rect.centerx - 50, player2.rect.bottom - 30, 20, 30, 0)
player2_hb_hard_r = RHitboxHardP2('pngs/player.png', player2.rect.centerx + 30, player2.rect.bottom - 30, 20, 30, 0)
right_wall = RWallHitbox('pngs/player.png', -9, 0, 10, 720, 0)
left_wall = LWallHitbox('pngs/player.png', w_width+9, 0, 10, 720, 0)
p1_wall = P1WallHitbox('pngs/player.png', 0, w_height - 1, w_width, 10, 0)
p2_wall = P2WallHitbox('pngs/player.png', 0, 1, w_width, 10, 0)

ball = Ball('pngs/ball.png', w_width/2, w_height/2, ball_size, ball_size, game_speed)
# Размеры окна игры
# устанавливаем размеры окна игры
window = display.set_mode((w_width, w_height))
# название
display.set_caption('Ping pong')


# загружаем фон
bg = image.load("pngs/bg.png")
# меняем его размеры
background = transform.scale(bg, (w_width, w_height))

# главная переменная
game = True

clock = time.Clock()
FPS = 60

start_dir = randint(1, 2)
if start_dir == 1:
    p1_wall.ball_collide(ball)
else:
    p2_wall.ball_collide(ball)
    

# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
font.init()
font1 = font.SysFont(None, 80)
font2 = font.SysFont(None, 36)
gameOver = font1.render("You Lose", True, (255, 0, 0))
youWin = font1.render("You Win", True, (255, 255, 0))
youWinBrilliant = font1.render("You Win (no loses)", True, (35, 255, 200))
# основной цикл
update_keys = True
while game:

    # узнаем когда крестик и закрываем игру
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE or e.key == K_r:
                p1_wall.ball_collide(ball)
    window.blit(background, (0, 0))
    player.before_update()
    player2.before_update()
    player.update(player_hb_center, player_hb_hard_l, player_hb_hard_r)
    player2.update(player2_hb_center, player2_hb_hard_l, player2_hb_hard_r)
    ball.update()
    player.reset()
    player2.reset()
    if debug:
        player_hb_center.reset()
        player_hb_hard_l.reset()
        player_hb_hard_r.reset()
        player2_hb_center.reset()
        player2_hb_hard_l.reset()
        player2_hb_hard_r.reset()
    ball.reset()
    right_wall.reset()
    left_wall.reset()
    p1_wall.reset()
    if sprite.collide_rect(ball, right_wall):
        right_wall.ball_collide(ball)
    if sprite.collide_rect(ball, left_wall):
        left_wall.ball_collide(ball)
    if sprite.collide_rect(ball, player_hb_hard_r):
        player_hb_hard_r.ball_collide(ball)
    elif sprite.collide_rect(ball, player_hb_hard_l):
        player_hb_hard_l.ball_collide(ball)
    elif sprite.collide_rect(ball, player_hb_center):
        player_hb_center.ball_collide(ball)
    if sprite.collide_rect(ball, player2_hb_hard_r):
        player2_hb_hard_r.ball_collide(ball)
    elif sprite.collide_rect(ball, player2_hb_hard_l):
        player2_hb_hard_l.ball_collide(ball)
    elif sprite.collide_rect(ball, player2_hb_center):
        player2_hb_center.ball_collide(ball)
    if sprite.collide_rect(ball, p1_wall):
        p1_wall.ball_collide(ball)
    if sprite.collide_rect(ball, p2_wall):
        p2_wall.ball_collide(ball)
    if cooldown >= 1 and cooldown < 59:
        window.blit(font1.render("3...", True, (255, 25, 25)), (w_width - 350, 200))
    if cooldown >= 60 and cooldown < 119:
        window.blit(font1.render("2..", True, (255, 20, 20)), (w_width - 350, 200))
    if cooldown >= 120 and cooldown < 179:
        window.blit(font1.render("1.", True, (255, 0, 0)), (w_width - 350, 200))


    # player2.reset()
    display.update()
    clock.tick(FPS)










