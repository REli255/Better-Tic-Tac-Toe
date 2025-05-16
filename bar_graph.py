import matplotlib.pyplot as plt

def display_wins(people):
    fig, ax = plt.subplots()

    people = ['Drake', 'MillyBobbyBrown', 'Billie Eilish', 'Diddy', 'Justin Beiber']#top 5 people
    
    wins = [40, 100, 30, 55, 10]#amount of wins they have
    bar_labels = people
    bar_colors = ['crimson', 'orangered', 'gold', 'olivedrab', 'hotpink']

    ax.bar(people, wins, label=bar_labels, color=bar_colors)#makes the bar graph

    ax.set_ylabel('Wins')#y axis label
    ax.set_xlabel('Top 5 People')#x axis label

    ax.set_title('Highscores')
    ax.legend(title='People')

    plt.show()#shows the bar graph

display_wins()



    
    