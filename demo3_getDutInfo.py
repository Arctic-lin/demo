# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 9:54
# @Author  : Arctic
# @FileName: demo3_getDutInfo.py
# @Software: PyCharm
# @Purpose :Get Device SN

import os
import subprocess
import re
#获取并返回手机设备号
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
#获取并返回当前应用的包名和activity(full_activity)
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
#获取并返回所有带有Activity的包名和activity(full_activity)
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
#获取并返回播放音乐状态,0为未知,2为未播放,3为播放中
def checkMusicIsPlaying():
	runCMD = subprocess.check_output ('adb shell "dumpsys media_session | grep state=PlaybackState"', encoding="utf-8")
	playState=re.findall("state="+"(\d)" + "\,",runCMD)
	if playState:
		if playState[0] == "2":
			print("Play status:%s,No playing Music"%playState[0])
			return 2
		elif playState[0] == "3":
			print ("Play status:%s,Playing Music Now" % playState[0])
			return 3
	else:
		print("Can't get music_state,pls launcher music and play once time")
		return 0
#获取并返回手机基本信息
def getDutInfo():
	dutInfo={}
	cmd_=["getprop ro.build.fingerprint","wm size","getprop gsm.device.imei","settings get system screen_brightness",
	      "getprop ro.tct.trace.wifi"]
	for i in cmd_:
		if "fingerprint" in i :
			runCMD = subprocess.check_output ("adb shell"+" "+i, encoding="utf-8")
			getData=runCMD.split("/")
			if getData:
				dutInfo["Branch"]=getData[1]
				dutInfo["ProjectName"]=getData[2]
				dutInfo["Version"]=getData[-2]
		elif "wm" in i:
			runCMD = subprocess.check_output ("adb shell" + " " + i, encoding="utf-8")
			if runCMD:
				a = re.findall("size:" + "(.*?)" +"\n",runCMD)
				dutInfo["ScreenDisplay"]=a[0]
		elif "imei" in i:
			runCMD = subprocess.check_output ("adb shell" + " " + i, encoding="utf-8")
			if runCMD:
				dutInfo["IMEI"]=runCMD.strip()
		elif "brightness" in i:
			runCMD = subprocess.check_output ("adb shell" + " " + i, encoding="utf-8")
			if runCMD:
				dutInfo["Brightness"]=runCMD.strip()
		elif "wifi" in i:
			runCMD = subprocess.check_output ("adb shell" + " " + i, encoding="utf-8")
			if runCMD:
				dutInfo["MacAdress"]=runCMD.strip()
	return dutInfo

def checkHardKeyWork():
	pass

if __name__ == '__main__':
	getDutInfo()