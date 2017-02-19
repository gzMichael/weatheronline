#coding=utf-8
"""This weather API module of http://api.openweathermap.org/"""

import json
import datetime
import requests

KEY = 'e7928318b03c338d14082b636824e28c'

def convert_weather_code(argument):
    """Convert this API code to API_Thinkpage, so MainWindow can reuse the 
       pictures of API_Thinkpage.
    Args:
        A string of weather code, like '200'
    Returns:
        A string of weather code, like '16'
    """
    switcher = {
        #thunder
        '200': '16',
        '201': '16',
        '202': '16',
        '210': '16',
        '211': '16',
        '212': '16',
        '221': '16',
        '230': '16',
        '231': '16',
        '232': '16',
        #drizzle
        '300': '10',
        '301': '10',
        '302': '10',
        '310': '10',
        '311': '10',
        '312': '10',
        '313': '10',
        '314': '10',
        '321': '10',
        #rain
        '500': '13',
        '501': '14',
        '502': '15',
        '503': '15',
        '504': '15',
        '511': '20',
        '521': '10',
        '522': '14',
        '531': '15',
        #snow
        '600': '22',
        '601': '23',
        '602': '24',
        '611': '20',
        '612': '20',
        '615': '20',
        '616': '20',
        '620': '22',
        '621': '23',
        '622': '24',
        #atomosphere
        '701': '26',
        '711': '26',
        '721': '31',
        '731': '28',
        '741': '30',
        '751': '31',
        '761': '26',
        '762': '99',
        '771': '34',
        '781': '36',
        #clear
        '800': '0',
        #clouds
        '801': '5',
        '802': '5',
        '803': '7',
        '804': '4'
    }
    return switcher.get(argument, '99')

def get_weather_now(city_input):
    """Get realtime weather info from http://http://openweathermap.org/
    Args:
        city_input: The name of the city input by user.
    Returns:
        dict_weather_now:{
            "status_code": "200",
            "message": "ok",
            "name": city_name,
            "weather": "city_weather",
            "weather_code": "0",
            "temp": "city_temp"
        }
    API example:
        return 200
        {"coord":
        {"lon":145.77,"lat":-16.92},
        "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
        "base":"cmc stations",
        "main":{"temp":293.25,"pressure":1019,"humidity":83,"temp_min":289.82,"temp_max":295.37},
        "wind":{"speed":5.1,"deg":150},
        "clouds":{"all":75},
        "rain":{"3h":3},
        "dt":1435658272,
        "sys":{"type":1,"id":8166,"message":0.0166,"country":"AU",
                "sunrise":1435610796,"sunset":1435650870},
        "id":2172797,
        "name":"Cairns",
        "cod":200}
    """
    _dict_weather_now = {}
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q':city_input, 'units':'metric', 'lang':'zh_cn', 'appid':KEY}
    try:
        req = requests.get(url, params=params)
    except Exception as err:
        #print('I got the ConnectionError:', err)
        _dict_weather_now = {'status_code':'404', 'message':'无法连接服务器'}
        return _dict_weather_now
    if req.status_code == 200:
        j = json.loads(req.text)
        _dict_weather_now['status_code'] = '200'
        _dict_weather_now['message'] = 'ok'
        _dict_weather_now['name'] = j['name']
        _dict_weather_now['weather'] = j['weather'][0]['description']
        _dict_weather_now['temp'] = str("%2.f"%(j['main']['temp']))
        weather_code = str(j['weather'][0]['id'])
        _dict_weather_now['weather_code'] = convert_weather_code(weather_code)
    #req.status_code == 502
    else:
        _dict_weather_now = {'status_code':'502', 'message':'城市名称不存在'}
    return _dict_weather_now

