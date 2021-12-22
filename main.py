import csv
import matplotlib.pyplot as plt
import matplotlib.cm as mplcm
import matplotlib.colors as colors


def plot_percentages(data):
    # Number of Final Fantasy Games (excluding Total Votes)
    NUM_GAMES = len(data) - 1

    # Number of Rounds (excluding Total Votes and final game not to be eliminated)
    NUM_ROUNDS = len(data) - 2

    cm = plt.get_cmap('gist_rainbow')
    cNorm = colors.Normalize(vmin=0, vmax=NUM_GAMES)
    scalarMap = mplcm.ScalarMappable(norm=cNorm, cmap=cm)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_prop_cycle(color=[scalarMap.to_rgba(i) for i in range(NUM_GAMES)])

    for key in data:
        if key != "Total Votes":
            # Convert vote data to percentage of total votes
            y_data = [int((data[key][i] / data["Total Votes"][i]) * 100) for i in range(len(data[key]))]

            # Set X values to start at 1
            x_data = list(range(1, len(y_data) + 1))

            # Plot Lines and Points
            ax.plot(x_data, y_data, label="Final Fantasy " + key)
            ax.scatter(list(range(1, len(y_data) + 1)), y_data)

    plt.title("Final Fantasy Games Elimination Rounds - Results")

    # Set X ticks to be every round of elimination [1, NUM_GAMES - 1]
    plt.xticks(list(range(1, NUM_ROUNDS + 1)))
    plt.xlabel("Nth Round of Votes")

    # Set Y ticks to be every 5 percent instead of every 10 percent.
    plt.yticks(list(range(0, 105, 5)))
    plt.ylabel("Percentage (%)")

    plt.legend()
    plt.show()


def plot_votes(data, log=False):
    # Number of Data Rows
    NUM_ROWS = len(data)

    # Number of Rounds (minus total votes and final game not eliminated)
    NUM_ROUNDS = len(data) - 2

    cm = plt.get_cmap('gist_rainbow')
    cNorm = colors.Normalize(vmin=0, vmax=NUM_ROWS)
    scalarMap = mplcm.ScalarMappable(norm=cNorm, cmap=cm)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_prop_cycle(color=[scalarMap.to_rgba(i) for i in range(NUM_ROWS)])

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

    plt.legend()
    plt.show()


def main():
    data = {}

    with open("ff_reddit_contest_data.csv", 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            # Ignore header line
            if line[0] == "Game":
                continue

            key = line[0]
            data[key] = []

            for cell in line[1:]:
                if cell == '':
                    break
                data[key].append(int(cell))

    plot_percentages(data)
    plot_votes(data)
    plot_votes(data, log=True)


if __name__ == "__main__":
    main()
