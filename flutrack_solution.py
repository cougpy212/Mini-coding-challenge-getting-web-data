import pprint
import requests

def get_json_response(days):
    '''Gets information about cases of flu detected by flutrack.org's API in JSON format. Days is taken as an argument
    and allows the user to specify how many days back in history they wan to obtain this information for.
    '''
    url = 'http://api.flutrack.org/?time={}'.format(days)
    json_response = requests.get(url).json()
    return(json_response)

def get_coordinates(json_response):
    '''Processes returned JSON of get_json_response function to obtain username and location data.
    '''
    for item in json_response:
        print('user ' + item['user_name'] + '\'s location is: ' + '\n'
              + item['latitude'] + ' latitude' + '\n'
              + item['longitude'] + ' longitude' + '\n\n')

json_response = get_json_response(days=1)
pprint.pprint(json_response)
get_coordinates(json_response)
