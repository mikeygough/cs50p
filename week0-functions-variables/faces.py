def convert(input):
    # replace smilies
    input = input.replace(":)", "🙂")
    # replace frownies
    input = input.replace(":(", "🙁")
    return(input)

def main():
    # get input
    user_input = input("What's your string? ")
    # convert
    user_input = convert(user_input)
    # print
    print(user_input)

main()