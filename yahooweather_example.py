import pprint
import requests

def get_json_response(city, state):
    '''Gets forecast from yahoo's weather API in JSON format,
        city and state are taken as arguments to specify forecast location.
        '''
    url = ('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in'
               '%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{}%2C%20{}%22)&format=json&env=store'
               '%3A%2F%2Fdatatables.org%2Falltableswithkeys').format(city, state)
    response = requests.get(url)
    json_response = response.json()
    return json_response

def get_temp_forecast(json_response):
    '''Processes returned JSON from the get_json_response function for the short term temperature forecast.
        '''
    for item in json_response['query']['results']['channel']['item']['forecast']:
        print('The forecasted high and low for ' + item['date'] + ' is: ' + item['high'] + ' and '
              + item['low'] + ' deg F, respectively')

json_response = get_json_response(city='seattle', state='wa')
pprint.pprint(json_response)
get_temp_forecast(json_response)



