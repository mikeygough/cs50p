input = input("Input: ")
output = ""
vowels = ['a','e','i','o','u']
for i in input:
    if i.lower() not in vowels:
        output += i
    else:
        pass
print(output)