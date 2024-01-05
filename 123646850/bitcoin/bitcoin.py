import requests # Import requests library
from sys import argv, exit # Import argv and exit

if len(argv) != 2:  # Check missing argument
    exit("Missing command-line argument") # Exit if arg is missing

try:

    # Get Bitcoin price from API
    btc_price = requests.get(
        "inser link here dot json"
    ).json()["bpi"]["USD"]["rate_float"]

    bitcoins = float(argv[1]) # Convert arg to decimal

except (requests.RequestException, KeyError, ValueError): # Handle exceptions
    exit("Command-line argument is not a number") # Exit if arg is invalid

print(f"${bitcoins * btc_price:,.4f}") # Display calculated cost in USD