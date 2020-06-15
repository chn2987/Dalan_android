#!/usr/bin/env python
# encoding: utf-8
__author__ = "晨晨"
import os,re
import threading
from airtest.core.api import *
from dalan_tools import  Screencap
from TestCase.chwy_74.dalan.dsdk import get_order_log
from multiprocessing import Process
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

def place_order(device):
    '''游戏内操作充值'''
    order_id=None#默认为None
    sleep(3.0)
    try:
        connect_device("Android:///"+device)
        auto_setup(__file__)
        poco=AndroidUiautomationPoco()
        sleep(1.8)
        #先判断是否有商城按钮
        if exists(Template(r"mxd_商城按钮.png", threshold=0.6,record_pos=(0.345, -0.226), resolution=(1280, 720))):
            print('{}--{}找到商城入口按钮'.format(os.getpid(),device))
            touch(Template(r"mxd_商城按钮.png", threshold=0.6,record_pos=(0.345, -0.226), resolution=(1280, 720)))
            sleep(2.0)
            touch(Template(r"mxd_充值按钮.png", record_pos=(0.428, 0.066), resolution=(1280, 720)))
            sleep(2.0)
        #直接通过头像位置进入充值档位
        elif exists(Template(r"mxd_游戏内任务.png",record_pos=(0.334, 0.231), resolution=(1280, 720)),30):
            print('{}--{}没有找到商城-直接通过头像位置进入充值档位'.format(os.getpid(),device))
            poco.click([0.033,0.087])
            sleep(2.0)
            poco.click([0.918,0.038])
            sleep(2.0)
        else:
            print('%s--在游戏内找不到元素_可能原因：实名制弹窗|游戏副本加载页|游戏不固定元素蒙层|网络异常弹框蒙层'%device)
            img=Screencap.GetScreen(time.time(), device, "True")
            return False,device+'在游戏内找不到元素_可能原因：实名制弹窗|游戏副本加载页|游戏不固定元素蒙层|网络异常弹框蒙层',img[img.find(r'superdalan.com//')+16:][:-4]

        #创建线程获取日志
        t = threading.Thread(target=get_order_log.say,args=('eve',device))
        t.setDaemon(True)
        t.start()
        sleep(1.8)
        if exists(Template(r"mxd_6元按钮.png", record_pos=(-0.306, 0.037), resolution=(1280, 720))):
            print('{}--{}进入充值档位页面'.format(os.getpid(),device))
            touch(Template(r"mxd_6元按钮.png", record_pos=(-0.306, 0.037), resolution=(1280, 720)))
            #判断是否弹出支付方式
            if  poco(text="微信").wait(8).exists():
                print('{}--{}拉起支付方式弹窗成功'.format(os.getpid(),device))
                poco(text="微信").click()
                time.sleep(4)
            else:
                print('{}--{}拉起支付方式失败'.format(os.getpid(),device))
            t.join()
        print('{}___主线程结束___'.format(device))
        path=os.path.dirname(__file__)
        #----------------打开文件读取数据-----------------------
        with open(path+'/order_log/'+device+'.txt',mode="r",encoding="UTF-8",errors="ignore") as abc:
            fileContent=abc.readlines()
        #---------------筛选mPayInfo  pay日志的内容-------------------------
        for i in  range(len(fileContent)):
            if 'union_order_sn' in fileContent[i]:
                pattern = re.compile('"union_order_sn":"([0-9]{15,20})')#正则表达式实例
                result = pattern.findall(fileContent[i])#匹配的字符串
                order_id=''.join(result)
                print('%s登录order_id=%s'%(device,order_id))
                break
            else:
                print('{}日志文件是空的_没有获取到order_id'.format(device))
        for i in range(5):
            sleep(4.0)
            if poco(text="登录").exists():
                print('%s当前未登录微信'%device)
                img=Screencap.GetScreen(time.time(), device, "")
                return True,order_id,img[img.find(r'superdalan.com//')+16:][:-4]
            elif poco(text="立即支付").exists():
                img=Screencap.GetScreen(time.time(), device, "")
                return True,order_id,img[img.find(r'superdalan.com//')+16:][:-4]
        else:
            img=Screencap.GetScreen(time.time(), device, "")
            return False, device+'微信无法调起!,手机反应太慢_超时',img[img.find(r'superdalan.com//')+16:][:-4]

    except:
        img=Screencap.GetScreen(time.time(), device, "")
        print('{}--{}--已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'.format(os.getpid(),device))
        return False,device+'由于网络原因，或手机反应慢到导致元素无法找到_超时',img[img.find(r'superdalan.com//')+16:][:-4]

if __name__ == "__main__":
    # p1 = Process(target=place_order,args=('54a4c6159804',))
    # p2 = Process(target=place_order,args=('R8AYIJWO99999999',))
    # p1.start()
    # p2.start()
    print(place_order('R8AYIJWO99999999'))
