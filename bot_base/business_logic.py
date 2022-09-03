from api import get_weather_from_api



def parse_weather(metro):

    metro_dict = {
        'некрасовка':[55.704119,37.929819],
        'таганская':[55.742403,37.653445],
        'курская':[55.757976,37.660761]
    }

    if str(metro).lower() in metro_dict.keys():
        weather=get_weather_from_api(metro_dict[f'{metro}'][0],metro_dict[f'{metro}'][1])
        temp=weather['fact']['temp']
        wind_speed=weather['fact']['wind_speed']
        pressure_mm=weather['fact']['pressure_mm']
        messages=f'Погода у метро "{metro}"\n температура воздуха: {temp},\n скорость ветра: {wind_speed}м/с,\n давление: {pressure_mm}'
        return messages
    else:
        list_metro=list(metro_dict.keys())
        messages = f'Метро нет в перечне,\n список метро:{list_metro}'
        return messages

