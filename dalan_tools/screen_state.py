#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,time

def isAwaked(deviceid = ''):
    '''
    判断手机是否息屏，若息屏则解锁
    '''
    if deviceid == '':
        cmd = 'adb shell dumpsys window policy'
    else:
        cmd = 'adb -s ' + deviceid + ' shell dumpsys window policy^|grep isStatusBarKeyguard'
    allList = os.popen(cmd).read()
    if  'isStatusBarKeyguard=true' not in allList:
        return deviceid+'--手机亮屏状态'
    else:
        print('%s手机已灭屏_将执行解锁命令'%deviceid)
        os.popen('adb -s '+ deviceid + ' shell input keyevent 26')
        time.sleep(1)
        os.system('adb -s '+ deviceid + ' shell input swipe 500 1150 500 200')
        return deviceid+'--手机亮屏状态_二次点亮'

if __name__ == "__main__":
    print(isAwaked('54a4c6159804'))
