def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    d1 = d.replace("$", "")
    return(float(d1))

def percent_to_float(p):
    # TODO
    p1 = p.replace("%", "")
    p1 = float(p1)
    return(p1 / 100.)

main()