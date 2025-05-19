import random
import time

from get_mouse import *
from grid import *
from place_mark import *
from check_space import *
from tic_single_play import set_board

def tic_two_play(profile, profile_2):
    def check_win(row_1, row_2, row_3, choices, profile, profile_2):#checks for win conditions and runs code based on it
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
        else:#uses this to make sure the game ends after the board is full
            end = 0
            for x in range(len(choices)):
                if choices[str(x + 1)]:
                    end += 1
            if end == 9:
                game = False
                print("Its a Draw")

        return game, profile, profile_2


    screen = set_grid()#Activate PyGame Window
    board, choices, slots = set_board()#makes the board that is going to be used to get win conditions
    game = True

    
    def game_run(board, choices, profile, profile_2, slots):
        print("Its Player 1's Turn")
        mouse_x, mouse_y = get_mouse_pos()#Get User's Choice On The Board
        mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)#makes sure their choice is valid
        board, choices, slots = draw_x(mouse_x, mouse_y, screen, board, choices, slots)# draws the mark on the board
        game, profile, profile_2 = check_win(board[0], board[1], board[2], choices, profile, profile_2)#checks if anyone has won yet and ends the game if someone has
        
        if game == False:#stops the game if someone has won
            time.sleep(0.5)#a delay
            return game, profile, profile_2

        time.sleep(0.1)
        print("Its Player 2's Turn")
        mouse_x, mouse_y = get_mouse_pos()#Get User's Choice On The Board
        mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
        board, choices, slots = draw_o(mouse_x, mouse_y, screen, board, choices, slots)
        game, profile, profile_2 = check_win(board[0], board[1], board[2], choices, profile, profile_2)

        time.sleep(0.5)
        return game, profile, profile_2

    while game == True:# keeps the game running if no one has one
        game, profile, profile_2 = game_run(board, choices, profile, profile_2, slots)
    time.sleep(0.5)
    pygame.quit()# closes the pygame window
    
    return profile, profile_2