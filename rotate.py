import pygame
import sys
import random
import math
import pygame

pygame.init()


window = pygame.display.set_mode((1000, 800))
player = pygame.transform.smoothscale(pygame.image.load("arrow_up.png").convert_alpha(), (100, 100))

#   0 - image is looking to the right
#  90 - image is looking up
# 180 - image is looking to the left
# 270 - image is looking down
correction_angle = 90

iconimg1 = pygame.image.load('icon1.png')
iconimg1 = pygame.transform.scale(iconimg1, (64,64))
icon1X = random.randint(20,750)
icon1Y = random.randint(20,750)
icon1X_change = 1
icon1Y_change = -1


def icon1(x, y):
    window.blit(iconimg1, (x, y))





run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#-----------------------------------------------------------boundries

    icon1X += icon1X_change
    icon1Y += icon1Y_change

    if icon1X <= 0:
        icon1X_change = 2
    elif icon1X >= 736:
        icon1X_change = -2  # these are x and y boundaries for players icon

    if icon1Y <= 0:
        icon1Y_change = 2
    elif icon1Y >= 536:
        icon1Y_change = -2

#------------------------------------------------------get position of mouse

    player_pos = window.get_rect().center
    player_rect = player.get_rect(center=player_pos)

    mx, my = pygame.mouse.get_pos()
    dx, dy = mx - player_rect.centerx, my - player_rect.centery
    angle = math.degrees(math.atan2(-dy, dx)) - correction_angle

    rot_image = pygame.transform.rotate(player, angle)
    rot_image_rect = rot_image.get_rect(center=player_rect.center)

    window.fill((255, 255, 255))
    window.blit(rot_image, rot_image_rect.topleft)
    pygame.display.flip()



icon1(icon1X, icon1Y)
pygame.quit()
exit()
pygame.display.update()

