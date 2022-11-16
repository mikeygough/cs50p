def main():
    num, denom = get_fuel()
    print(calc_fuel(num, denom))

def get_fuel():
    while True:
        # get input
        user_input = input("Fuel: ")
        try:
            # separate numerator and denominator
            num = int(user_input.split("/")[0])
            denom = int(user_input.split("/")[1])

            # check input
            if denom == 0:
                pass
            elif num > denom:
                pass
            else:
                return num, denom
        except (ValueError, ZeroDivisionError):
            pass


def calc_fuel(x, y):
    # calculate fraction
    frac = int(round(float(x) / float(y), 2) * 100)

    # format output
    if frac <= 1:
        return "E"
    elif frac >= 99:
        return "F"
    else:
        return str(frac) + "%"


main()