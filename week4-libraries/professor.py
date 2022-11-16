import random

def main():
    # get level
    level = get_level()
    # initialize incorrect count
    incorrect_count = 0
    correct_count = 0
    # start the game
    for i in range(10):
        # generate integers
        x, y = generate_integer(level)
        # calculate correct answer
        answer = x + y
        # initialize guess count to 0
        guess_count = 0
        # afford 3 guesses
        while guess_count < 3:
            # get user answer
            user_answer = int(input(f"{x} + {y} = "))
            # check
            if user_answer != answer:
                print("EEE")
                guess_count += 1
                # if 3 incorrect guesses
                if guess_count == 3:
                    print(f"{x} + {y} = {answer}")
                    incorrect_count +=1
                    break
            else:
                correct_count += 1
                break

    print(f"Score: {correct_count}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                pass
            else:
                return level
        except ValueError:
            pass

def generate_integer(level):
    try:
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            return x, y
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
            return x, y
        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            return x, y
    except ValueError:
        exit("level is not 1, 2, or 3")

if __name__ == "__main__":
    main()