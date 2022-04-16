import pygame
import sys
import random
import math
import pygame

pygame.init()

display = pygame.display.set_mode((1000, 800))
player = pygame.transform.smoothscale(pygame.image.load("arrow_up.png").convert_alpha(), (100, 100))


iconimg1 = pygame.image.load('icon1.png')
iconimg1 = pygame.transform.scale(iconimg1, (64, 64))
icon1X = random.randint(20, 750)
icon1Y = random.randint(20, 750)


def icon1(x, y):
    display.blit(iconimg1, (x, y))


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


icon1(icon1X, icon1Y)
pygame.display.update()

