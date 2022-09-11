from api import get_weather_from_api
import json
from threading import Timer
from time import sleep


metro_dict = {
        'некрасовка':[55.704119,37.929819],
        'таганская':[55.742403,37.653445],
        'курская':[55.757976,37.660761]
    }

def parse_weather(metro:str):


    if str(metro).lower() in metro_dict.keys():
        # weather=get_weather_from_api(metro_dict[f'{metro}'][0],metro_dict[f'{metro}'][1])
        weather = get_weather_from_cach(metro)
        temp=weather[0]['temp']
        wind_speed=weather[0]['wind_speed']
        pressure_mm=weather[0]['pressure_mm']
        messages=f'Погода у метро "{metro}"\n температура воздуха: {temp},\n скорость ветра: {wind_speed}м/с,\n давление: {pressure_mm}'
        return messages
    else:
        list_metro=list(metro_dict.keys())
        messages = f'Метро нет в перечне,\n список метро:{list_metro}'
        return messages


def get_weather_from_cach(station:str):
    with open('cach.json','r') as f:
        data = json.load(f)
    return data[f'{station}']


def update_cach():
    for metr in metro_dict:
        weather = get_weather_from_api(metro_dict[f'{metr}'][0],metro_dict[f'{metr}'][1])
        with open('cach.json','r', encoding = "utf-8") as f:
            data=json.load(f)
            data[f'{metr}'][0]['temp']=weather['fact']['temp']
            data[f'{metr}'][0]['wind_speed']=weather['fact']['wind_speed']
            data[f'{metr}'][0]['pressure_mm']=weather['fact']['pressure_mm']
        with open('cach.json','wt') as f:
            json.dump(data,f,ensure_ascii=False, indent=4)
    return

while 1:
    timer = Timer(interval=1,function=update_cach)
    sleep(5400)
    timer.start()
