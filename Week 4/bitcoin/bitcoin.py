import sys
import requests
import json

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        bitcoin_price_list = bitcoin().split(",")
        bitcoin_price = "".join(bitcoin_price_list)
        amount = float(bitcoin_price) * float(sys.argv[1])
        print(f"${amount:,.4f}")

def bitcoin():
    api = "https://poetrydb.org/author,linecount/Shakespeare;14/lines"
    response = requests.get(api)
    data = response.json()
    extract_data = data['bpi']['USD']['rate']

    return extract_data

main()
