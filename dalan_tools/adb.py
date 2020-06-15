#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年9月14日

@author: chen
'''
import time
import os
class SDK():
    def __init__(self,device,bao):
         self.a = os.popen("adb -s " +device+" shell pm list package -3")
         os.system('adb devices')
         self.bao=bao
         self.device=device

    def sdk_zhuye(self):
        ''' 用于截图 '''
        
        a='SDK主页'
        os.system('adb version')
        os.system('adb shell /system/bin/screencap -p /data/local/tmp/'+a+'.png')
        os.system('adb pull /data/local/tmp/'+a+'.png  D:/dalan/javacc/appium/dalan/'+a+'.png')
    
    def sdk_install(self):
        '''用于安装apk'''
        chen=input("请输入安装apk的绝对路径")
        time.sleep(2)
        os.system('adb install -r '+chen+'')

    def sdk_uninstall(self):
        '''用于卸载apk'''
        # os.system('adb uninstall '+self.bao+'')
        fan=sd.bao_is_or_no()
        print(fan)
        if fan:#只要返回值不等于0就走if
            os.system('adb uninstall '+self.bao+'')
        else:
            print('此手机未安装%s包'%(self.bao))

    def bao_is_or_no(self):
        '''判断手机是否安装了_某个应用'''
        aa=[]#定义空列表，用于遍历for的
        for i in self.a:
            a = i.lstrip('package').lstrip(":").strip()#取出每一个包
            aa.append(a)
        if self.bao in aa:#判断列表是否存在指定元素
            print('%s手机已安装%s包....'%(self.device,self.bao))
            return True
        else:
            print('%s手机未安装%s包....'%(self.device,self.bao))
            return  False
if __name__ == '__main__':
    sd=SDK('ea91a8e0','com.dalan.zyrg')
    sd.bao_is_or_no()
    # sd.sdk_zhuye()
    # sd.sdk_install()
    #sd.bao_is_or_no()
    # sd.sdk_uninstall()


