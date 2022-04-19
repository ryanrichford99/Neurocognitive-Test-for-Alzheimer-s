import pygame


from tkinter import *


root = Tk()
root.geometry("600x800")
root.title("HOMEPAGE")
myLabel = Label(root, text="General User Interface", width = 50, height = 8, fg = "red")
myLabel.pack()
speed = 0

memory1 = False
speed1 = 0






import random
import pygame

pygame.init()
# constants and variables
WIDTH = 600
HEIGHT = 600
white = (200,0,0)
black = (0,0,0)
green = (0,255,0)
grey = (0,0,0)
example_mem = 26
fps = 60
timer = pygame.time.Clock()

rows = 6
cols = 8
correct =   [[0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]]
op_list = []
spaces = []
used = []
new_board = True
first_guess = False
second_guess = False
first_guess_num = 0
second_guess_num = 0
score = 0
best_score = 0
matches = 0
game_over = False






def Memory(WIDTH,HEIGHT,white,black,green,grey,fps,timer,rows,cols,correct,op_list,spaces,used,new_board,first_guess,second_guess,first_guess_num,second_guess_num,score,best_score,matches,game_over):


    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    pygame.display.set_caption('memory battery')
    title_font = pygame.font.Font('freesansbold.ttf', 56)
    small_font = pygame.font.Font('freesansbold.ttf', 26)

    def generate_board(): # creating a randomly generated number lsit
        global op_list
        global spaces
        for item in range(rows * cols // 2):
            op_list.append(item)

    #grabs an option from list of optioned made and it grabs a number from 0-23 and then checks it agaist the used list, fiannly it will draw it anc check again agaisnt the first number
        for item in range(rows * cols):
            piece = op_list[random.randint(0,len(op_list)-1)]
            spaces.append(piece)
            if piece in used:
                used.remove(piece)
                op_list.remove(piece)
            else:
                used.append(piece)



    def draw_background():
        top_menu = pygame.draw.rect(screen, black, [0,0,WIDTH,100])
        title_text = title_font.render('Memory Battery', True, white)
        screen.blit(title_text, (10,20))
        board_space = pygame.draw.rect(screen, grey, [0, 100, WIDTH, HEIGHT - 200] ,)
        top_menu = pygame.draw.rect(screen, black, [0, HEIGHT - 100, WIDTH, 100])
        reset_button = pygame.draw.rect(screen, grey, [10, HEIGHT - 90, 160, 80], 0, 3)
        #reset_text = title_font.render('Reset', True, white)
        #screen.blit(reset_text, (10,520))

       # score_text = small_font.render(f'score: {score}', True, white)
        #screen.blit(score_text, (350,520))
        #best_text = small_font.render(f'Previous Best: {best_score}', True, white)
        #screen.blit(best_text, (350, 560))
        return reset_button


    def draw_board():
        global rows
        global cols
        global correct
        board_list = []
        for i in range(cols):
            for j in range(rows):# this will complete the rectangles relitive tro the I and J pixles, this has been taken from a pygame tutorial and has been referenced
                piece = pygame.draw.rect(screen, white, [i * 75 + 12, j * 65 + 112, 50, 50],0,4) # the + 112 is padding to move them further away
                board_list.append(piece)


                #so you can show
                piece_text = small_font.render(f'{spaces[i * rows + j]}', True, black)
                screen.blit(piece_text, (i * 75 + 18, j * 65 + 120))

        for r in range(rows):
            for c in range(cols):
                if correct[r][c] == 1:
                    pygame.draw.rect(screen, green, [c * 75 + 10, r * 65 + 110, 54, 54], 3, 4)
                    piece_text = small_font.render(f'{spaces[c * rows + r]}', True, black)
                    screen.blit(piece_text, (c * 75 + 18, r * 65 + 120))


    # the screen blit line has given the numbers a ssimilar spot but has given + 12 to move it from left and to move it down the + 65
        return board_list


    def check_guesses(first,second):
        global spaces
        global correct
        global score
        global matches

        if spaces[first] == spaces[second]:
            col1 = first // rows
            col2 = second // rows
            row1 = first - (first // rows * rows)
            row2 = second - (second // rows * rows )
            if correct[row1][col1] == 0 and correct[row2][col2] == 0:
                correct[row1][col1] = 1
                correct[row2][col2] = 1
                score += 1
                matches += 1
                print(correct)
        else:
            score += 0

    running = True
    while running:
        timer.tick(fps)
        screen.fill(white)
        if new_board:
            generate_board()
            print(spaces)
            new_board = False

        reset = draw_background()
        board = draw_board()

        if first_guess and second_guess:
            check_guesses(first_guess_num, second_guess_num)
            pygame.time.delay(1000)
            first_guess = False
            second_guess = False


        #if quit is pressed the while loop for the game is false

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                title_text = title_font.render('Memory Battery', True, black)
                screen.blit(title_text, (10, 20))
                print("return")
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(board)):
                    button = board[i]
                    if not game_over:
                        if button.collidepoint(event.pos) and not first_guess:
                            first_guess = True
                            first_guess_num = i
                            print(i)
                        if button.collidepoint(event.pos) and not second_guess and first_guess and i != first_guess_num:
                            second_guess = True
                            second_guess_num = i
                            print(i)
                if reset.collidepoint(event.pos):
                    op_list = []
                    used = []
                    spaces = []
                    new_board = True
                    score = 0
                    matches = 0
                    first_guess = False
                    second_guess = False
                    correct =   [[0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0],
                                 [0,0,0,0,0,0,0,0]]
                    game_over = False

        if matches == rows * cols // 2:
            game_over = True
            winner = pygame.draw.rect(screen, grey, [10, HEIGHT- 300 , WIDTH - 20, 80] ,0,5)
            winner_text = title_font.render(f'Complete in {score} moves', True, white)
            screen.blit(winner_text, (10, HEIGHT - 290))
            if best_score > score or best_score == 0:
                memory_score = score
                print (memory_score)



        if first_guess:
            piece_text = small_font.render(f'{spaces[first_guess_num]}', True, black)
            location = (first_guess_num // rows * 75 + 18, (first_guess_num - (first_guess_num // rows * rows))* 65 + 120)
            screen.blit(piece_text, (location))

        if second_guess:
            piece_text = small_font.render(f'{spaces[second_guess_num]}', True, black)
            location = (second_guess_num // rows * 75 + 18, (second_guess_num - (second_guess_num // rows * rows)) * 65 + 120)
            screen.blit(piece_text, (location))




        pygame.display.flip()
    pygame.quit()
    return score
print(score)



#-----------------------------------------------------------------------------------------------------------


import pygame
import math
import random
import time
import mysql.connector


def Speed_battery():
    tic = time.time()
    data = [0,0,0,0,0,0,0,0,0,0]
    clickcount = 0
    example_answer = 0.3
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
    running = 0

    #--------------------------------all colors and metrics for screen above-------------------------------------------

    myfont = pygame.font.SysFont('freesansbold.ttf',42)
    myfont_large = pygame.font.SysFont('freesansbold.ttf',52)

    #---------------------------------fonts and size--------------------------------------------------------------------

    surface = myfont.render("Speed Battery", False, red)

    colors = [red,red]

    clo = pygame.time.Clock()
    cx = random.randint(15, width - 15)
    cy = random.randint(40, height - 400)
    width_of_circle = random.randint(14, 20)
    pygame.draw.circle(screen, random.choice(colors), (cx, cy), width_of_circle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

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
                global speed_final_score
                speed_final_score = average_text
                average_gui = 0
                average_gui = average_text
            pygame.draw.circle(screen, random.choice(colors), (cx,cy), width_of_circle)
        screen.blit(surface,(200,20))
        pygame.display.update()
        clock.tick()



def Database():
    print("speed", speed_final_score)

#-----------------------------------------------------------------------------------------------------------------------


def memory():
    Memory(WIDTH,HEIGHT,white,black,green,grey,fps,timer,rows,cols,correct,op_list,spaces,used,new_board,first_guess,second_guess,first_guess_num,second_guess_num,score,best_score,matches,game_over)
    myButton.pack()

def speed():
    global speed1
    Speed_battery()
    myButton1.pack()

def visuo():
    import percent
    myButton2.pack()

def database():
    import exam
    myButton3.pack()


myButton = Button(root, text=("MEMORY BATTERY:\nMemory Battery requires you to locate matching \n boxes, once complete you will be given a score out of 21\n" ),width = 50, height = 5, command=memory, fg="red", bg="black")
myButton.pack()

myLabe2 = Label(root, text=" ")
myLabe2.pack()

myButton1 = Button(root, text="SPEED BATTERY:\n Speed Battery requires you to click the red circle 10 times,\n once complete an average speed will be scored ", width = 50, height = 5,  command=speed, fg="red", bg="black")
myButton1.pack()

myLabe4 = Label(root, text=" ")
myLabe4.pack()

myButton2 = Button(root, text="VISUOSPATIAL BATTERY:\nVisuospatial Battery requires you to hit targets,\nthe first 3 shots are not counted. Following this a mark out of 10 will be provided\n (10=100%)", width = 50, height = 5,  command=visuo, fg="red", bg="black")
myButton2.pack()

myLabe5 = Label(root, text=" ")
myLabe5.pack()

myButton3 = Button(root, text="DATABASE:\n Database will show you your previous scores", width = 50, height = 5,  command=database, fg="red", bg="black")
myButton3.pack()



root.mainloop()