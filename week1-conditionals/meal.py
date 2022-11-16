def main():
    user_time = input("What time is it? ")
    converted_time = convert(user_time)
    if converted_time >= 7 and converted_time <= 8:
        print("breakfast time")
    elif converted_time >= 12 and converted_time <= 13:
        print("lunch time")
    elif converted_time > 18 and converted_time <= 19:
        print("dinner time")

def convert(time):
    hours = float(time.split(":")[0])
    minutes = float(time.split(":")[1])
    # convert to hourly
    minutes = minutes / 60
    time = hours + minutes
    return time

if __name__ == "__main__":
    main()