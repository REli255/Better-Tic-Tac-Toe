# Eli Robison, my origianl tic-tac-toe program

import random

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rows = 3
columns = 3

def check():
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        return "you won"
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        return "you won"
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        return "you won"
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        return "you won"
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return "you won"
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        return "you won"
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return "you won"
    elif board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
        return "you won"
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        return "you lost"
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        return "you lost"
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        return "you lost"
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        return "you lost"
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        return "you lost"
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        return "you lost"
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return "you lost"
    elif board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
        return "you lost"
    else:
        return "you tied"

def game(profile):
    turns = 0
    winner = check()
    even = [0, 2, 4, 6, 8]

    while turns < 9 and winner != "you won" and winner != "you lost":
        for x in range(rows):
            for y in range(columns):
                print("", board[x][y], end= " |")
            print("")
        if turns in even:
            print("player's turn")
            player = int(input("enter the number of where you would like to play: "))
            if player in numbers:
                if player == 1:
                    board[0][0] = "X"
                    numbers.remove(player)
                    turns += 1
                elif player == 2:
                    board[0][1] = "X"
                    numbers.remove(player)
                    turns += 1
                elif player == 3:
                    board[0][2] = "X"
                    numbers.remove(player)
                    turns += 1
                elif player == 4:
                    board[1][0] = "X"
                    numbers.remove(player)
                    turns += 1
                elif player == 5:
                    board[1][1] = "X"
                    numbers.remove(player)
                    turns += 1
                elif player == 6:
                    board[1][2] = "X"
                    numbers.remove(player)
                    turns += 1
                elif player == 7:
                    board[2][0] = "X"
                    numbers.remove(player)
                    turns += 1
                elif player == 8:
                    board[2][1] = "X"
                    numbers.remove(player)
                    turns += 1
                elif player == 9:
                    board[2][2] = "X"
                    numbers.remove(player)
                    turns += 1
                else:
                    print("that is not an option")
            else:
                print("that is not an option")
        else:
            print("computer's turn")
            computer = random.choice(numbers)
            if computer == 1:
                board[0][0] = "O"
            elif computer == 2:
                board[0][1] = "O"
            elif computer == 3:
                board[0][2] = "O"
            elif computer == 4:
                board[1][0] = "O"
            elif computer == 5:
                board[1][1] = "O"
            elif computer == 6:
                board[1][2] = "O"
            elif computer == 7:
                board[2][0] = "O"
            elif computer == 8:
                board[2][1] = "O"
            elif computer == 9:
                board[2][2] = "O"
            turns += 1
            numbers.remove(computer) 
        winner = check()

    for x in range(rows):
            for y in range(columns):
                print("", board[x][y], end= " |")
            print("")
    print(winner)
    if winner == "you won":
        profile = [profile[0], int(profile[1]) + 1]
    return profile