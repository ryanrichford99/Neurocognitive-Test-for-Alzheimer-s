import pygame

# i have done this to initialise my pygame
pygame.init()
# created screen of 800 pix by 600 pix, first did not add second brackets and would not work
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Games 1st iteration")  # changing the game title
icon = pygame.image.load('thinking.png')
pygame.display.set_icon(icon)  # cant get the icon to show up at the moment

# player image or images
playerImg = pygame.image.load('arrow_up.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))  # writing the image and the axis onto the game screen using blit


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

        # keystroke left or right, up or down using the x a y axis
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
    player(playerX, playerY)  # sends def player funtion to draw at correct coordinates
    pygame.display.update()


