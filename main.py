# Eli and Asher, Tic-Tac-Toe

# statements to import functions
from basic_tic_tac_toe import game
from highscore_managment import *

chosen = 0

# function with the main user interface
def main():
    if chosen == 0:
        profile = profile_manager()
    
    choice = input("""1. Play Tic-Tac-Toe
    2. Change Profile
    3. End
    Enter the number of the thing you would like to do: """)
    if choice == "1":
        players = input("do you want to play 1. a two player game against a friend or 2. a one player game against a bot (enter the number next to the option you want): ")
        
        profile = game(profile)
        with open("highscores.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(profile)
    elif choice == "2":
        profile = profile_manager()
    elif choice == "3":
        return "end"
    else:
        print("that is not an option")
        return main()

# loop that makes sure the program continues until the user is done 
while True:
    end = main()
    chosen = 56
    if end == "end":
        print("thank you for using this program")
        break
    else:
        highscore()