import requests
import datetime

url = 'https://dashboard.elering.ee/api'
end_point = '/nps/price'

params = ['EE', 'LT', 'LV', 'FI', 'UK']

for country in params:

    response = requests.get(url + end_point + f'/{country}/current')
    data = response.json()
    if data.get('success'):
        print(country, data['data'][0]['price'], 'Time', datetime.datetime.fromtimestamp(data['data'][0]['timestamp']))
    else:
        print(country, 'NO DATA')
