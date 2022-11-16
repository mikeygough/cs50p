def main():
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
            elif num < 0 or denom < 0:
                pass
            else:
                break
        except (ValueError, ZeroDivisionError):
            pass

    fraction = convert(user_input)
    fuel = gauge(fraction)
    print(fuel)

def convert(fraction):
    try:
        num = int(fraction.split("/")[0])
        denom = int(fraction.split("/")[1])
    except (ValueError, ZeroDivisionError):
            exit()

    return int((num / denom) * 100)


def gauge(percentage):
    # format output
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()