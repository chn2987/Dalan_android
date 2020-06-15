#!/usr/bin/env python
#coding:utf-8
import re,os
import subprocess
class ApkInfo:
    def __init__(self, apkPath):
        self.apkPath = apkPath

    def getApkBaseInfo(self):
        'u''通过apk的路径来获取包名'''
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode('utf-8', errors='ignore'))
        if not match:
            return '获取包名失败配置问题'
        packagename = match.group(1)
        versionCode = match.group(2)
        versionName = match.group(3)

        print(self.apkPath+'==' + packagename)#打印包名
        #print(packagename)
        #print('versionCode:' + versionCode)
        #print('versionName:' + versionName)#版本
        return packagename

if __name__=='__main__':
    chen=ApkInfo(r'D:\Downloads\zyrghb_dalan_dsdk_48_1.0.0_20200422_181857.apk')#相当于创建对象，并调用
    print(chen.getApkBaseInfo())
