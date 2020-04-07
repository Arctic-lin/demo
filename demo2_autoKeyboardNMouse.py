# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 11:26
# @Author  : Arctic
# @FileName: demo2_autoKeyboardNMouse.py
# @Software: PyCharm
# @Purpose :

# import requests
# url="http://simplex.tclcom.com/pms/attendance/sheet?page.pageNo=1&dto.begin=&dto.end="
#
# html_text=requests.get(url)
# print(html_text.text)
import pyautogui,sys
import subprocess
try:
	while True:
		x, y = pyautogui.position ()
		positionStr = "X:" + str (x).rjust (4) + "Y:" + str (y).rjust (4)
		print (positionStr, end="")
		print ("\b" * len (positionStr), end="", flush=True)
except KeyboardInterrupt:
		print ("\n")

