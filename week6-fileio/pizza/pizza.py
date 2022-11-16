import csv
import sys
from tabulate import tabulate

def main():
    # require file name
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # require csv file
    elif sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")

    menu = read_csv(fname=sys.argv[1])
    print(tabulate(menu, headers="keys", tablefmt="grid"))


def read_csv(fname):
    # initialize empty list
    menu = []
    # open file
    try:
        with open(f"{fname}", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    return menu


if __name__ == "__main__":
    main()