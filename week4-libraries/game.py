import random

# get level
while True:
    try:
        level = int(input("Level: "))
        if level < 0:
            pass
        else:
            answer = random.randint(1, level)
            break
    except ValueError:
        pass

# get guess
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < answer:
                print("Too small!")
            elif guess > answer:
                print("Too large!")
            else:
                exit("Just right!")
        else:
            pass
    except ValueError:
        pass
