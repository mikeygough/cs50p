import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    check_sum = 0
    for _ in ip.split("."):
        try:
            if int(_) >= 0 and int(_) <= 255:
                check_sum += 1
        except ValueError:
            break
    if check_sum == 4:
        return True
    else:
        return False


if __name__ == "__main__":
    main()