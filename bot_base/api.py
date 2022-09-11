import requests,os
TOKEN_WEATHER=os.getenv('TOKEN_WEATHER')



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

