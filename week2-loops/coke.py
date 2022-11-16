def main():
    amount_due = 50
    amount_due = get_coin(amount_due)
    print("Change Owed: ", 0-amount_due)

def get_coin(due):
    while True:
        if due > 0:
            print("Amount Due: ", due)
            coin = int(input("Insert Coin: "))
            if coin == 25 or coin == 10 or coin == 5:
                due -= coin
            else:
                pass
        else:
            break
    return due

main()

