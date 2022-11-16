def main():
    user_input = input("Input: ")
    print(shorten(user_input))


def shorten(word):
    vowels = ['a','e','i','o','u']
    output = ""
    for w in word:
        if w.lower() not in vowels:
            output += w
        else:
            pass
    return output


if __name__ == "__main__":
    main()