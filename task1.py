import pygame
import random
import pygame
import random
import math
import cmath # for the negitive sqrt for distance for hitts
import time

pygame.init()
# created screen of 800 pix by 600 pix, first did not add second brackets and would not work
screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('backg.png')
background = pygame.transform.scale(background, (800,600))

pygame.display.set_caption("Task One")  # changing the game title
icon = pygame.image.load('player.png')
pygame.display.set_icon(icon)# cant get the icon to show up at the moment



# player image or images
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 250
playerX_change = 0
playerY_change = 0


# interactive icon and the chosen image


iconimg1 = pygame.image.load('icon1.png')
iconimg1 =pygame.transform.scale(iconimg1, (64,64))
icon1X = random.randint(20,750)
icon1Y = random.randint(20,750)
icon1X_change = 1
icon1Y_change = -1

iconimg2 = pygame.image.load('icon2.png')
iconimg2 =pygame.transform.scale(iconimg2, (64,64))
icon2X = random.randint(30,750)
icon2Y = random.randint(50,400)
icon2X_change = 1
icon2Y_change = -1

iconimg3 = pygame.image.load('icon3.png')
iconimg3 =pygame.transform.scale(iconimg3, (64,64))
icon3X = random.randint(50,750)
icon3Y = random.randint(50,400)
icon3X_change = 2
icon3Y_change = -2

iconimg4 = pygame.image.load('icon4.png')
iconimg4 =pygame.transform.scale(iconimg4, (64,64))
icon4X = random.randint(0,800)
icon4Y = random.randint(50,400)
icon4X_change = 2
icon4Y_change = -2

score = 0

start = time.time()

now = time.gmtime()
now = time.asctime(now)


def player(x, y):
    screen.blit(playerImg, (x, y))  # writing the image and the axis onto the game screen using blit

def icon1(x, y):
    screen.blit(iconimg1, (x, y))

def icon2(x, y):
    screen.blit(iconimg2, (x, y))

def icon3(x, y):
    screen.blit(iconimg3, (x, y))

def icon4(x, y):
    screen.blit(iconimg4, (x, y))

def iscollide(icon1X, icon1Y, playerX ,playerY): # keepa hitting on the y axis, tried to fix with getting other veriables in
    callable(icon1Y)
    callable(playerY)
    distance = math.sqrt(math.pow(icon1Y - playerY, 2))
    distance1 = math.sqrt(math.pow(icon1X - playerX, 2))
    if distance < 4:
        return True
    elif distance1 < 4:
        return True
    else:
        return False

running = True  # Game loop
while running:

    # RGB
    screen.fill((211, 211, 211))
    screen.blit(background,(0,0))


    for event in pygame.event.get():  # Error was here
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # process events & if quit button is hit the window will close
        # Update your sprites

        # keystroke left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
                print("left")
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
                print("right")
            if event.key == pygame.K_UP: #all event keys for up down left and right displayed on the program as i go
                playerY_change = -3
                print("up")
            if event.key == pygame.K_DOWN:
                playerY_change = +3
                print("down")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0


    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736 # these are x and y boundaries for players icon

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

#__________________________________ Distance calc using complex math and sqrt__________________________

    if not icon1X:
        print("no")
    else:
        from cmath import sqrt

        distance = cmath.sqrt((icon1X - icon1Y) ^ 2 + (playerX - playerY) ^ 2)
        print("distance", distance)


    #___________________ ICON1 _________________________________________

    icon1X += icon1X_change
    icon1Y += icon1Y_change

    if icon1X <= 0:
        icon1X_change = 2
    elif icon1X >= 736:
        icon1X_change = -2 # these are x and y boundaries for players icon

    if icon1Y <= 0:
        icon1Y_change = 2
    elif icon1Y >= 536:
        icon1Y_change = -2

#______________________ ICON2 ________________________________________________

    icon2X += icon2X_change
    icon2Y += icon2Y_change

    if icon2X <= 0:
        icon2X_change = 2
    elif icon2X >= 736:
        icon2X_change = -2  # these are x and y boundaries for players icon

    if icon2Y <= 0:
        icon2Y_change = 2
    elif icon2Y >= 536:
        icon2Y_change = -2

#______________________ ICON3 ________________________________________________

    icon3X += icon3X_change
    icon3Y += icon3Y_change

    if icon3X <= 0:
        icon3X_change = 2
    elif icon3X >= 736:
        icon3X_change = -2 # these are x and y boundaries for players icon

    if icon3Y <= 0:
        icon3Y_change = 2
    elif icon3Y >= 536:
        icon3Y_change = -2

#_____________________ ICON4 ______________________________________________________

    icon4X += icon4X_change
    icon4Y += icon4Y_change

    if icon4X <= 0:
        icon4X_change = 2
    elif icon4X >= 736:
        icon4X_change = -2  # these are x and y boundaries for players icon

    if icon4Y <= 0:
        icon4Y_change = 2
    elif icon4Y >= 536:
        icon4Y_change = -2

#______________________ collide __________________________________________

    collide = iscollide(icon1X,icon1Y,playerX,playerY)
    if collide:
        icon1X = 1
        icon1Y = 1
        player_state = "ready"
        score += 1
        print(score)
        stop = time.time()
        print(stop - start)

    collide = iscollide(icon2X, icon2Y, playerX, playerY)
    if collide:
        icon2X = 100000
        icon2Y = 100000
        player_state = "ready"
        score += 1
        print(score)

    collide = iscollide(icon3X, icon3Y, playerX, playerY)
    if collide:
        icon3X = 1000000
        icon3Y = 1000000
        player_state = "ready"
        score += 1
        print(score)

    collide = iscollide(icon4X, icon4Y, playerX, playerY)
    if collide:
        icon4X = 10000000
        icon4Y = 10000000
        player_state = "ready"
        score += 1
        print(score)




    #iconimg2 += icon2X_change
    player(playerX, playerY)
    icon1(icon1X,icon1Y)
    icon2(icon2X,icon2Y)
    icon3(icon3X,icon3Y)
    icon4(icon4X,icon4Y)# sends def player funtion to draw at correct coordinates
    pygame.display.update()
