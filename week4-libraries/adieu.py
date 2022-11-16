import inflect

p = inflect.engine()

# initialize empty list
names = []
while True:
    try:
        # get names
        user_input = input()
        names.append(user_input)
    except EOFError:
            break

# join
myNames = p.join((names))
# print
print(f"Adieu, adieu, to {myNames}")