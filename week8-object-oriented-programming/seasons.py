from datetime import date
import inflect

p = inflect.engine()

def main():
    birthDate = input('Date of Birth: ')
    print(convert(birthDate))


def convert(s):
    try:
        s = date.fromisoformat(s)
    except ValueError:
        exit('Invalid date')

    today = date.today()
    minutes = (today-s).days * 24 * 60
    return f'{p.number_to_words(minutes, andword="").capitalize()} minutes'

if __name__ == "__main__":
    main()