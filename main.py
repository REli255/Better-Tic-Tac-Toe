# Eli and Asher, Tic-Tac-Toe

# statements to import functions
from basic_tic_tac_toe import game
from highscore_managment import *
from tic_single_play import tic_single_play
from tic_two_play import tic_two_play

chosen = 0

# function with the main user interface
def main(profile):
    if chosen == 0:
        profile = profile_manager()
    

    print("""
    Choices
    1. Play Tic-Tac-Toe
    2. Change Profile
    3. End
    """)
    choice = input("Enter the number of the thing you would like to do: ")
    
    if choice == "1":
        print("""
        Tic-Tac-Toe Choices
        1. Play Two Player(With a Friend)
        2. One Player(Play Against a Bot)
        """)
        
        players = input("Choose a Number: ")
        
        profiles = []
        if players == "2":
            profile = tic_single_play(profile)
            with open("highscores.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    profiles.append([row[0], row[1]])
            for item in profiles:
                if item[0] == profile[0]:
                    if item[0] == profiles[0][0]:
                        with open("highscores.csv", "w", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow(profile)
                    else:
                        with open("highscores.csv", "a", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow(profile)
                else:
                    if item[0] == profiles[0][0]:
                        with open("highscores.csv", "w", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow(item)
                    else:
                        with open("highscores.csv", "a", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow(item)
        elif players == "1":
            print("set a profile for the second player")
            profile_2 = profile_manager()
            profile, profile_2 = tic_two_play(profile, profile_2)
            with open("highscores.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    profiles.append([row[0], row[1]])
            for item in profiles:
                if item[0] == profile[0]:
                    if item[0] == profiles[0][0]:
                        with open("highscores.csv", "w", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow(profile)
                    else:
                        with open("highscores.csv", "a", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow(profile)
                elif item[0] == profile_2[0]:
                    if item[0] == profiles[0][0]:
                        with open("highscores.csv", "w", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow(profile_2)
                    else:
                        with open("highscores.csv", "a", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow(profile_2)
                else:
                    if item[0] == profiles[0][0]:
                        with open("highscores.csv", "w", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow(item)
                    else:
                        with open("highscores.csv", "a", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow(item)
        else:
            print("That is not an option")
    elif choice == "2":
        profile = profile_manager()
    elif choice == "3":
        return "end", profile
    else:
        print("that is not an option")
    return "", profile

profile = []

# loop that makes sure the program continues until the user is done 
while True:
    end, profile = main(profile)
    chosen = 56
    if end == "end":
        print("thank you for using this program")
        break
    else:
        print("HIGHSCORES")
        highscore()