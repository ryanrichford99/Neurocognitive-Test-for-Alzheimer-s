import pygame
import random


# i have done this to initialise my pygame
pygame.init()
# created screen of 800 pix by 600 pix, first did not add second brackets and would not work
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Games 1st iteration")  # changing the game title
icon = pygame.image.load('player.png')
pygame.display.set_icon(icon)  # cant get the icon to show up at the moment

# player image or images
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# interactive icon
iconimg = pygame.image.load('icon1.png')
iconimg =pygame.transform.scale(iconimg, (64,64))
iconX = random.randint(30,750)
iconY = random.randint(50,400)
iconX_change = 0
iconY_change = 0

iconimg1 = pygame.image.load('icon1.png')
icon1X = random.randint(30,750)
icon1Y = random.randint(50,400)
icon1X_change = 0
icon1Y_change = 0

iconimg2 = pygame.image.load('icon2.png')
iconimg2 =pygame.transform.scale(iconimg2, (64,64))
icon2X = random.randint(30,750)
icon2Y = random.randint(50,400)
icon2X_change = 0
icon2Y_change = 0

iconimg3 = pygame.image.load('icon3.png')
iconimg3 =pygame.transform.scale(iconimg3, (64,64))
icon3X = random.randint(50,750)
icon3Y = random.randint(50,400)
icon3X_change = 0
icon3Y_change = 0

iconimg4 = pygame.image.load('icon4.png')
iconimg4 =pygame.transform.scale(iconimg4, (64,64))
icon4X = random.randint(0,800)
icon4Y = random.randint(50,400)
icon4X_change = 0
icon4Y_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))  # writing the image and the axis onto the game screen using blit

def icon(x, y):
    screen.blit(iconimg, (x, y))

def icon1(x, y):
    screen.blit(iconimg1, (x, y))

def icon2(x, y):
    screen.blit(iconimg2, (x, y))

def icon3(x, y):
    screen.blit(iconimg3, (x, y))

def icon4(x, y):
    screen.blit(iconimg4, (x, y))

running = True  # Game loop
while running:

    # RGB
    screen.fill((0, 0, 0))

    for event in pygame.event.get():  # Error was here
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # process events & if quit button is hit the window will close
        # Update your sprites

        # keystroke left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
                print("left")
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
                print("right")
            if event.key == pygame.K_UP:
                playerY_change = -0.4
                print("up")
            if event.key == pygame.K_DOWN:
                playerY_change = +0.4
                print("down")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0


    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    icon(iconX, iconY)
    icon1(icon1X,icon1Y)
    icon2(icon2X,icon2Y)
    icon3(icon3X,icon3Y)
    icon4 (icon4X,icon4Y)# sends def player funtion to draw at correct coordinates
    pygame.display.update()
