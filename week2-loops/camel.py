input = input("camelCase: ")
new_string = ""
for i in input:
    if i.isupper():
        new_string += "_"
        new_string += i.lower()
    else:
        new_string += i.lower()
print(new_string)
