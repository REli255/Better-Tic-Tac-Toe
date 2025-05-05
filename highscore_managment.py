# Eli Robison

import csv

def highscore():
    scores = []

    with open("highscores.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            scores.append({row[0]:row[1]})
            print(row)
    
    scores.sort()

    print(scores)

def profile_maker():
    pass

def profile_search():
    pass

def profile_managment():
    pass

highscore()