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
    name = input("enter the username you want: ")
    with open("highscores.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(name, 0)
      
    profile = [name, 0]
    return profile

def profile_search():
    profiles = []

    with open("highscores.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            profiles.append([row[0], row[1]])
    
    username = input("enter the username of your profile: ")
    for item in profiles:
        if item[0] == username:
            print("your profile was found")
            return item
        else:
            pass
    print("the username you entered did not match any of the profiles")


def profile_manager():
    choice = input("do you want to 1. make a new profile or 2. choose an old profile (enter the number next to the option you want): ")
    if choice == "1":
        profile = profile_maker()
    elif choice =="2":
        profile = profile_search()
    else:
        print("that is not an option")
        profile = profile_manager()
    return profile