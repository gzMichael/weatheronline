# -*- coding: utf-8 -*-
import datetime
from app import app
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from app.myipquery import locationquery
from app.models import History
from app import db
from app import api_thinkpage as api_tp
from app import api_openweathermap as api_owm 

class QueryForm(FlaskForm):
    city_name = StringField('需要查询天气的城市名称', validators=[DataRequired()])
    temp_unit = SelectField('温度单位', choices=[('1','℃'),('2','℉')])
    submit = SubmitField('查询')
    
def check_zh_or_en(check_str):
    for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
    return False
    
def convert_c_to_f(str1):
        """Convert Celsius to Fahrenheit
        Args:
            A Celsius temperature in string
        Returns:
            A Fahrenheit temperature in string
        """
        temp1 = float(str1) * 1.8 +32
        str2 = str("%2.f"%temp1)
        print(str1,str2)
        return str2
       
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    ip_str = request.remote_addr
    province_str, city_str = locationquery(ip_str)
    location_str = province_str + city_str
    dict_weather = {}
    queryform = QueryForm()
    if queryform.city_name.data:
        city_name = queryform.city_name.data
        temp_unit = queryform.temp_unit.data
        #根据是否输入中文，调用不同的接口
        if check_zh_or_en(city_name):
            dict_weather = api_tp.get_weather_forecast(city_name)
            api_str = '心知天气'
        else:
            dict_weather = api_owm.get_weather_forecast(city_name)
            api_str = 'OpenWeatherMap'
        #如果接口有数据返回
        if dict_weather:
            if dict_weather['status_code'] == '200':
                history = History()
                history.cityname = city_name
                history.ip = ip_str
                dt = datetime.datetime.now()
                history.time = dt.strftime("%Y-%m-%d %H:%M:%S")
                print(dt.strftime("%Y-%m-%d %H:%M:%S"))
                history.location = location_str
                history.api = api_str
                history.weather = dict_weather['weather_d0']
                history.weathercode = dict_weather['weather_code_d0']
                history.tempmin = dict_weather['temp_min_d0']
                history.tempmax = dict_weather['temp_max_d0']
                db.session.add(history)
                db.session.commit()
                if temp_unit == '2':
                    print(dict_weather['temp_min_d0'])
                    a = dict_weather['temp_min_d0']
                    dict_weather['temp_min_d0'] = convert_c_to_f(dict_weather['temp_min_d0'])
                    print(dict_weather['temp_min_d0'])
                    b = dict_weather['temp_min_d0']
                    dict_weather['temp_max_d0'] = convert_c_to_f(dict_weather['temp_max_d0'])
                    dict_weather['temp_min_d1'] = convert_c_to_f(dict_weather['temp_min_d1'])
                    dict_weather['temp_max_d1'] = convert_c_to_f(dict_weather['temp_max_d1'])
                    dict_weather['temp_min_d2'] = convert_c_to_f(dict_weather['temp_min_d2'])
                    dict_weather['temp_max_d2'] = convert_c_to_f(dict_weather['temp_max_d2'])
                    temp_unit_str = '℉'
                else:
                    temp_unit_str = '℃'
        return render_template('index.html', form=queryform, city_name=city_name, api=api_str,
            weather=dict_weather, unit=temp_unit_str)
    else:
        print(queryform.city_name.data)
        return render_template('index.html', form=queryform, location_str=location_str)

@app.route('/history')
def history():
    history = db.session.query(History).all()
    print(history)
    return render_template('history.html', history=history)

@app.route('/about')
def about():
    return render_template('about.html')