def get_weather_forecast(city_input):
    """Get weather forecast from http://openweathermap.org/
    Args:
        city_input: The name of the city input by user.
    Returns:
        dict_weather_forecast:{
            "status_code": "200",
            "message": "ok",
            "name": city_name,
            "date_d0": date_d0,
            "weather_d0": city_weather_d0,
            "weather_code_d0": weather_code_d0,
            "temp_max_d0": temp_max_d0,
            "temp_min_d0": temp_min_d0,
            "date_d1": date_d1,
            "weather_d1": city_weather_d1,
            "weather_code_d1": weather_code_d1,
            "temp_max_d1": temp_max_d1,
            "temp_min_d1": temp_min_d1,
            "date_d2": date_d2,
            "weather_d2": city_weather_d2,
            "weather_code_d2": weather_code_d2,
            "temp_max_d2": temp_max_d2,
            "temp_min_d2": temp_min_d2
        }
    API: Weather forecast interface, return 3 days of weather information for free users.
    API example:
        url = 'http://api.openweathermap.org/data/2.5/forecast/daily'
        params = {'q':city_input, 'units':'metric', 'lang':'zh_cn', 'appid':KEY}
        req = requests.get(url, params=params)
        return 200
        {"cod":"200","message":0.0032,
        "city":{"id":1851632,"name":"Shuzenji",
        "coord":{"lon":138.933334,"lat":34.966671},
        "country":"JP"},
        "cnt":10,
        "list":[{
            "dt":1406080800,
            "temp":{
                "day":297.77,
                "min":293.52,
                "max":297.77,
                "night":293.52,
                "eve":297.77,
                "morn":297.77},
            "pressure":925.04,
            "humidity":76,
            "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],}
        ]}
    """
    _dict_weather_forecast = {}
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily'
    params = {'q':city_input, 'units':'metric', 'lang':'zh_cn', 'appid':KEY}
    try:
        req = requests.get(url, params=params)
    except Exception as err:
        #print('I got ConnectionError:', err)
        _dict_weather_forecast = {'status_code':'404', 'message':'无法连接服务器'}
        return _dict_weather_forecast
    if req.status_code == 200:
        j = json.loads(req.text)
        _dict_weather_forecast['status_code'] = '200'
        _dict_weather_forecast['message'] = 'ok'
        #Today
        timestamp = j['list'][0]['dt']
        date_now = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
        _dict_weather_forecast['date_d0'] = date_now
        _dict_weather_forecast['weather_d0'] = j['list'][0]['weather'][0]['description']
        _dict_weather_forecast['temp_max_d0'] = str("%2.f"%(j['list'][0]['temp']['max']))
        _dict_weather_forecast['temp_min_d0'] = str("%2.f"%(j['list'][0]['temp']['min']))
        weather_code = str(j['list'][0]['weather'][0]['id'])
        _dict_weather_forecast['weather_code_d0'] = convert_weather_code(weather_code)
        #Tomorrow
        timestamp = j['list'][1]['dt']
        date_now = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
        _dict_weather_forecast['date_d1'] = date_now
        _dict_weather_forecast['weather_d1'] = j['list'][1]['weather'][0]['description']
        _dict_weather_forecast['temp_max_d1'] = str("%2.f"%(j['list'][1]['temp']['max']))
        _dict_weather_forecast['temp_min_d1'] = str("%2.f"%(j['list'][1]['temp']['min']))
        weather_code = str(j['list'][1]['weather'][0]['id'])
        _dict_weather_forecast['weather_code_d1'] = convert_weather_code(weather_code)
        #The day after tomorrow
        timestamp = j['list'][2]['dt']
        date_now = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
        _dict_weather_forecast['date_d2'] = date_now
        _dict_weather_forecast['weather_d2'] = j['list'][2]['weather'][0]['description']
        _dict_weather_forecast['temp_max_d2'] = str("%2.f"%(j['list'][2]['temp']['max']))
        _dict_weather_forecast['temp_min_d2'] = str("%2.f"%(j['list'][2]['temp']['min']))
        weather_code = str(j['list'][2]['weather'][0]['id'])
        _dict_weather_forecast['weather_code_d2'] = convert_weather_code(weather_code)
    #req.status_code == 502
    else:
        _dict_weather_forecast = {'status_code':'502', 'message':'城市名称不存在'}
    return _dict_weather_forecast
