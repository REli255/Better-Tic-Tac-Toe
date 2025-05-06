#Asher Wangia, Tic-Tac-Toe game
import random

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

print("You are X")
game = True



while game == True:
    
    valid = True
    board_row1 = [slot1,slot2,slot3]
    board_row2 = [slot4,slot5,slot6]
    board_row3 = [slot7,slot8,slot9]
    
    board = [board_row1,
            board_row2,
            board_row3]
    
    for row in board:
            print(row)
    
    user_choice = input("Choose a spot to place your mark: ")
	
    if user_choice == "1" and slot1 != "X" and slot1 != "O":
        slot1 = "X"
    elif user_choice == "2" and slot2 != "X" and slot2 != "O":
        slot2 = "X"
    elif user_choice == "3" and slot3 != "X" and slot3 != "O":
        slot3 = "X"
    elif user_choice == "4" and slot4 != "X" and slot4 != "O":
        slot4 = "X"
    elif user_choice == "5" and slot5 != "X" and slot5 != "O":
        slot5 = "X"
    elif user_choice == "6" and slot6 != "X" and slot6 != "O":
        slot6 = "X"
    elif user_choice == "7" and slot7 != "X" and slot7 != "O":
        slot7 = "X"
    elif user_choice == "8" and slot8 != "X" and slot8 != "O":
        slot8 = "X"
    elif user_choice == "9" and slot9 != "X" and slot9 != "O":
        slot9 = "X"
    else:
        print("Invalid Choice Try Again")
        valid = False
    
    
    choices = [slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9]
  
    comp_choices = []
    
    if slot1 in choices and slot1 != "X" and slot1 != "O":
        comp_choices.append(slot1)
    if slot2 in choices and slot2 != "X" and slot2 != "O":
        comp_choices.append(slot2)
    if slot3 in choices and slot3 != "X" and slot3 != "O":
        comp_choices.append(slot3)
    if slot4 in choices and slot4 != "X" and slot4 != "O":
        comp_choices.append(slot4)
    if slot5 in choices and slot5 != "X" and slot5 != "O":
        comp_choices.append(slot5)
    if slot6 in choices and slot6 != "X" and slot6 != "O":
        comp_choices.append(slot6)
    if slot7 in choices and slot7 != "X" and slot7 != "O":
        comp_choices.append(slot7)
    if slot8 in choices and slot8 != "X" and slot8 != "O":
        comp_choices.append(slot8)
    if slot9 in choices and slot9 != "X" and slot9 != "O":
        comp_choices.append(slot9)
    

    if comp_choices[0:]:
        comp_choice = random.choice(comp_choices)
    
    if valid == True:
        if comp_choice == slot1:
            slot1 = "O"
        elif comp_choice == slot2:
            slot2 = "O"
        elif comp_choice == slot3:
            slot3 = "O"
        elif comp_choice == slot4:
            slot4 = "O"
        elif comp_choice == slot5:
            slot5 = "O"
        elif comp_choice == slot6:
            slot6 = "O"
        elif comp_choice == slot7:
            slot7 = "O"
        elif comp_choice == slot8:
            slot8 = "O"
        elif comp_choice == slot9:
            slot9 = "O"


    if slot1 == "X" and slot2 == "X" and slot3 == "X":
        print("Player Won")
        game = False
    elif slot4 == "X" and slot5 == "X" and slot6 == "X":
        print("Player Won")
        game = False
    elif slot7 == "X" and slot8 == "X" and slot9 == "X":
        print("Player Won")
        game = False
    elif slot1 == "X" and slot4 == "X" and slot7 == "X":
        print("Player Won")
        game = False
    elif slot2 == "X" and slot5 == "X" and slot8 == "X":
        print("Player Won")
        game = False
    elif slot3 == "X" and slot6 == "X" and slot9 == "X":
        print("Player Won")
        game = False
    elif slot1 == "X" and slot5 == "X" and slot9 == "X":
        print("Player Won")
        game = False
    elif slot3 == "X" and slot5 == "X" and slot7 == "X":
        print("Player Won")
        game = False
    elif slot1 == "O" and slot2 == "O" and slot3 == "O":
        print("Computer Won")
        game = False
    elif slot4 == "O" and slot5 == "O" and slot6 == "O":
        print("Computer Won")
        game = False
    elif slot7 == "O" and slot8 == "O" and slot9 == "O":
        print("Computer Won")
        game = False
    elif slot1 == "O" and slot4 == "O" and slot7 == "O":
        print("Computer Won")
        game = False
    elif slot2 == "O" and slot5 == "O" and slot8 == "O":
        print("Computer Won")
        game = False
    elif slot3 == "O" and slot6 == "O" and slot9 == "O":
        print("Computer Won")
        game = False
    elif slot1 == "O" and slot5 == "O" and slot9 == "O":
        print("Computer Won")
        game = False
    elif slot3 == "O" and slot5 == "O" and slot7 == "O":
        print("Computer Won")
        game = False