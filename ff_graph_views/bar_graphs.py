import matplotlib.pyplot as plt
import matplotlib.cm as mplcm
import matplotlib.colors as colors

import numpy as np

def bar_percentage(data):
    # Number of Final Fantasy Games (excluding Total Votes)
    NUM_GAMES = len(data) - 1

    # Number of Rounds (excluding Total Votes and final game not to be eliminated)
    NUM_ROUNDS = len(data) - 2

    fig = plt.figure()
    ax = fig.add_subplot(111)

    y_data = []
    for key in data:
        if key != "Total Votes":
            for i in range(len(data[key])):
                if i >= len(y_data):
                    y_data.append([])
                y_data[i].append([data[key][i], int(key)])

    for i in range(len(y_data)):
        y_data[i].sort()
        temp = [y_data[i][0]]
        for k in range(1, len(y_data[i])):
            temp.append([y_data[i][k][0] + temp[-1][0], y_data[i][k][1]])
        y_data[i] = temp
        y_data[i] = [[100 * (x[0] / y_data[i][-1][0]), x[1]] for x in y_data[i]]
        y_data[i] = y_data[i][::-1]


    cmap = plt.cm.tab20
    cmaplist = [cmap(i * (1 / NUM_GAMES)) for i in range(NUM_GAMES)]

    x_data = list(range(1, NUM_ROUNDS + 1))
    for i in range(len(y_data)):
        for k in range(len(y_data[i])):
            if i == 0:
                if k == 0:
                    ax.bar(x_data[i], y_data[i][k][0], color=cmaplist[y_data[i][k][1] - 1], label="Final Fantasy " + str(y_data[i][k][1]))
                else:
                    ax.bar(x_data[i], y_data[i][k][0], color=cmaplist[y_data[i][k][1] - 1], label="Final Fantasy " + str(y_data[i][k][1]))
            else:
                if k == 0:
                    ax.bar(x_data[i], y_data[i][k][0], color=cmaplist[y_data[i][k][1] - 1])
                else:
                    ax.bar(x_data[i], y_data[i][k][0], color=cmaplist[y_data[i][k][1] - 1])

    '''
    for i in data:
        if key != "Total Votes":
            # Convert vote data to percentage of total votes
            y_data = [int((data[key][i] / data["Total Votes"][i]) * 100) for i in range(len(data[key]))]

            # Set X values to start at 1
            x_data = list(range(1, len(y_data) + 1))

            # Plot Lines and Points
            ax.bar(x_data, y_data, label="Final Fantasy " + key)
    '''

    plt.title("Final Fantasy Games Elimination Rounds - Results")

    # Set X ticks to be every round of elimination [1, NUM_GAMES - 1]
    plt.xticks(list(range(1, NUM_ROUNDS + 1)))
    plt.xlabel("Nth Round of Votes")

    # Set Y ticks to be every 5 percent instead of every 10 percent.
    plt.yticks(list(range(0, 105, 5)))
    plt.ylabel("Percentage (%)")

    handles, labels = ax.get_legend_handles_labels()
    # sort both labels and handles by labels
    labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: int(t[0][len("Final Fantasy "):])))

    ax.legend(handles, labels, loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()