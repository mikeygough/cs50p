def main():
    grocery_list = add_items()
    print_grocery(grocery_list)


def add_items():
    grocery_list = {}
    while True:
        try:
            # get input
            user_input = input().upper()
            # if exists, +1 quantity
            if user_input in grocery_list:
                grocery_list[user_input] += 1
            # else add item
            else:
                grocery_list[user_input] = 1
        except EOFError:
            return grocery_list


def print_grocery(grocery_list):
    for k, v in sorted(grocery_list.items()):
        print(v, k)


main()