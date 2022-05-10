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
ball = GameSprite('ball.jpg',400,300,speed,40,40)
clock = time.Clock()
FPS = 60

#игровой цикл

finish = True
menu_1 = True
menu_reshim = False
game = True
reshim = 0

while game:
    window.blit(background,(0,0))
    player_left.reset()
    player_right.reset()
    player_left.update()
    player_right.update()

    for e in event.get():
            if e.type == QUIT:
                game = False
    clock.tick(FPS)
    display.update()  
        

