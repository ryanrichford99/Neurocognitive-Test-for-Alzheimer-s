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
IconY = 100
IconX_change = 30
IconY_change = 40

bulletimg = pygame.image.load('arrow_up.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "raedy" #ready state means you cant see  it and fire state means its in motion
bullet_count = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

def Icon(x,y):
    screen.blit(IconImg, (x, y))


def fire_bullet(x, y):
    global bullet_state #cant call from function if its not global
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 1, y + 10)) #make sure the bullet appears in the centre of the space ship

def iscollide (Icon3X, Icon3Y, bulletX, bulletY):
    distance = math.sqrt(math.pow(Icon3X - bulletX, 2) + math.pow(Icon3Y - bulletY,2)) #this is the equasion for the disstance
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

            if event.key == pygame.K_RIGHT:
                playerX_change = 3

            if event.key == pygame.K_SPACE:
                    bullet_count += 1
                    bulletX = playerX
                    fire_bullet(playerX,bulletY)
                    print("bullets fired =",bullet_count)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    elif playerX  >=736: # trial and error shows 736 as the best boader
        playerX = 736

    IconX += IconX_change
#if the icon hist pixel 0 it is changed to plus 3, once it hist pixel 736 it then moves to -0.3
    if IconX <= 0:
        IconX_change = random.randint(2,7)
    elif IconX >= 736:  # trial and error shows 736 as the best boader
        IconX_change = random.uniform(-3,-7)


    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"

    #collide
    collision = iscollide(IconX,IconY,bulletX,bulletY)
    if collision:
        bulletY = 480# if the function collide is met then the bullet state iss chaaged and one is added to the score
        bullet_state = "ready"
        score += 1
        print("bullets hit =",score)
        IconX = random.randint(0,735)
        #id the cillision is met the game icon is moved
        stop = time.time()


    def percentage():
        if bullet_count == 11:
            percent1 = score / bullet_count
            percent2 = percent1 * 100
            percent3 = round(percent2)
            print("percent2 = ", percent2)
            return percent3

    def show_titles(percent3):  # UI text and info

        title_font = pygame.font.Font('freesansbold.ttf', 32)
        content_font = pygame.font.Font('freesansbold.ttf', 32)

        title_text = title_font.render('Visuospatial Battery:', True, WHITE)
        title_rect = title_text.get_rect(midtop=(800 // 3.5, 25))

        level_text = content_font.render(f'Accuracy = {percent3}%', True, WHITE)
        level_rect = level_text.get_rect(midtop=(800 // 1.30, 25))

        screen.blit(title_text, title_rect)
        screen.blit(level_text, level_rect)


    player(playerX,playerY)
    Icon(IconX,IconY)
    show_titles(percentage())
    percentage()
    pygame.display.update()