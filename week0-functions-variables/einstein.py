def calculate(m, c=300000000):
    return(m*c**2)

def main():
    user_m = int(input("m: "))
    e = calculate(m=user_m)
    print(e)

main()