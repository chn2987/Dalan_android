#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
class Android_device_xinxi():

    def __init__(self,device_id):
        self.device=device_id
        self.size=os.popen('adb -s '+device_id+' shell wm size').read().strip('\n')#分辨率
        self.model=os.popen('adb -s '+device_id+' shell getprop  ro.product.model').read().strip('\n')#获取型号
        self.system_version=os.popen('adb -s '+device_id+' shell getprop ro.build.version.release').read().strip('\n')#获取版本
        #获取ime
        self.imei=os.popen("adb -s "+device_id+" shell "+'"'+r"service call iphonesubinfo 1 | grep -o '[0-9a-f]\{8\} ' | tail -n+3 | while read a; do echo -n \\u${a:4:4}\\u${a:0:4}; done"+'"'"").read().strip('\x00\x00')
        if os.popen('adb -s '+device_id+' shell ifconfig wlan0|findstr "inet addr"|findstr "Bcast"').read() is not '':
            self.network='当前网络为-wifi'
        else:
            self.network='当前网络为-移动网络'

    def device_xinxi(self):
        return {'device_id':self.device,'size':self.size[self.size.find('Physical size:')+15:],'model':self.model,'system_version':self.system_version,'imei':self.imei,'network':self.network}

if __name__ == '__main__':
    a=Android_device_xinxi('R8AYIJWO99999999')
    print(a.size,a.model,a.system_version,a.imei,'\n',a.network,a.device)
    print(a.device_xinxi())

