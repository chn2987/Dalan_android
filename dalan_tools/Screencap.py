# -*- coding: utf-8 -*-
__author__ = "无声"
import os
import time
from PIL import Image
from dalan_API import img_upload
from dalan_tools import config

#############——————————————————————————用于手动截图操作—————————————————————————————————
'''
_print = print
def print(*args, **kwargs):
    _print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), *args, **kwargs)
'''
adb=r'D:\adtwindows\sdk\platform-tools\adb.exe'
reportpath = os.path.join(os.getcwd(), "Report")
screenpath = os.path.join(reportpath, "Screen")

def  GetScreen(starttime,devices,action):##action传True表示横屏截图(action为空是竖屏)
    ABIcommand = adb + " -s {} shell getprop ro.product.cpu.abi".format(devices)#获取Android系统属性
    ABI = os.popen(ABIcommand).read().strip()
    if ABI=="x86":
        pass
        png = GetScreenbyADBCap(starttime, devices, action)#模拟器
    else:
        try:
            png= GetScreenbyMiniCap(starttime,devices,action)#手机，，starttime当前时间,devices, action描述
        except:
            print("MiniCap截图失败，换ADB截图")
    return png

#用ADBCAP的方法截图——-模拟器截图方法
def GetScreenbyADBCap(starttime,devices,action):
    #先给昵称赋值，防止生成图片的命名格式问题。
    if ":" in devices:
        nickname = devices.split(":")[1]
    else:
        nickname=devices
    upload=''
    os.system(adb + " -s " + devices + " pull /sdcard/screencap.png " + ('"' + str(png) + '"'))
    png = screenpath +"\\"+ time.strftime('%Y%m%d_%H%M%S',time.localtime(starttime))+ nickname+ "_" + action+ ".png"
    os.system(adb + " -s " + devices + " shell screencap -p /sdcard/screencap.png")
    time.sleep(1)
    fp = open(png, "a+", encoding="utf-8")
    fp.close()
    os.system(adb + " -s " + devices + " pull /sdcard/screencap.png " + ('"' + str(png) + '"'))
    time.sleep(0.5)
    #ADB截图过大，需要压缩，默认压缩比为0.2，全屏。
    compressImage(png)
    print("<img src='" + png + "' width=600 />")
    return png

#用MiniCap的方法截图，使用前需要确保手机上已经安装MiniCap和MiniCap.so。一般用过STF和airtestide的手机会自动安装，若未安装，则可以执行Init_MiniCap.py，手动安装。
#starttime当前时间,action描述---------------正常手机截图
def GetScreenbyMiniCap(starttime,devices,action,ssFlipped=False):
    # 先给昵称赋值，防止生成图片的命名格式问题。
    if ":" in devices:
        nickname = devices.split(":")[1]
    else:
        nickname=devices
    #创建图片
    #png='http://file.local.superdalan.com/e327858baca597c0fd3f8a02f9ecf4c3~500'
    #png = screenpath + "\\" + time.strftime("%Y%m%d_%H%M%S_", time.localtime(starttime)) + nickname + "_" + action + ".png"
    #获取设备分辨率
    wmsizecommand = adb + " -s {} shell wm size".format(devices)
    size = os.popen(wmsizecommand).read()
    size = size.split(":")[1].strip()
    if ssFlipped:
        slist = size.split("x")
        size = slist[1] + "x" + slist[0]
    a_path=(os.path.dirname(os.path.dirname(__file__))+'/Report/'+devices+'_test.png')
    if os.path.exists(a_path):
        os.remove(a_path)#删除文件
    chen=a_path
    if devices != 'b5940085':
        #截图并上传PC端
        s_size=size[size.find('x')+1:]+'x'+size[:size.find('x'):]
        if action=="":
            screen=adb  + " -s {} shell \" LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P {}@{}/0 -s > /sdcard/screencap.png\"".format(devices,size, size)
        elif action=="True":
            screen=adb  + " -s {} shell \" LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P {}@{}/0 -s > /sdcard/screencap.png\"".format(devices,s_size,s_size)
        os.system(screen)#执行shell
        time.sleep(1)
    elif devices ==  'b5940085':#android 10不支持minicap
        os.system('adb -s {} shell screencap -p sdcard/screencap.png'.format(devices))
        time.sleep(1)
    os.system(adb + " -s " + devices + " pull /sdcard/screencap.png " +('"' + str(chen) + '"'))#上传截图到PC
    path= img_upload.upload(chen)#上传图片到文件系统
    environment=config.using_huanj()
    if environment=='test':
        png='http://file.local.superdalan.com'+'//'+path+'~500'
    elif environment=='production':
        png='http://file.superdalan.com'+'//'+path+'~500'
    print("<img src='" + png + "' width=600 />")
    print("{}--返回的png为 {}".format(devices,png))
    return png

    # 图片压缩批处理，cr为压缩比，其他参数为屏幕截取范围
def compressImage(path,cr=0.2,left=0,right=1,top=0,buttom=1):
    # 打开原图片压缩
    sImg =Image.open(path)
    w, h = sImg.size# 获取屏幕绝对尺寸
    box=(int(w*left),int(h*top),int(w*right),int(h*buttom))
    sImg=sImg.crop(box)
    time.sleep(0.1)
    # 设置压缩尺寸和选项
    dImg = sImg.resize((int(w*cr), int(h*cr)), Image.ANTIALIAS)
    time.sleep(0.1)
    # 压缩图片路径名称
    dImg.save(path)  # save这个函数后面可以加压缩编码选项JPEG之类的


if __name__=="__main__":
    #compressImage(r'C:\Users\Administrator\Desktop\chen.png')#图片压缩
    GetScreen(time.time(),'b5940085',"")#为True截横屏
    #GetScreenbyMiniCap(time.time(),"172.16.6.82:7597","test")






