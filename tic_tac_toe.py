import random

from get_mouse import *
from grid import *

def main():
    print("""
    Choices
    1. Single Player
    2. Two Player
    3. Exit
    """)

    choice = input("Choose a Number: ")

    if choice == "1":
        board = set_board()
        game_single_play(board)
    elif choice == "2":
        board = set_board()
        game_two_play(board)
    else:
        exit()



def set_board():
    slot1 = "1"
    slot2 = "2"
    slot3 = "3"
    slot4 = "4"
    slot5 = "5"
    slot6 = "6"
    slot7 = "7"
    slot8 = "8"
    slot9 = "9"

    choices = [slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9]

    board_row1 = [slot1,slot2,slot3]
    board_row2 = [slot4,slot5,slot6]
    board_row3 = [slot7,slot8,slot9]

    board = [board_row1,
            board_row2,
            board_row3]

    return board, choices

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
    

def game_two_play():
    pass

def game_single_play(board):
    screen = set_grid()#Activate PyGame Window
    game = True
    
    def game_run():
        for row in board:
            print(row)

        mouse_x, mouse_y = get_mouse_pos(screen)#Get User's Choice On The Board
        draw_x(mouse_x, mouse_y, screen)

        mouse_x, mouse_y = bot_choice()
        draw_o(mouse_x, mouse_y, screen)

    while game == True:
        game_run()


main()