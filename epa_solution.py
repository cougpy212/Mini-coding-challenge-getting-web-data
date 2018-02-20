import pprint
import requests

def get_json_response(zipcode):
    '''Gets UV index forecast information in JSON format for a specific location from epa.gov's API.
    Zipcode is taken as an argument.
    '''
    url = 'https://iaspub.epa.gov/enviro/efservice/getEnvirofactsUVHOURLY/ZIP/{}/JSON'.format(zipcode)
    json_response = requests.get(url).json()
    return(json_response)

def get_UV_prediction(json_response):
    '''Processes returned JSON of get_json_response function to obtain the UV index and corresponding date time value
    of the forecast.
    '''
    for item in json_response:
        print('The UV index prediction for ' + item['DATE_TIME'] + ' is ' + str(item['UV_VALUE']))

json_response = get_json_response(zipcode=99163)
pprint.pprint(json_response)
get_UV_prediction(json_response)





