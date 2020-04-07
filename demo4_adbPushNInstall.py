import os
import sys

# filedir = input()

def pushDocument(name="pdf", reName=True, type="push"):
    # 将文件夹进行遍历
    for filename in os.listdir(filedir):
        # 将文件夹名进行分割
        a = filename.split(".")
    # 判断文件夹名最后一位是否是中文，如果是就增加英文以免报错
        if name in a[-1]:
            if u'\u4e00' <= a[0][-1:] <= u'\u9fff':
                os.rename(os.path.join(filedir, filename), os.path.join(
                    filedir, a[0] + "_rename." + a[-1]))
    # 将更改后的文件进行二次遍历，并进行相应的安装或者push
    for filename in os.listdir(filedir):
        a = filename.split(".")
        if name in a[-1]:
            b = os.path.join(filedir, filename)
            if type.lower().strip() == "push":
                os.system("adb push \"%s\" /sdcard/" % b)
            elif type.lower().strip() == "install":
                os.system("adb install -r %s" % b)
    # 把更改后的文件夹恢复到原本的样子
    if reName:
        for filename in os.listdir(filedir):
            a = filename.split(".")
            if name in a[-1]:
                if len(a[0]) > 7:
                    if a[0][-7:] == "_rename":
                        os.rename(os.path.join(filedir, filename), os.path.join(
                            os.path.join(filedir, a[0][0:-7] + "." + a[-1])))


if __name__ == '__main__':
    filedir = input("文件目录名： ")
    pushDocument(name="doc", type="push", reName=True)
    a = input()
