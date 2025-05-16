import matplotlib.pyplot as plt

def display_wins(people, wins):
    fig, ax = plt.subplots()

    bar_labels = people
    bar_colors = ['crimson', 'orangered', 'gold', 'olivedrab', 'hotpink']

    ax.bar(people, wins, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Wins')
    ax.set_xlabel('Top 5 People')

    ax.set_title('Highscores')
    ax.legend(title='People')

    plt.show() 