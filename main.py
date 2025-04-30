# Eli and Asher, Tic-Tac-Toe

# statement to import a function
from basic_tic_tac_toe import game
from highscore_managment import *



# function with the main user interface
def main():
    if chosen == 0:
        profile_managment()
    
    choice = input("""1. Play Tic-Tac-Toe
    2. Change Profile
    3. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        game()
    elif choice == "2":
        profile_managment()
    elif choice == "3":
        return "end"
    else:
        print("that is not an option")

# loop that makes sure the program continues until the user is done 
while True:
    end = main()
    chosen = 56
    if end == "end":
        print("thank you for using this program")
        break