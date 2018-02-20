import pprint
import requests

def get_json_response(base):
    '''Gets data in JSON format for the exchange rates of common currencies compared to the base currency,
     which is taken as an argument(i.e base=USD).
    '''
    url = 'https://api.fixer.io/latest?base={}'.format(base)
    json_response = requests.get(url).json()
    return json_response

def get_exchange(json_response):
    '''Processes the returned JSON of get_json_response function and prints exchange rates for the given base
    currency.
    '''
    print('The exchange rate for 1 ' + json_response['base'] + ' is: ' + '\n')
    for key in json_response['rates']:
        print(str(json_response['rates'][key]) + ' ' + key)

json_response = get_json_response(base='USD')
pprint.pprint(json_response)
get_exchange(json_response)


