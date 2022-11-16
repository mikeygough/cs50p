import csv
import sys


def main():
    # require file name
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 4:
        sys.exit("Too many command-line arguments")

    # read in before.csv
    names = read_csv(fname=sys.argv[1])
    # write to after.csv
    write_csv(names, sys.argv[2])


def read_csv(fname):
    # initialize empty list
    names = []
    # open file
    try:
        with open(f"{fname}", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                names.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    return names


def write_csv(input_file, output_file):
    with open(output_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for name in input_file:
            first_name = name['name'].split(",")[1].strip()
            last_name = name['name'].split(",")[0]
            writer.writerow({"first": first_name,
                             "last": last_name,
                             "house": name['house']})



if __name__ == "__main__":
    main()