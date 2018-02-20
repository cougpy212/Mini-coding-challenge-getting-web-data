import pprint
import requests

def get_json_response(woeid):
    '''Gets forecast from metaweather.com in JSON format,
    whereonearthid is taken as an argument to specify forecast location.
    '''
    url = 'https://www.metaweather.com/api/location/{}'.format(woeid)
    response = requests.get(url)
    json_response = response.json()
    return json_response

def get_temp(json_response):
    '''Processes returned JSON from the get_json_response function for the short term temperature forecast.
    '''
    for item in json_response['consolidated_weather']:
        print('The forecast for ' + item['applicable_date'] + ' is: ' + str(item['the_temp']) + ' deg C')

json_response = get_json_response(woeid=2490383)
pprint.pprint(json_response)
get_temp(json_response)





