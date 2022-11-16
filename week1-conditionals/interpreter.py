input = input("Expression: ")
x = float(input.split(" ")[0])
y = input.split(" ")[1]
z = float(input.split(" ")[2])

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)