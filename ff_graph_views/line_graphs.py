import matplotlib.pyplot as plt
import matplotlib.cm as mplcm
import matplotlib.colors as colors


def plot_percentages(data):
    # Number of Final Fantasy Games (excluding Total Votes)
    NUM_GAMES = len(data) - 1

    # Number of Rounds (excluding Total Votes and final game not to be eliminated)
    NUM_ROUNDS = len(data) - 2

    cmap = plt.cm.tab20
    cmaplist = [cmap(i * (1 / NUM_GAMES)) for i in range(NUM_GAMES)]

    fig = plt.figure()
    ax = fig.add_subplot(111)

    for key in data:
        if key != "Total Votes":
            # Convert vote data to percentage of total votes
            y_data = [int((data[key][i] / data["Total Votes"][i]) * 100) for i in range(len(data[key]))]

            # Set X values to start at 1
            x_data = list(range(1, len(y_data) + 1))

            # Plot Lines and Points
            ax.plot(x_data, y_data, label="Final Fantasy " + key, color=cmaplist[int(key) - 1])
            ax.scatter(list(range(1, len(y_data) + 1)), y_data, color=cmaplist[int(key) - 1])

    plt.title("Final Fantasy Games Elimination Rounds - Results")

    # Set X ticks to be every round of elimination [1, NUM_GAMES - 1]
    plt.xticks(list(range(1, NUM_ROUNDS + 1)))
    plt.xlabel("Nth Round of Votes")

    # Set Y ticks to be every 5 percent instead of every 10 percent.
    plt.yticks(list(range(0, 105, 5)))
    plt.ylabel("Percentage (%)")

    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()


def plot_votes(data, log=False):
    # Number of Data Rows
    NUM_ROWS = len(data)

    # Number of Rounds (minus total votes and final game not eliminated)
    NUM_ROUNDS = len(data) - 2

    cmap = plt.cm.tab20
    cmaplist = [cmap(i * (1 / NUM_ROWS)) for i in range(NUM_ROWS)]
    cmaplist = {k: x for k, x in zip(data.keys(), cmaplist)}

    fig = plt.figure()
    ax = fig.add_subplot(111)

    for key in data:
        label = key
        if label != "Total Votes":
            label = "Final Fantasy " + label
        x_data = list(range(1, len(data[key]) + 1))
        ax.plot(x_data, data[key], label=label)
        ax.scatter(list(range(1, len(data[key]) + 1)), data[key])

    plt.title("Final Fantasy Games Elimination Rounds - Results")

    plt.xticks(list(range(1, NUM_ROUNDS + 1)))
    plt.xlabel("Nth Round of Votes")

    # Set to log scale if log parameter is true
    if log:
        plt.yscale("log")
        plt.ylabel("# of Votes (log10)")
    else:
        plt.ylabel("# of Votes")

    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()
