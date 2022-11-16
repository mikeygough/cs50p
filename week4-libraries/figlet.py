import sys
from pyfiglet import Figlet
import random

# get list of fonts
figlet = Figlet()
fontList = figlet.getFonts()

# check command line arguments
if len(sys.argv) == 3:
    # specific font?
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        # font available?
        if sys.argv[2] in fontList:
            try:
                input = input("Input: ")
                font = sys.argv[2]
                f = Figlet(font=font)
                print(f.renderText(input))
            except IndexError:
                pass
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
# random font
elif len(sys.argv) == 1:
    randomFont = random.choice(fontList)
    input = input("Input: ")
    f = Figlet(font=randomFont)
    print(f.renderText(input))
# invalid use
else:
    sys.exit("Invalid usage")