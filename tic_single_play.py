import random
import time

from get_mouse import *
from grid import *
from place_mark import *


def main():
    print("""
    Choices
    1. Single Player
    2. Two Player
    3. Exit
    """)

    choice = input("Choose a Number: ")

    if choice == "1":
        tic_single_play()
    else:
        exit()



def set_board(choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"], board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]): return board, choices


def bot_choice(choices):
    slot = random.choice(choices)

    if slot == "1":
        mouse_x = 150
        mouse_y = 150
    elif slot == "2":
        mouse_x = 450
        mouse_y = 150
    elif slot == "3":
        mouse_x = 750
        mouse_y = 150
    elif slot == "4":
        mouse_x = 150
        mouse_y = 450
    elif slot == "5":
        mouse_x = 450
        mouse_y = 450
    elif slot == "6":
        mouse_x = 750
        mouse_y = 450
    elif slot == "7":
        mouse_x = 150
        mouse_y = 750
    elif slot == "8":
        mouse_x = 450
        mouse_y = 750
    elif slot == "9":
        mouse_x = 750
        mouse_y = 750

    return mouse_x, mouse_y
    


def check_win_single(row_1, row_2, row_3, choices):
    game = True
    
    if row_1[0] == "X" and row_1[1] == "X" and row_1[2] == "X":
        print("You Won")
        game = False
    elif row_2[0] == "X" and row_2[1] == "X" and row_2[2] == "X":
        print("You Won")
        game = False
    elif row_3[0] == "X" and row_3[1] == "X" and row_3[2] == "X":
        print("You Won")
        game = False
    elif row_1[0] == "X" and row_2[0] == "X" and row_3[0] == "X":
        print("You Won")
        game = False
    elif row_1[1] == "X" and row_2[1] == "X" and row_3[1] == "X":
        print("You Won")
        game = False
    elif row_1[2] == "X" and row_2[2] == "X" and row_3[2] == "X":
        print("You Won")
        game = False
    elif row_1[0] == "X" and row_2[1] == "X" and row_3[2] == "X":
        print("You Won")
        game = False
    elif row_1[2] == "X" and row_2[1] == "X" and row_3[0] == "X":
        print("You Won")
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
    else:
        try:
            random.choice(choices)
        except:
            game = False
            print("Its a Draw")

    return game


def tic_single_play():
    screen = set_grid()#Activate PyGame Window
    board, choices = set_board()
    game = True

    print(board[1][1])
    
    def game_run(board, choices):
        print("Its Your Turn")
        mouse_x, mouse_y = get_mouse_pos(choices)#Get User's Choice On The Board
        board, choices = draw_x(mouse_x, mouse_y, screen, board, choices)
        game = check_win_single(board[0], board[1], board[2], choices)
        
        if game == False:
            time.sleep(0.5)
            return game

        time.sleep(0.5)
        print("Bot Placed Mark")
        mouse_x, mouse_y = bot_choice(choices)
        board, choices = draw_o(mouse_x, mouse_y, screen, board, choices)
        game = check_win_single(board[0], board[1], board[2], choices)

        time.sleep(0.5)
        return game

    while game == True:
        game = game_run(board, choices)



main()