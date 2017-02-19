#coding=utf-8
"""This weather API module of http://api.thinkpage.cn/"""

import json
import requests

KEY = 'cdvqctjafbrlflqo'    #API key of thinkpage.cn
def get_weather_now(city_input):
    """Get realtime weather info from http://api.thinkpage.cn/
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
    API: Return three parameters (city name, weather and temperature) for free users only.
    API example:
        https://api.thinkpage.cn/v3/weather/now.json?key=KEY&location=beijing&language=zh-Hans&unit=c
        return 200
        {
          "results": [{
          "location": {
              "id": "C23NB62W20TF",
              "name": "西雅图",
              "country": "US",
              "timezone": "America/Los_Angeles",
              "timezone_offset": "-07:00"
          },
          "now": {
              "text": "多云", //天气现象文字
              "code": "4", //天气现象代码
              "temperature": "14", //温度，单位为c摄氏度或f华氏度
              "feels_like": "14", //体感温度，单位为c摄氏度或f华氏度
              "pressure": "1018", //气压，单位为mb百帕或in英寸
              "humidity": "76", //相对湿度，0~100，单位为百分比
              "visibility": "16.09", //能见度，单位为km公里或mi英里
              "wind_direction": "西北", //风向文字
              "wind_direction_degree": "340", //风向角度，范围0~360，0为正北，90为正东，180为正南，270为正西
              "wind_speed": "8.05", //风速，单位为km/h公里每小时或mph英里每小时
              "wind_scale": "2", //风力等级，请参考：http://baike.baidu.com/view/465076.htm
              "clouds": "90", //云量，范围0~100，天空被云覆盖的百分比 #目前不支持中国城市#
              "dew_point": "-12" //露点温度，请参考：http://baike.baidu.com/view/118348.htm #目前不支持中国城市#
          },
          "last_update": "2015-09-25T22:45:00-07:00" //数据更新时间（该城市的本地时间）
          }]
        }
    """
    _dict_weather_now = {}
    url = 'https://api.thinkpage.cn/v3/weather/now.json'
    params = {'key':KEY, 'location':city_input, 'language':'zh-Hans', 'unit':'c'}
    try:
        req = requests.get(url, params=params)
    except Exception as err:
        #print(err)
        _dict_weather_now = {'status_code':'404', 'message':'无法连接服务器'}
        return _dict_weather_now
    if req.status_code == 200:
        j = json.loads(req.text)
        _dict_weather_now['status_code'] = '200'
        _dict_weather_now['message'] = 'ok'
        _dict_weather_now['name'] = j['results'][0]['location']['name']
        _dict_weather_now['weather'] = j['results'][0]['now']['text']
        _dict_weather_now['temp'] = j['results'][0]['now']['temperature']
        _dict_weather_now['weather_code'] = j['results'][0]['now']['code']
    #req.status_code == 502
    else:
        _dict_weather_now = {'status_code':'502', 'message':'城市名称不存在', 'name':city_input}
    return _dict_weather_now

def get_weather_forecast(city_input):
    """Get weather forecast from http://api.thinkpage.cn/
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
    API: Return 3 days of weather information for free users.
    API example:
        https://api.thinkpage.cn/v3/weather/daily.json?key=KEY&location=beijing&language=zh-Hans&unit=c
        return 200
        {
          "results": [{
            "location": {
              "id": "WX4FBXXFKE4F",
              "name": "北京",
              "country": "CN",
              "path": "北京,北京,中国",
              "timezone": "Asia/Shanghai",
              "timezone_offset": "+08:00"
            },
            "daily": [{                         //返回指定days天数的结果
              "date": "2015-09-20",             //日期
              "text_day": "多云",               //白天天气现象文字
              "code_day": "4",                  //白天天气现象代码
              "text_night": "晴",               //晚间天气现象文字
              "code_night": "0",                //晚间天气现象代码
              "high": "26",                     //当天最高温度
              "low": "17",                      //当天最低温度
              "precip": "0",                    //降水概率，范围0~100，单位百分比
              "wind_direction": "",             //风向文字
              "wind_direction_degree": "255",   //风向角度，范围0~360
              "wind_speed": "9.66",             //风速，单位km/h（当unit=c时）、mph（当unit=f时）
              "wind_scale": ""                  //风力等级
            }, {
              "date": "2015-09-21",
              "text_day": "晴",
              "code_day": "0",
              "text_night": "晴",
              "code_night": "0",
              "high": "27",
              "low": "17",
              "precip": "0",
              "wind_direction": "",
              "wind_direction_degree": "157",
              "wind_speed": "17.7",
              "wind_scale": "3"
            }, {
              ...                               //更多返回结果
            }],
            "last_update": "2015-09-20T18:00:00+08:00" //数据更新时间（该城市的本地时间）
          }]
        }
    """
    _dict_weather_forecast = {}
    url = 'https://api.thinkpage.cn/v3/weather/daily.json'
    params = {'key':KEY,
              'location':city_input,
              'language':'zh-Hans',
              'unit':'c', 'start':'0',
              'days':'3'}
    try:
        req = requests.get(url, params=params)
    except Exception as err:
        #print(err)
        _dict_weather_forecast = {'status_code':'404', 'message':'无法连接服务器'}
        return _dict_weather_forecast
    if req.status_code == 200:
        j = json.loads(req.text)
        _dict_weather_forecast['status_code'] = '200'
        _dict_weather_forecast['message'] = 'ok'
        _dict_weather_forecast['name'] = j['results'][0]['location']['name']
        #Today
        _dict_weather_forecast['date_d0'] = j['results'][0]['daily'][0]['date']
        _dict_weather_forecast['weather_d0'] = j['results'][0]['daily'][0]['text_day']
        _dict_weather_forecast['temp_max_d0'] = j['results'][0]['daily'][0]['high']
        _dict_weather_forecast['temp_min_d0'] = j['results'][0]['daily'][0]['low']
        _dict_weather_forecast['weather_code_d0'] = j['results'][0]['daily'][0]['code_day']
        #Tomorrow
        _dict_weather_forecast['date_d1'] = j['results'][0]['daily'][1]['date']
        _dict_weather_forecast['weather_d1'] = j['results'][0]['daily'][1]['text_day']
        _dict_weather_forecast['temp_max_d1'] = j['results'][0]['daily'][1]['high']
        _dict_weather_forecast['temp_min_d1'] = j['results'][0]['daily'][1]['low']
        _dict_weather_forecast['weather_code_d1'] = j['results'][0]['daily'][1]['code_day']
        #The day after tomorrow
        _dict_weather_forecast['date_d2'] = j['results'][0]['daily'][2]['date']
        _dict_weather_forecast['weather_d2'] = j['results'][0]['daily'][2]['text_day']
        _dict_weather_forecast['temp_max_d2'] = j['results'][0]['daily'][2]['high']
        _dict_weather_forecast['temp_min_d2'] = j['results'][0]['daily'][2]['low']
        _dict_weather_forecast['weather_code_d2'] = j['results'][0]['daily'][2]['code_day']
    #req.status_code == 502
    else:
        _dict_weather_forecast = {'status_code':'502', 'message':'城市名称不存在', 'name':city_input}
    return _dict_weather_forecast
