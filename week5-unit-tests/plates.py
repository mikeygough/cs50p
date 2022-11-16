def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    req_1 = True
    req_2 = True
    req_3 = True
    req_4 = True

    # req_1
    ''' “All vanity plates must start with at least two letters.” '''
    if len(s) < 2:
        req_1 = False
    elif s[0].isnumeric() or s[1].isnumeric():
        req_1 = False
    else:
        pass

    # req_2
    ''' “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.” '''
    if len(s) < 2 or len(s) > 6:
        req_2 = False
    else:
        pass

    # req_3
    ''' “Numbers cannot be used in the middle of a plate; they must come at the end.
    For example, AAA222 would be an acceptable … vanity plate; AAA22A / CS50P2 would not be acceptable.
    The first number used cannot be a 0.” '''
    # digit then letter then digit
    for _ in range(1, len(s)-1):
        if s[_ - 1].isalpha() and s[_].isdigit() and s[_ + 1].isalpha():
            req_3 = False
        elif s[_].isdigit() and s[_ + 1].isalpha():
            req_3 = False
    # 0 is the first number
    if '0' in s and s[s.find('0') - 1].isalpha():
        req_3 = False
    else:
        pass

    # req_4
    ''' “No periods, spaces, or punctuation marks are allowed.” '''
    if s.isalnum():
        pass
    else:
        req_4 = False

    if req_1 and req_2 and req_3 and req_4:
        return True
    else:
        return False


if __name__ == "__main__":
    main()