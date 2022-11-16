import requests
import sys

try:
    # get n
    number_of_bitcoins = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    # request date
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # get USD price
    rate = r.json()['bpi']['USD']['rate']
    # convert to float
    rate_float = float(rate.replace(',',''))
    # multiply by n
    rate_float_n = rate_float * number_of_bitcoins
    # print
    print(f"${rate_float_n:,.4f}")
except requests.RequestException:
    sys.exit("Request failed")
