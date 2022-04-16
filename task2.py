import math
from turtledemo import clock

import pygame
import time
import pygame
import math

sw = 800
sh = 800

bg = pygame.image.load('backg.png')
alienImg = pygame.image.load('icon1.png')
player = pygame.image.load('arrow_up.png')
star = pygame.image.load('icon2.png')
asteroid = pygame.image.load('icon3.png')

pygame.display.set_caption('asteroids')

win = pygame.display.set_mode((sw, sh))

clock = pygame.time.Clock()

gameover = False

class Player(object):
    def __init__(self):
        self.img = player
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = sw//2
        self.y = sh//2# screen wwidth and height devided by 2 in order to get tehe size of the player img
        self.angle = 0
        self.rotatedSurface = pygame.transform.rotate(self.img, self.angle) # this rotate and give the neww up value of image
        self.rotatedRect = self.rotatedSurface.get_rect()
        self.rotatedRect.center = (self.x, self.y) #re align the center with the upwards arrow icon
        self.cosine = math.cos(math.radians(self.angle + 90)) # this 90 will fix the offset but the middle is off to the right side so the 90 will fix it
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w//2, self.y - self.sine * self.h//2) #this is to always knoww where the fron of thre icon is to show the bullet direction

    def draw(self, win):
       # win.blit(self.img, [self.x, self.y, self.w, self.h]) #old line does take changed of the arroe into account but neww line does
        win.blit(self.rotatedSurface, self.rotatedRect)

    def turnLeft(self):
        self.angle += 5
        self. rotatedSurface = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurface.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.cosine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w//2, self.y - self.sine * self.h//2)

    def turnRight(self):
        self.angle -= 5
        self. rotatedSurface = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurface.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.cosine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w//2, self.y - self.sine * self.h//2)

    def moveForwward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurface = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurface.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.cosine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w // 2, self.y - self.sine * self.h // 2)

class Bullet(object):
    def __init__(self):
        self.point = player.head
        self.x, self.y = self.point
        self.w = 4
        self.h = 4
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c * 10
        self.yv = self.s * 10

    def move(self):
        self.x += self.xv
        self.y += self.yv

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), [self.x, self.y, self.w, self.h])


def redrawGW():
    win.blit(bg, (0, 0))
    player.draw(win)
    pygame.display.update()

player = Player()
run = True
while run:
    clock.tick(60)

    if not gameover:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.turnLeft()
        if keys[pygame.K_RIGHT]:
            player.turnRight()
        if keys[pygame.K_UP]:
            player.moveForwward()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGW()
pygame.quit()