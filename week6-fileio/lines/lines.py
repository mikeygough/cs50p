import sys

def main():
    # require file name
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # require python file
    elif sys.argv[1][-3:] != ".py":
        sys.exit("Not a python file")

    # assign file_name
    file_name = sys.argv[1]
    # return lines
    lines = read_file(file_name)
    print(calculate_lines(lines))

def read_file(fname):
    try:
        with open(f"{fname}", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

def calculate_lines(lines):
    line_count = 0
    for line in lines:
        # check for comments
        if line.lstrip().startswith(("#")):
            pass
        # check for blank lines
        elif line.isspace():
            pass
        # increment line count
        else:
            line_count += 1
    return line_count


if __name__ == "__main__":
    main()