import random
import time

from get_mouse import *
from grid import *
from place_mark import *
from check_space import *
from tic_single_play import set_board

def tic_two_play(profile, profile_2):

    def check_win(row_1, row_2, row_3, choices, profile, profile_2):
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
            end = 0
            for x in range(len(choices)):
                print(choices[str(x + 1)])
                if choices[str(x + 1)]:
                    end += 1
            if end == 9:
                game = False
                print("Its a Draw")

        return game, profile, profile_2


    screen = set_grid()#Activate PyGame Window
    board, choices, slots = set_board()
    game = True

    print(board[1][1])
    
    def game_run(board, choices, profile, profile_2, slots):
        print("Its Player 1's Turn")
        mouse_x, mouse_y = get_mouse_pos()#Get User's Choice On The Board
        mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
        board, choices, slots = draw_x(mouse_x, mouse_y, screen, board, choices, slots)
        game, profile, profile_2 = check_win(board[0], board[1], board[2], choices, profile, profile_2)
        
        if game == False:
            time.sleep(0.5)
            return game, profile, profile_2

        time.sleep(0.1)
        print("Its Player 2's Turn")
        mouse_x, mouse_y = get_mouse_pos()#Get User's Choice On The Board
        mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
        board, choices, slots = draw_o(mouse_x, mouse_y, screen, board, choices, slots)
        game, profile, profile_2 = check_win(board[0], board[1], board[2], choices, profile, profile_2)

        time.sleep(0.5)
        return game, profile, profile_2

    while game == True:
        game, profile, profile_2 = game_run(board, choices, profile, profile_2, slots)
    time.sleep(0.5)
    pygame.quit()
    
    return profile, profile_2