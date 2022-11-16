months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    month, day, year = get_date()
    format(month, day, year)


def get_date():
    while True:
        try:
            # get input
            user_input = input("Date: ")
            # if format xx/xx/xxxx
            if len(user_input) <= 10:
                if int(user_input.split("/")[0]) <= 12 and int(user_input.split("/")[1]) <= 31:
                    month = int(user_input.split("/")[0])
                    day = int(user_input.split("/")[1])
                    year = int(user_input.split("/")[2])
                    return month, day, year
                else:
                    pass
            # if format September 8, 1636 (textual)
            else:
                if user_input.split(" ")[0].capitalize() in months and int(user_input.split(" ")[1][:-1]) <= 31:
                    month = user_input.split(" ")[0]
                    day = int(user_input.split(" ")[1][:-1])
                    year = int(user_input.split(" ")[2])
                    return month, day, year
                else:
                    pass
        except (ValueError, TypeError):
            pass

def format(month, day, year):
    # if format xx/xx/xxxx
    if type(month) == int and type(day) == int and type(year) == int:
        day_fmt = str(day).zfill(2)
        month_fmt = str(month).zfill(2)
        print(f"{year}-{month_fmt}-{day_fmt}")
    # if format September 8, 1636 (textual)
    else:
        month_fmt = str(months.index(month) + 1).zfill(2)
        day_fmt = str(day).zfill(2)
        print(f"{year}-{month_fmt}-{day_fmt}")


main()