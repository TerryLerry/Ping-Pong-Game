from pygame import *
mixer.init()
from random import randint
font.init() 

#создание классов

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, p_speed, w1, h1):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w1, h1))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))  

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()   
        if key_pressed[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 414:
            self.rect.y += self.speed

class Player_2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()   
        if key_pressed[K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 414:
            self.rect.y += self.speed            

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, p_speed, w1, h1, speedy, speedx):
        super().__init__(player_image, player_x, player_y, p_speed, w1, h1)
        self.speedy = speedy
        self.speedx = speedx

#создание спрайтов фона

window = display.set_mode((800,600))
display.set_caption('Space-Pong')
background = transform.scale(image.load('fon.jpg'),(800,600)) 
menu_f = transform.scale(image.load('fon_1.png'),(800,600))
menu_reshim = transform.scale(image.load('fon_reshim.png'),(800,600))

#создание спрайтов и текста

font = font.SysFont('Fixedsys',70)
player_left = Player('bluerocket.png', 30, 400, 5,60,185)
player_right = Player_2('redrocket.png', 705, 400, 5,60,185)
speedYball = 2
speedXball = 2
ball = Ball('ball.jpg',400,300,0,40,40,speedYball,speedXball)
clock = time.Clock()
FPS = 60
win_1 = font.render('Игрок 1 победил!', True, (255,215,20))
win_2 = font.render('Игрок 2 победил!', True, (255,215,20))
#игровой цикл

finish = True
menu_1 = True
menu_reshim = False
game = True
reshim = 0
n = 0
while game:

    window.blit(background,(0,0))
    player_left.reset()
    player_right.reset()
    player_left.update()
    player_right.update()
    ball.reset()

    ball.rect.y += speedYball
    ball.rect.x += speedXball
    if ball.rect.y >= 560:
        speedYball *= -1    
    if ball.rect.y <= 40:
        speedYball *= -1
    if sprite.collide_rect(ball, player_right):
        speedXball *= -1    
    if sprite.collide_rect(ball, player_left):
        speedXball *= -1     
    if ball.rect.x >= 760:
        window.blit(win_1, (200,275))
        finish = False
    if ball.rect.x <= 30:
        window.blit(win_2, (200,275))
        finish = False    
    for e in event.get():
            if e.type == QUIT:
                game = False
    clock.tick(FPS)
    display.update()  
        

