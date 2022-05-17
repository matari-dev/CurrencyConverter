import requests
import json


def get_rates(currency):
    url = f'http://www.floatrates.com/daily/{currency}.json'
    r = requests.get(url)
    json_str = r.text
    rates = json.loads(json_str)
    return rates


def check_cache(desired_cur, cache_currency):
    print("Checking the cache...")
    found = desired_cur in cache_currency
    if found:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        cache_currency[desired_cur] = get_rates(desired_cur)


# create empty dictionary to be your
# cache of currencies
cache_currency = dict()

# prime dictionary with USD & EUR
cache_currency['usd'] = get_rates('usd')
cache_currency['eur'] = get_rates('eur')


# get user input
my_cur = input().lower()

while True:
    desired_cur = input().lower()
    if desired_cur == '':
        break
    monetary_amt = float(input())

    # check if in cache_currency dictionary
    check_cache(desired_cur, cache_currency)
    # do the conversion and
    # return result
    desired_rate = cache_currency[desired_cur][my_cur]['inverseRate']
    converted_amt = round(monetary_amt * desired_rate, 2)
    print(f'You received {converted_amt} {desired_cur.upper()}')
