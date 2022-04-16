
import pygame
import random
import math
import cmath
import time 


pygame.init() #init game

W_width = 800
W_height = 600
screen = pygame.display.set_mode((W_width, W_height))#sceen size in pixel
background = pygame.image.load('backg.png')
pygame.display.set_caption("Visuospatial Battery")
icon = pygame.image.load('player.png')
pygame.display.set_icon(icon) #cant get the icon to work

average_acuracy = 0

bullet_used = 0
score = 0

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

WHITE = (0, 0,
         255)

def show_titles(): # UI text and info
    title_font = pygame.font.Font('freesansbold.ttf',32)
    content_font = pygame.font.Font('freesansbold.ttf',32)

    title_text = title_font.render('Visuospatial Battery', True, WHITE)
    title_rect = title_text.get_rect(midtop = (800 // 2, 10))

    #level_text = content_font.render('Acuracy =  ', True, WHITE)
   # level_rect = level_text.get_rect(midtop=(800 // 1.30, 45))

    #info_text = content_font.render('Hit Targets with arrow!:', True, WHITE)
    #info_rect = info_text.get_rect(midtop=(800 // 4, 45))

    screen.blit(title_text, title_rect)
    #screen.blit(level_text, level_rect)
    #screen.blit(info_text, info_rect)


def show_score(x,y):
    score = font.render("score :" + str(score_value),True, (255,255,255))
    screen.blit(score,(x,y))



start = time.time()
now = time.gmtime()
now = time.asctime(now)

#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

IconImg = pygame.image.load('icon1.png')
IconX = random.randint(0,800)
IconY = random.randint(50,150)
IconX_change = 3
IconY_change = 40

Iconimg2 = pygame.image.load('icon2.png')
Iconimg2 =pygame.transform.scale(Iconimg2, (60,60))
Icon2X = random.randint(0,750)
Icon2Y = random.randint(50,150)
Icon2X_change = 3
Icon2Y_change = 40

Iconimg3 = pygame.image.load('icon3.png')
Iconimg3 = pygame.transform.scale(Iconimg3, (64,64))
Icon3X = random.randint(0,750)
Icon3Y = random.randint(50,150)
Icon3X_change = 3
Icon3Y_change = 40

Iconimg4 = pygame.image.load('icon4.png')
Iconimg4 =pygame.transform.scale(Iconimg4, (64,64))
Icon4X = random.randint(0,750)
Icon4Y = random.randint(50,150)
Icon4X_change = 3
Icon4Y_change = 40

bulletimg = pygame.image.load('arrow_up.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "raedy" #ready state means you cant see  it and fire state means its in motion

def player(x,y):
    screen.blit(playerImg, (x, y))

def Icon(x,y):
    screen.blit(IconImg, (x, y))

def Icon2(x,y):
    screen.blit(Iconimg2, (x, y))

def Icon3(x,y):
    screen.blit(Iconimg3, (x, y))

def Icon4(x,y):
    screen.blit(Iconimg4, (x, y))

def fire_bullet(x, y):
    global bullet_state #cant call from function if its not global
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 1, y + 10)) #make sure the bullet appears in the centre of the space ship

def iscollide (IconX, IconY, bulletX, bulletY):
     #this is the equasion for the disstance
    if distance < 35:
        return True
        print(f'Acuracy red = {distance}')
    else:
        return False

def iscollide (Icon2X, Icon2Y, bullet2X, bulletY):
    distance = math.sqrt(math.pow(Icon2X - bullet2X, 2) + math.pow(Icon2Y - bulletY,2)) #this is the equasion for the disstance
    if distance < 35:
        return True
        print(f'Acuracy red = {distance}')
    else:
        return False

def iscollide (Icon3X, Icon3Y, bulletX, bulletY):
    distance = math.sqrt(math.pow(Icon3X - bulletX, 2) + math.pow(Icon3Y - bulletY,2)) #this is the equasion for the disstance
    if distance < 35:
        return True
        print(f'Acuracy red = {distance}')
    else:
        return False

def iscollide (Icon4X, Icon4Y, bulletX, bulletY):
    distance = math.sqrt(math.pow(Icon4X - bulletX, 2) + math.pow(Icon4Y - bulletY,2)) #this is the equasion for the disstance
    if distance < 35:
        return True
        print(f'Acuracy red = {distance}')
    else:
        return False

# keep the game running always (im going to be putting notes in here for the eventuality of the deposition thingy )
running = True
while running:

    screen.fill((0, 0, 0))  # RGB colours
    screen.blit(background, (0,0)) #every itteration is happening slower after addimg image so i have to incraese the value



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

         # if key is pressed check right or left prinf ststments added like the first try to check movement and that the loop is working
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
                print("left")
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
                print("right")
            if event.key == pygame.K_SPACE:

                    bulletX = playerX
                    fire_bullet(playerX,bulletY)
                    print("space")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print("keyup")

    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    elif playerX  >=736: # trial and error shows 736 as the best boader
        playerX = 736

    IconX += IconX_change
#if the icon hist pixel 0 it is changed to plus 3, once it hist pixel 736 it then moves to -0.3
    if IconX <= 0:
        IconX_change = 3
        IconY += IconY_change
        bullet_used += 1
    elif IconX >= 736:  # trial and error shows 736 as the best boader
        IconX_change = -3
        IconY += IconY_change
        bullet_used += 1#bullet used has one added if it hists or misses, thiw will be used later for the memeory

    Icon2X += Icon2X_change

    if Icon2X <= 0:
        Icon2X_change = 3
        Icon2Y += IconY_change
        bullet_used += 1
    elif Icon2X >= 736:  # trial and error shows 736 as the best boader
        Icon2X_change = -3
        Icon2Y += Icon2Y_change
        bullet_used += 1

    Icon3X += Icon3X_change

    if Icon3X <= 0:
        Icon3X_change = 3
        Icon3Y += IconY_change
        bullet_used += 1
    elif Icon3X >= 736:  # trial and error shows 736 as the best boader
        Icon3X_change = -3
        Icon3Y += Icon3Y_change
        bullet_used += 1

    Icon4X += Icon4X_change

    if Icon4X <= 0:
        Icon4X_change = 3
        Icon4Y += IconY_change
        bullet_used += 1
    elif Icon4X >= 736:  # trial and error shows 736 as the best boader
        Icon4X_change = -3
        Icon4Y += Icon4Y_change
        bullet_used += 1






    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"
        print("bullet used", bullet_used)



    #collide
    collision = iscollide(IconX,IconY,bulletX,bulletY)
    if collision:
        bulletY = 480# if the function collide is met then the bullet state iss chaaged and one is added to the score
        bullet_state = "ready"
        score += 1
        print ("score =", score)
        print("bullet used", bullet_used)
        IconX = random.randint(0,735)
        IconY = random.randint(50, 150) #id the cillision is met the game icon is moved
        stop = time.time()
        print(stop - start) #to get the time needed for hitt anf fitts law

    collision = iscollide(Icon2X, Icon2Y, bulletX, bulletY)
    if collision:
        bullet2Y = 480  # if the function collide is met then the bullet state iss chaaged and one is added to the score
        bullet_state = "ready"
        score += 1
        print("score =", score)
        print("bullet used", bullet_used)
        Icon2X = random.randint(0, 735)
        Icon2Y = random.randint(50, 150)  # id the cillision is met the game icon is moved
        stop = time.time()
        print(stop - start)  # to get the time needed for hitt anf fitts law

    collision = iscollide(Icon3X, Icon3Y, bulletX, bulletY)
    if collision:
        bullet3Y = 480  # if the function collide is met then the bullet state iss chaaged and one is added to the score
        bullet_state = "ready"
        score += 1
        print("score =", score)
        print("bullet used", bullet_used)
        Icon3X = random.randint(0, 735)
        Icon3Y = random.randint(50, 150)  # id the cillision is met the game icon is moved
        stop = time.time()
        print(stop - start)  # to get the time needed for hitt anf fitts law

    collision = iscollide(Icon4X, Icon4Y, bulletX, bulletY)
    if collision:
        bullet4Y = 480  # if the function collide is met then the bullet state iss chaaged and one is added to the score
        bullet_state = "ready"
        score += 1
        print("score =", score)
        print("bullet used", bullet_used)
        Icon4X = random.randint(0, 735)
        Icon4Y = random.randint(50, 150)  # id the cillision is met the game icon is moved
        stop = time.time()
        print(stop - start)  # to get the time needed for hitt anf fitts law


    player(playerX,playerY)
    Icon(IconX,IconY)
    Icon2(Icon2X, Icon2Y)
    Icon3(Icon3X, Icon3Y)
    Icon4(Icon4X, Icon4Y)
    show_score(textX, textY)
    show_titles()

    pygame.display.update()