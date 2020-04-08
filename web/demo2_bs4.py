# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 16:51
# @Author  : Arctic
# @FileName: demo2_bs4.py
# @Software: PyCharm
# @Purpose : Practise beautifulsoup
import requests
import re
from bs4 import BeautifulSoup
import get_proxies
import random
headers={
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
}
a=get_proxies.get_proxies()
proxies=[]
for k,v in a.items():
	proxies.append({v[-1].lower():k+":"+v[0]})
abc=random.choice(proxies)
print(abc)
url = 'http://www.cntour.cn/'
strhtml = requests.get(url,headers=headers,proxies=abc)
soup = BeautifulSoup(strhtml.text,"lxml")
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox')
for i in data:
	result={
		'title':i.get_text().strip(),
		'link':i.get('herf'),
		# 'ID':re.findall('\d+',i.get("href"))
	}
	print(result)
# get_data = re.findall(".*<a href="+"(.*?)"+" target" + ".*title=" +"(.*?)" + "</a>",data.get_text())
# print(get_data)