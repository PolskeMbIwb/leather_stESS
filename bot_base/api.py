import requests,os
# TOKEN_WEATHER=os.getenv('TOKEN_WEATHER')
TOKEN_WEATHER='18c029b1-f55c-4c20-8b3e-bbf0636c08ef'


#lat-широта, lon-долгота
def get_weather_from_api(lat,lon):

    url='https://api.weather.yandex.ru/v2/informers?'
    params={
        'lat':lat,
        'lon':lon,
        'lang':'ru_RU'
    }

    header={
        'X-Yandex-API-Key':TOKEN_WEATHER
    }
    result=requests.get(url,params=params,headers=header)
    return result.json()

