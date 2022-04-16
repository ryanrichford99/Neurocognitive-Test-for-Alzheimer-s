import pygame
import math
import random
import time
import mysql.connector




pygame.init()


tic = time.time()
data = [0,0,0,0,0,0,0,0,0,0]
clickcount = 0


pygame.display.set_caption("Speed Battery")
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
purple = (120,0,120)
grey = (120,120,120)
sky = (0,0,220)
blue = (0,0,255)
red = (255,0,0)
orange = (255,102,0)
pink = (255,0,255)
lime = (153,204,0)
score = 0

#--------------------------------all colors and metrics for screen above-------------------------------------------

myfont = pygame.font.SysFont('freesansbold.ttf',42)
myfont_large = pygame.font.SysFont('freesansbold.ttf',52)

#---------------------------------fonts and size--------------------------------------------------------------------

surface = myfont.render("Speed Battery", False, red)


#----------------------------------render the sureface seena bove---------------------------------------------


colors = [red,red]

#------------------------------------array of colors used (made it only red)--------------------------------------------

clo = pygame.time.Clock()

cx = random.randint(15, width - 15)
cy = random.randint(40, height - 400)
width_of_circle = random.randint(14, 20)
pygame.draw.circle(screen, random.choice(colors), (cx, cy), width_of_circle)

#----------------------------------------x and y of circle constraints for thr rand function----------------------------------------


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()












#--------------------------------------------quit button--------------------------------------------------------------


    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    click = pygame.mouse.get_pressed()

    sqx = (x - cx)**2
    sqy = (y - cy)**2

    if math.sqrt(sqx + sqy) < width_of_circle and click[0] ==1:

        screen.fill(black)
        clickcount += 1
        toc = time.time()
        timespent = tic - toc
        print("time taken =",timespent)
        data.append(timespent)
        print("numbers taken",data)
        average = sum(data) / len(data)
        average_round = round(average, 3)
        average_text = myfont_large.render(f'-------{average_round} is your average--------', False, red)
        width_of_circle = random.randint(15,30 )
        cx = random.randint(20, width - 100)
        cy = random.randint(20, height - 100)
        if clickcount == 10:
            print('average =', average_text)
            screen.blit(average_text, (30, 550))
            width_of_circle = random.randint(0, 0)




        pygame.draw.circle(screen, random.choice(colors), (cx,cy), width_of_circle)


    screen.blit(surface,(200,20))
    pygame.display.update()
    clock.tick()