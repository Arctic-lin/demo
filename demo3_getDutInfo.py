# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 9:54
# @Author  : Arctic
# @FileName: demo3_getDutInfo.py
# @Software: PyCharm
# @Purpose :Get Device SN

import os
import subprocess
import re

def getDutSN():
	try:
		devInfo = subprocess.check_output("adb devices",encoding="utf-8")
		dutSN = re.findall ("\n" + "(.*?)" + r"\tdevice", devInfo)
		if dutSN:
			return dutSN
		else:
			print("No devices connect,Pls check...")
	except subprocess.CalledProcessError as e:
		print(e.returncode)
		print(e.output)

def getCurrentPkg(full_activity=True):
	runCMD=subprocess.check_output('adb shell "dumpsys activity top | grep ACTIVITY"',encoding="utf-8")
	listAppBackGround=runCMD.strip().split("\n")
	currentPKG=re.findall("ACTIVITY "+"(.*?)"+" ",listAppBackGround[-1])
	if full_activity:
		if currentPKG:
			return currentPKG[0]
	elif full_activity == False:
		if currentPKG:
			pkg=currentPKG[0].split("/")
			return pkg[0]

def getDutAPK(full_activity=True):
	runCMD="adb shell monkey -c android.intent.category.LAUNCHER -v -v -v 0"
	getData=subprocess.check_output(runCMD,encoding="utf-8")
	getActivityAndPkg=re.findall("main activity "+"(.*?)"+" \(from package " + "(.*?)" +"\)\n",getData)
	pkg=[]
	if full_activity:
		for i in getActivityAndPkg:
			joinstr=i[0]+"\\"
			joinstr_a=joinstr+i[1]
			pkg.append(joinstr)
	elif full_activity == False:
		for i in getActivityAndPkg:
			pkg.append(i[1])
	return pkg

if __name__ == '__main__':
	a=getDutAPK()
	print(a)
	os.system("adb shell am start -n %s"%a[0])