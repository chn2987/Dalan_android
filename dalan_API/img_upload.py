#!/usr/bin/env python
# encoding: utf-8
__author__ = "晨晨"
import requests,time
import os,json
from dalan_tools import config
#——————————————————————————————————————————————windows客服端————————————————————————————————————————————
#=================================上传文件到oss服务器==========================================================================
def upload(path):
    file = {'file': open(path,'rb')}
    data={'name':'test_3012',
    'chunks':'1',
    'type':'game_icon'
    }
    environment=config.using_huanj()
    if environment=='test':
        r = requests.post('http://file.local.superdalan.com/upload', data=data,files=file)
    elif environment=='production':
        r = requests.post('http://file.superdalan.com/upload', data=data,files=file)
    return  json.loads(r.text)['data']


if __name__=="__main__":
    print(upload(r'C:\Users\Administrator\Desktop\test.png'))
    # adb=r'D:\adtwindows\sdk\platform-tools\adb.exe'
    # wei=r'C:\Users\Administrator\Desktop'
    # aa=time.strftime("%Y%m%d_%H%M%S_", time.localtime())
    # screen=adb  + " -s {} shell \" LD_LIBRARY_PATH=/data/local/tmp /data/local/tmp/minicap -P {}@{}/0 -s > /sdcard/screencap.png\"".format('54a4c6159804',1920,1080)
    # os.popen(screen)
    # #传到电脑
    # os.system(adb + " -s " +'54a4c6159804'  + " pull /sdcard/screencap.png "  +(str(wei+'\\'+aa+'.png')))

'''
http://file.local.superdalan.com//117c66e0eb041d06d74353b9b51a9eaf~500...............测试环境在线查看图片
'''

