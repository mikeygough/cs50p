def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # print("r1", req_1(s))
    # print("r2", req_2(s))
    # print("r3", req_3(s))
    # print("r4", req_4(s))
    if req_1(s) and req_2(s) and req_3(s) and req_4(s):
        return True
    else:
        return False

def req_1(s):
    ''' “All vanity plates must start with at least two letters.” '''
    if len(s) < 2:
        return False
    elif s[0].isnumeric() or s[1].isnumeric():
        return False
    else:
        return True

def req_2(s):
    ''' “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.” '''
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        return True

def req_3(s):
    ''' “Numbers cannot be used in the middle of a plate; they must come at the end.
    For example, AAA222 would be an acceptable … vanity plate; AAA22A / CS50P2 would not be acceptable.
    The first number used cannot be a 0.” '''
    # digit then letter then digit
    for _ in range(1, len(s)-1):
        if s[_ - 1].isalpha() and s[_].isdigit() and s[_ + 1].isalpha():
            return False
        elif s[_].isdigit() and s[_ + 1].isalpha():
            return False
    # 0 is the first number
    if '0' in s and s[s.find('0') - 1].isalpha():
        return False
    else:
        return True

def req_4(s):
    ''' “No periods, spaces, or punctuation marks are allowed.” '''
    if s.isalnum():
        return True
    else:
        return False

main()