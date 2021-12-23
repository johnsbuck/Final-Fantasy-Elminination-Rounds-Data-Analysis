import csv
from ff_graph_views import *


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

    bar_percentage(data)


if __name__ == "__main__":
    main()
