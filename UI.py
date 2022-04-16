import tkinter
import pygame







pygame.init()

white = (255,255,255)
grey = (0,115,115)
black = (0,0,0)
red = (255,255,0)
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
pos = 0
new = (255,0,0)



#---------------------------------fonts and size--------------------------------------------------------------------

myfont = pygame.font.SysFont('freesansbold.ttf',50)
myfont1 = pygame.font.SysFont('freesansbold.ttf', 30)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    def draw_background():
        top_menu = pygame.draw.rect(screen, black, [0, 0, width, 100])
        board_space1 = pygame.draw.rect(screen, grey, [0, 200, width - 330, height - 500], )
        board_space2 = pygame.draw.rect(screen, grey, [0, 330, width - 0, height - 500], )
        board_space3 = pygame.draw.rect(screen, new, [330, 200, width, height - 500], )
        top_menu = pygame.draw.rect(screen, black, [0, height - 100, width, 100])
        reset_button = pygame.draw.rect(screen, grey, [10, height - 90, 160, 80], 0, 3)
        return board_space1,board_space3,board_space2

        pos = pygame.mouse.get_pos()
        if pos





    # board space 3 = speed

    def titles():
        surface = myfont.render("General User Interface", False, red)
        surface1 = myfont1.render("Please choose the battery you would like to play.", False, red)
        surface2 = myfont1.render("Memory Battery", False, red)
        surface3 = myfont1.render("Visuospatial Battery", False, red)
        surface4 = myfont1.render("Speed Battery", False, red)
        surface5 = myfont1.render("Database", False, red)


        screen.blit(surface, (120, 20))
        screen.blit(surface1, (70, 60))
        screen.blit(surface2, (60, 240))
        screen.blit(surface3, (190, 370))
        screen.blit(surface4, (380, 240))
        screen.blit(surface5, (40, 540))

    draw_background()
    titles()
    pygame.display.update()