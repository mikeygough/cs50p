import re
import sys


def main():
    # get user input
    print(parse(input("HTML: ")))


def parse(s):
    # match
    if matches := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/(\w*)', s, re.IGNORECASE):
        # concat with shortened youtube link
        return "https://youtu.be/" + matches.group(1)


if __name__ == "__main__":
    main()