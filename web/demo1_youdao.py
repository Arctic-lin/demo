# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 10:52
# @Author  : Arctic
# @FileName: demo1_youdao.py
# @Software: PyCharm
# @Purpose :study web crawler
import json
import requests
#浏览器中使用有道并抓取network中的XHR
def get_translate(word=None):
	#原本translate_o?去掉_o才能抓取
	url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
	daTA={"i": word,
	"from": "AUTO",
	"to": "AUTO",
	"smartresult": "dict",
	"client": "fanyideskweb",
	"salt": "15857097116353",
	"sign": "d3e3d344b4bdc1d1d98767028372f50f",
	"ts": "1585709711635",
	"bv": "319767f82622c78aa4241bb7a80c5077",
	"doctype": "json",
	"version": "2.1",
	"keyfrom": "fanyi.web",
	"action": "FY_BY_REALTlME"}
	htmlText=requests.post(url,data=daTA)
	content=json.loads(htmlText.text)
	print(content["translateResult"][0][0]["tgt"])
if __name__ == '__main__':
	get_translate("卧槽")