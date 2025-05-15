# Eli Robison

import csv
from bar_graph import display_wins

def highscore():
    profiles = []
    scores = []

    with open("highscores.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            profiles.append([row[0], row[1]])
            scores.append(row[1])
    scores.sort(reverse=True)

    top = 0
    ties = 0
    for score in scores:
        if ties > 1:
            ties -= 1
            continue
        ties = 0
        if top < 5:
            for user in profiles:
                if user[1] == score:
                    print(top + 1, ":", user[0], "won", user[1], "times")
                    ties += 1
            for x in range(ties):
                top += 1
    
    display_wins()

def profile_maker():
    name = input("Enter the username you want: ")
    profile = [name, 0]
    with open("highscores.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(profile)
    return profile

def profile_search():
    profiles = []

    with open("highscores.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            profiles.append([row[0], row[1]])
    
    found = 0
    username = input("Enter the username of your profile: ")
    for item in profiles:
        if item[0] == username:
            found += 1
            profile = item
        else:
            pass
    if found == 0:
        print("The username you entered did not match any of the profiles")
        profile = profile_manager()
        return profile
    else:
        print("Profile Found")
        return profile

def profile_manager():
    print("""
    Profile Choices
    1. Make a New Profile
    2. Choose an Old Profile
    """)
    
    choice = input("Choose a Number: ")
    
    if choice == "1":
        profile = profile_maker()
    elif choice =="2":
        profile = profile_search()
    else:
        print("That is not an option")
        profile = profile_manager()
    return profile