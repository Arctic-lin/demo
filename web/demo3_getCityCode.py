# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 21:24
# @Author  : Arctic
# @FileName: demo3_getCityCode.py
# @Software: PyCharm
# @Purpose : Get City Code
#base url:http://cdn.heweather.com/china-city-list.txt
import requests
import re
import time
my_key='284c5f3e240a4b7a98a28220e8ab8dfd'
def getCityCode(cityName="huizhou"):
	urlCityCode="http://cdn.heweather.com/china-city-list.txt"
	strHtml=requests.get(urlCityCode)
	strHtml.encoding="utf-8"
	data=strHtml.text
	dataSplit=data.split("\n")
	dict_code_name={}
	for i in range(3):
		dataSplit.remove(dataSplit[0])
	for i in dataSplit:
		code = re.findall("CN\d+",i)
		city_name=re.findall("[a-z]+",i)
		if code and city_name:
			dict_code_name[code[0]]=city_name[0]
	for k,v in dict_code_name.items():
		if v == cityName.lower():
			return k
def get_data(cityName="huizhou"):
	cityCode=getCityCode(cityName)
	urlWeather='https://free-api.heweather.net/s6/weather/now?location=%s&key=%s'%("惠州",my_key)
	print(urlWeather)
	htmlWeather=requests.get(urlWeather)
	htmlWeather.encoding="utf-8"
	time.sleep(1)
	print(htmlWeather.text)
if __name__ == '__main__':
	get_data()

