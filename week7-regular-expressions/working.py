import re
import sys

# assume that AM or PM will be capitalized (with no periods therein) and that there will be a space before each
# 9:00 AM to 5:00 PM
# 9 AM to 5 PM


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # initialize empty dictionary
    timeDict = {"AM": {"Hour": None, "Minute": None,},
                "PM": {"Hour": None, "Minute": None,}
                }

    # match
    # try:
        # first number 0-9, then AM/PM, then number 0-9, then AM/PM
    if matches := re.search(r'([0-9:*]*) ([AM|PM]+) to ([0-9:*]*) ([AM|PM]+)', s, re.IGNORECASE):
        mOne = matches.group(1)
        mTwo = matches.group(2)
        mThree = matches.group(3)
        mFour = matches.group(4)
    else:
        raise ValueError("Invalid input format. Try 9:00 AM to 5:00 PM or 9 AM to 5 PM")

    # except ValueError:
    #     exit("Invalid input format. Try 9:00 AM to 5:00 PM or 9 AM to 5 PM")

    # debug
    # print(mOne)
    # print(mTwo)
    # print(mThree)
    # print(mFour)

    # add values to Dict
    if mTwo == 'AM' and mFour == 'PM':
        timeDict['AM']['Hour'] = int(mOne.split(':')[0])
        try:
            timeDict['AM']['Minute'] = int(mOne.split(':')[1])
        except IndexError:
            timeDict['AM']['Minute'] = 0

        timeDict['PM']['Hour'] = int(mThree.split(':')[0])
        try:
            timeDict['PM']['Minute'] = int(mThree.split(':')[1])
        except IndexError:
            timeDict['PM']['Minute'] = 0

    elif mTwo == 'PM' and mFour == 'AM':
        timeDict['PM']['Hour'] = int(mOne.split(':')[0])
        try:
            timeDict['PM']['Minute'] = int(mOne.split(':')[1])
        except IndexError:
            timeDict['PM']['Minute'] = 0

        timeDict['AM']['Hour'] = int(mThree.split(':')[0])
        try:
            timeDict['AM']['Minute'] = int(mThree.split(':')[1])
        except IndexError:
            timeDict['AM']['Minute'] = 0

    # debug
    # print(timeDict)

    # check for ValueErrors
    for _ in timeDict:
        if timeDict[_]['Hour'] < 0 or timeDict[_]['Hour'] > 12:
            raise ValueError("Invalid Time")
        elif timeDict[_]['Minute'] < 0 or timeDict[_]['Minute'] > 59:
            raise ValueError("Invalid Time")

    # print(timeDict)
    if timeDict['AM']['Hour'] >= 12:
        newAmHour = f"{(timeDict['AM']['Hour'] % 12):02}"
    else:
        newAmHour = f"{timeDict['AM']['Hour']:02}"
    newAmMin = f"{timeDict['AM']['Minute']:02}"

    if timeDict['PM']['Hour'] < 12:
        newPmHour = f"{(timeDict['PM']['Hour'] + 12):02}"
    else:
        newPmHour = f"{timeDict['PM']['Hour']:02}"
    newPmMin = f"{timeDict['PM']['Minute']:02}"

    if mTwo == "AM":
        return f'{newAmHour}:{newAmMin} to {newPmHour}:{newPmMin}'
    elif mTwo == "PM":
        return f'{newPmHour}:{newPmMin} to {newAmHour}:{newAmMin}'


if __name__ == "__main__":
    main()

# working.py converts "12 AM to 12 PM" to "00:00 to 12:00"
# 5 PM -> 17:00
# 10 PM -> 22:00