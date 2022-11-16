menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0.00
    while True:
        try:
            # get input
            user_input = input("Item: ").title()
            # add to total
            total += menu[user_input]
            # format
            formatted_total = "{:.2f}".format(total)
            print(f"Total: ${formatted_total}")
        except KeyError:
            pass
        except EOFError:
            return total

main()