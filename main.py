from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_width = 1000
win_height = 700
back = (0, 0, 0)
display.set_caption("PingPong")
window = display.set_mode((win_width, win_height))
window.fill(back)
fon = transform.scale(image.load("fon.png"), (win_width, win_height))
game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('racket1.png', 30, 200, 4, 100, 200)
racket2 = Player('racket2.png', 870, 200, 4, 100, 200)
ball = Player('ball.png', 600, 200, 4, 80, 80)

font.init()
font = font.Font(None, 50)
lose1 = font.render('WASD ПОГИБ В БОЮ', True, (180, 0,0))
lose2 = font.render('СТРЕЛОЧНИК ПОГИБ', True, (180, 0,0))
gg = font.render('GG MAN', True, (25, 25,112))

speed_x = 1
speed_y = 1

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(fon, (0,0))
        racket1.update_1()
        racket2.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= 1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (330, 100))
            window.blit(gg, (450, 50))
            game_over = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (330, 100))
            window.blit(gg, (430, 50))
            game_over = True
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)