import random
import time

from get_mouse import *
from grid import *
from place_mark import *
from check_space import *

def set_board(): #sets the board where the users choices are gonna be stored to use because pygame is for visuals only
    slots = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    choices = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False, "7": False, "8": False, "9": False}
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return board, choices, slots

def bot_choice(choices,slots):#returns a random x and y cordinate using the available choices
    slot = random.choice(slots)

    if slot == 1:
        mouse_x = 150
        mouse_y = 150
    elif slot == 2:
        mouse_x = 450
        mouse_y = 150
    elif slot == 3:
        mouse_x = 750
        mouse_y = 150
    elif slot == 4:
        mouse_x = 150
        mouse_y = 450
    elif slot == 5:
        mouse_x = 450
        mouse_y = 450
    elif slot == 6:
        mouse_x = 750
        mouse_y = 450
    elif slot == 7:
        mouse_x = 150
        mouse_y = 750
    elif slot == 8:
        mouse_x = 450
        mouse_y = 750
    elif slot == 9:
        mouse_x = 750
        mouse_y = 750

    return mouse_x, mouse_y
    


def check_win_single(row_1, row_2, row_3, choices, profile):#checks for win conditions and runs code based on it
    game = True
    
    if row_1[0] == "X" and row_1[1] == "X" and row_1[2] == "X":
        print("You Won")
        profile = [profile[0], int(profile[1]) + 1]
        game = False
    elif row_2[0] == "X" and row_2[1] == "X" and row_2[2] == "X":
        print("You Won")
        profile = [profile[0], int(profile[1]) + 1]
        game = False
    elif row_3[0] == "X" and row_3[1] == "X" and row_3[2] == "X":
        print("You Won")
        profile = [profile[0], int(profile[1]) + 1]
        game = False
    elif row_1[0] == "X" and row_2[0] == "X" and row_3[0] == "X":
        print("You Won")
        profile = [profile[0], int(profile[1]) + 1]
        game = False
    elif row_1[1] == "X" and row_2[1] == "X" and row_3[1] == "X":
        print("You Won")
        profile = [profile[0], int(profile[1]) + 1]
        game = False
    elif row_1[2] == "X" and row_2[2] == "X" and row_3[2] == "X":
        print("You Won")
        profile = [profile[0], int(profile[1]) + 1]
        game = False
    elif row_1[0] == "X" and row_2[1] == "X" and row_3[2] == "X":
        print("You Won")
        profile = [profile[0], int(profile[1]) + 1]
        game = False
    elif row_1[2] == "X" and row_2[1] == "X" and row_3[0] == "X":
        print("You Won")
        profile = [profile[0], int(profile[1]) + 1]
        game = False
    elif row_1[0] == "O" and row_1[1] == "O" and row_1[2] == "O":
        print("The Bot Won")
        game = False
    elif row_2[0] == "O" and row_2[1] == "O" and row_2[2] == "O":
        print("The Bot Won")
        game = False
    elif row_3[0] == "O" and row_3[1] == "O" and row_3[2] == "O":
        print("The Bot Won")
        game = False
    elif row_1[0] == "O" and row_2[0] == "O" and row_3[0] == "O":
        print("The Bot Won")
        game = False
    elif row_1[1] == "O" and row_2[1] == "O" and row_3[1] == "O":
        print("The Bot Won")
        game = False
    elif row_1[2] == "O" and row_2[2] == "O" and row_3[2] == "O":
        print("The Bot Won")
        game = False
    elif row_1[0] == "X" and row_2[1] == "X" and row_3[2] == "X":
        print("The Bot Won")
        game = False
    elif row_1[2] == "X" and row_2[1] == "X" and row_3[0] == "X":
        print("The Bot Won")
        game = False
    else:#uses this to make sure the game ends after the board is full
        end = 0
        for x in range(len(choices)):
            print(choices[str(x + 1)])
            if choices[str(x + 1)]:
                end += 1
        if end == 9:
            game = False
            print("Its a Draw")

    return game, profile


def tic_single_play(profile):# starts the tic-tac-toe game using the alredy made functions
    screen = set_grid()#Activate PyGame Window
    board, choices, slots = set_board()#makes the board that is going to be used to get win conditions
    game = True
    
    def game_run(board, choices, profile, slots):
        print("Its Your Turn")
        mouse_x, mouse_y = get_mouse_pos()#Get User's Choice On The Board
        mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)#makes sure their choice is valid
        board, choices, slots = draw_x(mouse_x, mouse_y, screen, board, choices, slots)# draws the mark on the board
        game, profile = check_win_single(board[0], board[1], board[2], choices, profile)#checks if anyone has won yet and ends the game if someone has
        
        if game == False:#stops the game if someone has won
            time.sleep(0.5)#a delay
            return game, profile

        time.sleep(0.5)
        print("Bot Placed Mark")
        mouse_x, mouse_y = bot_choice(choices, slots)
        board, choices, slots = draw_o(mouse_x, mouse_y, screen, board, choices, slots)
        game, profile = check_win_single(board[0], board[1], board[2], choices, profile)

        time.sleep(0.5)
        return game, profile

    while game == True:# keeps the game running if no one has one
        game, profile = game_run(board, choices, profile, slots)
    time.sleep(0.5)
    pygame.quit()# closes the pygame window

    return profile