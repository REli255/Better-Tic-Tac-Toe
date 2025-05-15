import matplotlib.pyplot as plt

def display_wins(people):
    fig, ax = plt.subplots()

    people = ['Drake', 'MillyBobbyBrown', 'Billie Eilish', 'Diddy', 'Justin Beiber']
    
    wins = [40, 100, 30, 55, 10]
    bar_labels = people
    bar_colors = ['crimson', 'orangered', 'gold', 'olivedrab', 'hotpink']

    ax.bar(people, wins, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Wins')
    ax.set_xlabel('Top 5 People')

    ax.set_title('Highscores')
    ax.legend(title='People')

    plt.show()

display_wins()



    
    