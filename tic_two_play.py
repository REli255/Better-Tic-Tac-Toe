import random
import time

from get_mouse import *
from grid import *
from place_mark import *
from check_space import *

def tic_two_play(profile):

    def continue_play():
        print("""
        Choices
        1. Continue Play
        2. Exit and Save Score
        """)

        choice = input("Choose a Number: ")

        if choice == "1":
            tic_two_play()
        elif choice == "2":
            pass

    def set_board(choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"], board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]): return board, choices


    def check_win(row_1, row_2, row_3, choices, profile):
        game = True
        
        if row_1[0] == "X" and row_1[1] == "X" and row_1[2] == "X":
            print("Player 1 Won")
            profile = [profile[0], int(profile[1]) + 1]
            game = False
        elif row_2[0] == "X" and row_2[1] == "X" and row_2[2] == "X":
            print("Player 1 Won")
            profile = [profile[0], int(profile[1]) + 1]
            game = False
        elif row_3[0] == "X" and row_3[1] == "X" and row_3[2] == "X":
            print("Player 1 Won")
            profile = [profile[0], int(profile[1]) + 1]
            game = False
        elif row_1[0] == "X" and row_2[0] == "X" and row_3[0] == "X":
            print("Player 1 Won")
            profile = [profile[0], int(profile[1]) + 1]
            game = False
        elif row_1[1] == "X" and row_2[1] == "X" and row_3[1] == "X":
            print("Player 1 Won")
            profile = [profile[0], int(profile[1]) + 1]
            game = False
        elif row_1[2] == "X" and row_2[2] == "X" and row_3[2] == "X":
            print("Player 1 Won")
            profile = [profile[0], int(profile[1]) + 1]
            game = False
        elif row_1[0] == "X" and row_2[1] == "X" and row_3[2] == "X":
            print("Player 1 Won")
            profile = [profile[0], int(profile[1]) + 1]
            game = False
        elif row_1[2] == "X" and row_2[1] == "X" and row_3[0] == "X":
            print("Player 1 Won")
            profile = [profile[0], int(profile[1]) + 1]
            game = False
        elif row_1[0] == "O" and row_1[1] == "O" and row_1[2] == "O":
            print("Player 2 Won")
            profile_2 = [profile_2[0], int(profile_2[1]) + 1]
            game = False
        elif row_2[0] == "O" and row_2[1] == "O" and row_2[2] == "O":
            print("Player 2 Won")
            profile_2 = [profile_2[0], int(profile_2[1]) + 1]
            game = False
        elif row_3[0] == "O" and row_3[1] == "O" and row_3[2] == "O":
            print("Player 2 Won")
            profile_2 = [profile_2[0], int(profile_2[1]) + 1]
            game = False
        elif row_1[0] == "O" and row_2[0] == "O" and row_3[0] == "O":
            print("Player 2 Won")
            profile_2 = [profile_2[0], int(profile_2[1]) + 1]
            game = False
        elif row_1[1] == "O" and row_2[1] == "O" and row_3[1] == "O":
            print("Player 2 Won")
            profile_2 = [profile_2[0], int(profile_2[1]) + 1]
            game = False
        elif row_1[2] == "O" and row_2[2] == "O" and row_3[2] == "O":
            print("Player 2 Won")
            profile_2 = [profile_2[0], int(profile_2[1]) + 1]
            game = False
        elif row_1[0] == "X" and row_2[1] == "X" and row_3[2] == "X":
            print("Player 2 Won")
            profile_2 = [profile_2[0], int(profile_2[1]) + 1]
            game = False
        elif row_1[2] == "X" and row_2[1] == "X" and row_3[0] == "X":
            print("Player 2 Won")
            profile_2 = [profile_2[0], int(profile_2[1]) + 1]
            game = False
        else:
            try:
                random.choice(choices)
            except:
                game = False
                print("Its a Draw")

        return game, profile


    screen = set_grid()#Activate PyGame Window
    board, choices = set_board()
    game = True

    print(board[1][1])
    
    def game_run(board, choices, profile):
        print("Its Player 1's Turn")
        mouse_x, mouse_y = get_mouse_pos()#Get User's Choice On The Board
        mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
        board, choices = draw_x(mouse_x, mouse_y, screen, board, choices)
        game, profile = check_win(board[0], board[1], board[2], choices, profile)
        
        if game == False:
            time.sleep(0.5)
            return game

        time.sleep(0.1)
        print("Its Player 2's Turn")
        mouse_x, mouse_y = get_mouse_pos()
        mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
        board, choices = draw_o(mouse_x, mouse_y, screen, board, choices)
        game, profile = check_win(board[0], board[1], board[2], choices, profile)

        time.sleep(0.5)
        return game, profile

    while game == True:
        game = game_run(board, choices)
    
    return profile