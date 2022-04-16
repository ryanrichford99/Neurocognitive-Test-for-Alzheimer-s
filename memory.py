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

#screen

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
            #piece_text = small_font.render(f'{spaces[i * rows + j]}', True, grey) # had to have a look into matrix maths.
            #screen.blit(piece_text, (i * 75 + 18, j * 65 + 120))

    for r in range(rows):
        for c in range(cols):
            if correct[r][c] == 1:
                pygame.draw.rect(screen, green, [c * 75 + 10, r * 65 + 110, 54, 54], 3, 4)
                piece_text = small_font.render(f'{spaces[c * rows + r]}', True, grey)
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
            running = False
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
            best_score = score



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

