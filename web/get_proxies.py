# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 17:33
# @Author  : Arctic
# @FileName: get_proxies.py
# @Software: PyCharm
# @Purpose : getproxies
import requests
import re
from bs4 import BeautifulSoup
def get_proxies():
	headers={
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
	}
	url = 'https://www.xicidaili.com/'
	strhtml = requests.get(url,headers=headers)
	soup = BeautifulSoup(strhtml.text,"lxml")
	data={}
	mac_address= soup.select('#ip_list > tr > td:nth-child(2)')
	mac_port= soup.select('#ip_list > tr > td:nth-child(3)')
	mac_type = soup.select ('#ip_list > tr > td:nth-child(6)')
	for i in range(len(mac_address)):
		if "socks" not in str(mac_type[i]):
			if str(mac_port[i]) == "80" or "8080":
				data["%s"%str(mac_address[i]).replace("<td>","").replace("</td>","")] = \
				["%s"%str(mac_port[i]).replace("<td>","").replace("</td>",""),"%s"%str(mac_type[i]).replace("<td>","").replace("</td>","")]
	return data
if __name__ == '__main__':
	a=get_proxies()
	print(a)