# statement to import matplotlib
import matplotlib.pyplot as plt

# function to make a bar graph of the top five scores
def display_wins(people, wins):
    fig, ax = plt.subplots()
    
    bar_labels = people
    bar_colors = ['crimson', 'orangered', 'gold', 'olivedrab', 'hotpink']

    ax.bar(people, wins, label=bar_labels, color=bar_colors)#makes the bar graph

    ax.set_ylabel('Wins')#y axis label
    ax.set_xlabel('Top 5 People')#x axis label

    ax.set_title('Highscores')
    ax.legend(title='People')
    
    plt.show()#shows the bar graph