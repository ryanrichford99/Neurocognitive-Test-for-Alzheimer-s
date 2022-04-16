import os

import pygame
#cv2
import random
from pygame.examples.joystick import WHITE


class Tile (pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        super()
        super().__init__()

        self.name = filename.split('.')[0]

        self.original_image = pygame.image.load('ryanrichford/images/icons/' + filename)

        self.back_image = pygame.image.load('images/icons/' + filename)
        pygame.draw.rect(self.back_image, WHITE, self.back_image.get_rect())

        self.image = self.back_image
        self.rect = self.image.get_rect(topleft = (x,y))
        self.shown = False

    def update(self):
        self.image = self.original_image if self.shown else self.back_image

    def show(self):
        self.shown = True
    def hide(self):
        self.shown = False





class Game():
    def __init__(self):
        self.level = 1 # the first level
        self.level_complete = False

        # initialise icons as well as the other things
        self.all_icons = [f for f in os.listdir('ryanrichford/Documents/icons') if os.path.join('ryanrichford/Documents/icons, f')]
        self.img_width, self.img_height = (128,128)
        self.margin_top = 160
        self.cols = 4
        self.rows = 2
        self.width = 1280

    def update(self, event_list):
        self.user_input(event_list)
        self.draw()

    def user_input(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('down')



    def draw(self):
        screen.fill(RED)
#font ui text and info
        title_font = pygame.font.Font('freesansbold.ttf',32)
        content_font = pygame.font.Font('freesansbold.ttf',32)
#text
        title_text = title_font.render('Memory Game', True, WHITE)
        title_rect = title_text.get_rect(midtop = (W_Width // 2, 10))

        level_text = content_font.render('Level  ' + str(self.level), True, WHITE)
        level_rect = level_text.get_rect(midtop = (W_Width // 1.25, 45))


        info_text = content_font.render('Match 2 of each type:', True, WHITE)
        info_rect = info_text.get_rect(midtop = (W_Width // 4, 45))

        screen.blit(title_text, title_rect)
        screen.blit(level_text, level_rect)
        screen.blit(info_text, info_rect)

# we are the line above 25:26

W_Width = 800
W_Height = 600
screen = pygame.display.set_mode((W_Width, W_Height))#sceen size in pixel
pygame.display.set_caption('Memeory battery')
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

RGB = (255, 0, 0)
FPS = 60 #if i wanted to have a video background
clock = pygame.time.Clock()
game = Game()


running = True #using a wile instead of an event for the fps
while running:
    event_list = pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.update(event_list)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()


