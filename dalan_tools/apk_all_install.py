#!/usr/bin/env python
# encoding: utf-8
__author__ = "晨晨"
from airtest.core.api import *
from dalan_tools import adb,lujin_qubaoming,log_file,screen_state
import time,os
import threading
from time import ctime

def device_oppo(device):
    '''用于oppo手机装包输密码'''
    print(screen_state.isAwaked(device))#保证手机在亮屏状态
    for i in range(25):
        if 'com.coloros.safecenter' in os.popen('adb -s ea91a8e0 shell dumpsys activity|findstr "mFocusedActivity"').read():
            os.system('adb -s '+device+' shell input text "xiawei1314"')
            os.system('adb -s '+device+' shell input tap 740 1100')
            break
        else:
            time.sleep(3)
    time.sleep(7.5)
    os.system('adb -s '+device+' shell input tap 780 1840')
    time.sleep(4.5)
    print(ctime())
    os.system('adb -s '+device+' shell input tap 300 1840')

    if device=='ea91a8e0':
        installThread = threading.Thread(target=device_oppo, args=(device,))
        installThread.start()

def meizu():
    pass


def auto_install(device,name):
    start_time=str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print(start_time+'--{}开始安装{}'.format(device,name))
    'u''自动安装apk_安装后默认打开app'''
    try:
        #connect_device("Android://127.0.0.1:5037"+'/'+device)
        connect_device("Android:///{}?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH".format(device))
        time.sleep(2)
        auto_setup(__file__)
        apk_lujin= os.path.dirname(os.path.dirname(__file__))+'/File_directory/'+name
        print(apk_lujin)
        #根据apk路径获取包名
        chen=lujin_qubaoming.ApkInfo(apk_lujin)#创建对象
        apk_bao_name=chen.getApkBaseInfo()#调用
        #判断是否已安装
        duix=adb.SDK(device,apk_bao_name)#创建对象
        fanhui=duix.bao_is_or_no()#调用bao_is_or_no()
        print(fanhui)
        sleep(2)
        if fanhui==True:
            print('{}--{}--install_前检查手机已安装{}'.format(ctime(),device,name))
            print('{}--开始卸载{}包'.format(device,name))
            uninstall(apk_bao_name)#卸载包
            print('{}--{}--卸载{}包完成_____进行再次安装{}'.format(ctime(),device,name,name))
            #启动一个线程执行安装密码操作
            # if device=='ea91a8e0':
            #     installThread = threading.Thread(target=device_oppo, args=(device,))
            #     installThread.start()
            # time.sleep(2)
            install(os.path.dirname(os.path.dirname(__file__))+'/File_directory/'+name)
            #installThread.join()
            duix=adb.SDK(device,apk_bao_name)#创建对象
            z_fanhui=duix.bao_is_or_no()#调用bao_is_or_no()
            if z_fanhui==True:
                return True
        else:
            start=str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            print(start+'_开始在%s设备安装_%s'%(device,name))
            # if device=='ea91a8e0':
            #     installThread = threading.Thread(target=device_oppo, args=(device,))
            #     installThread.start()
            # time.sleep(2)
            install(os.path.dirname(os.path.dirname(__file__))+'/File_directory/'+name)
            #installThread.join()
            #判断手机是否安装apk
            bao_name=adb.SDK(device,apk_bao_name)
            fan=bao_name.bao_is_or_no()
            print(fan)
            if fan==True:
               return True
    except:
        print('{}--{}安装{}过程中出现异常_执行失败'.format(ctime(),device,name))
        if apk_bao_name=='获取包名失败配置问题':
            return '包名获取失败_原因apk损坏'
        elif device !='':
            return '未知异常_404'
        else:
            print('当前没有设备')
            return '当前无设备连接_error'
    zuihou=str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    log_file.log(r'D:\Downloads目录有:', name)#写入日志

if __name__ == '__main__':
    print(auto_install('ea91a8e0','plugin_host_demo-dalan-debug.apk'))
