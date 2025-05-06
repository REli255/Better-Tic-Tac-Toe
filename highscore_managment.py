# Eli Robison

import csv

def highscore():
    profiles = []
    scores = []

    with open("highscores.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            profiles.append([row[0], row[1]])
            scores.append(row[1])
    scores.sort()

    top = 0
    for score in scores:
        if top < 5:
            for user in profiles:
                if user[1] == score:
                    print(top + 1, ":", user[0], "won", user[1], "times in a row")
        top += 1

def profile_maker():
    pass

def profile_search():
    profiles = []

    with open("highscores.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            profiles.append([row[0], row[1]])
    
    username = input()
    for item in profiles:
        if item == username:
            print("your profile was found")
            profile = item
            break
        else:
            pass
    print("the username you entered did not match any of the profiles")


def profile_manager():
    choice = input()
    if choice == "1":
        profile_maker()
    elif choice =="2":
        profile_search()
    else:
        print("that is not an option")
        profile_manager()