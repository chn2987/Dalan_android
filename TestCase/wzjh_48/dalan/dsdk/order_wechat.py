#!/usr/bin/env python
# encoding: utf-8
__author__ = "晨晨"
import os,re,logging
from airtest.core.api import *
import threading
from dalan_tools import  Screencap
from TestCase.wzjh_48.dalan.dsdk import get_order_log
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

class Order(object):

    def __init__(self,device):
        self.device=device
        logger = logging.getLogger("airtest")
        logger.setLevel(logging.ERROR)#过滤日志等级
        connect_device("Android:///{}?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH".format(device))
        time.sleep(2)
        auto_setup(__file__)
        self.poco=AndroidUiautomationPoco()
        sleep(1.5)
        os.system('adb -s {} shell input swipe 500 900 800 400 100'.format(device))

    def order_handle_wzjh(func):
        '''装饰器函数：日志获取及结果处理'''
        def wrapped(self,*arg,**kwargs):
            result=func(self)#调用函数
            if result is None:#正常情况下没有返回值,也就是None
                path=os.path.dirname(__file__)
                #----------------打开文件读取数据-----------------------
                with open(path+'/order_log/'+self.device+'.txt',mode="r",encoding="UTF-8",errors="ignore") as abc:
                    fileContent=abc.readlines()
                #---------------筛选mPayInfo  pay日志的内容-------------------------
                for i in  range(len(fileContent)):
                    if 'union_order_sn' in fileContent[i]:
                        pattern = re.compile('"union_order_sn":"([0-9]{15,20})')#正则表达式实例
                        result = pattern.findall(fileContent[i])#匹配的字符串
                        order_id=''.join(result)
                        print('%s登录order_id=%s'%(self.device,order_id))
                        break
                    else:print('{}日志文件是空的_没有获取到order_id'.format(self.device))
                if len(fileContent) is 0:
                    print('{}__日志是空的'.format(self.device))
                    img=Screencap.GetScreen(time.time(), self.device, "")
                    return False, self.device+'__获取日志为空！',img[img.find(r'superdalan.com//')+16:][:-4]
                #循环5次还找不到元素，就直接返回False
                for i in range(5):
                    sleep(4.0)
                    if self.poco(text="登录").exists():
                        print('%s当前未登录微信'%self.device)
                        img=Screencap.GetScreen(time.time(), self.device, "")
                        return True,order_id,img[img.find(r'superdalan.com//')+16:][:-4]
                    elif self.poco(text="立即支付").exists():
                        img=Screencap.GetScreen(time.time(), self.device, "")
                        return True,order_id,img[img.find(r'superdalan.com//')+16:][:-4]
                else:
                    img=Screencap.GetScreen(time.time(), self.device, "")
                    return False, self.device+'微信无法调起!,手机反应太慢_超时',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                return result
        #这里可以加预处理操作
        return wrapped

    @order_handle_wzjh
    def place_order_54a4c6159804(self):
        '''小米4x调起微信'''
        if exists(Template(r"wzjh立即领取.png", threshold=0.6, record_pos=(0.054, 0.161), resolution=(1920, 1080))):
            print('{}--{}有立即领取按钮'.format(os.getpid(),self.device))
            touch(Template(r"wzjh立即领取.png", threshold=0.6, record_pos=(0.054, 0.161), resolution=(1920, 1080)))
            sleep(6)#已在充值档位页面
        elif exists(Template(r"wzjh首充按钮.png",record_pos=(0.333, -0.16), resolution=(1920, 1080))):
            print('{}--{}找到首充按钮'.format(os.getpid(),self.device))
            touch(Template(r"wzjh首充按钮.png", record_pos=(0.333, -0.16), resolution=(1920, 1080)))
            sleep(2.0)
            touch(Template(r"wzjh立即领取.png", threshold=0.6, record_pos=(0.054, 0.161), resolution=(1920, 1080)))
            sleep(6)#已在充值档位页面
        if exists(Template(r"wzjh_6元档位.png", record_pos=(-0.374, -0.016), resolution=(1920, 1080))):
            print('{}_已在充值档位页面'.format(self.device))
            #创建线程获取日志
            t = threading.Thread(target=get_order_log.say,args=('eve',self.device))
            t.setDaemon(True)
            t.start()
            touch(Template(r"wzjh_6元档位.png", record_pos=(-0.374, -0.016), resolution=(1920, 1080)))
            if  self.poco(text="微信").wait(8).exists():
                print('{}--{}拉起支付方式弹窗成功'.format(os.getpid(),self.device))
                self.poco(text="微信").click()
                time.sleep(4)
            else:
                print('{}--{}拉起支付方式失败'.format(os.getpid(),self.device))
            t.join()
        else:
            print('{}在游戏内找不到元素_可能原因：实名制弹窗|游戏副本加载页|游戏不固定元素蒙层|网络异常弹框蒙层_请看截图'.format(self.device))
            img=Screencap.GetScreen(time.time(), self.device, "")
            return False,self.device+'在游戏内找不到元素_可能原因：实名制弹窗|游戏副本加载状态|游戏不固定元素蒙层|网络异常弹框蒙层等',img[img.find(r'superdalan.com//')+16:][:-4]
        print('{}___主线程结束___'.format(self.device))

    @order_handle_wzjh
    def place_order_QDY4C17818002168(self):
        '''华为畅享7_调起微信'''
        if exists(Template(r"wzjh首充按钮.png", threshold=0.55,record_pos=(0.333, -0.16), resolution=(1920, 1080))):
            print('{}--{}找到首充按钮'.format(os.getpid(),self.device))
            touch(Template(r"wzjh首充按钮.png", record_pos=(0.333, -0.16), resolution=(1920, 1080)))
            sleep(2.0)
        #有时候可能直接弹出立即领取页面
        if exists(Template(r"wzjh立即领取.png", threshold=0.6, record_pos=(0.054, 0.161), resolution=(1920, 1080))):
            print('{}--{}有立即领取按钮'.format(os.getpid(),self.device))
            touch(Template(r"wzjh立即领取.png", threshold=0.6, record_pos=(0.054, 0.161), resolution=(1920, 1080)))
            sleep(4)#已在充值档位页面
        if exists(Template(r"wzjh_6元档位.png", record_pos=(-0.374, -0.016), resolution=(1920, 1080))):
            print('{}_已在充值档位页面'.format(self.device))
            #创建线程获取日志
            t = threading.Thread(target=get_order_log.say,args=('eve',self.device))
            t.setDaemon(True)
            t.start()
            touch((165,220))#点击档位
            if  self.poco(text="微信").wait(8).exists():
                print('{}--{}拉起支付方式弹窗成功'.format(os.getpid(),self.device))
                self.poco(text="微信").click()
                time.sleep(4)
            else:
                print('{}--{}拉起支付方式失败'.format(os.getpid(),self.device))
            t.join()
        else:
            print('{}在游戏内找不到元素_可能原因：实名制弹窗|游戏副本加载页|游戏不固定元素蒙层|网络异常弹框蒙层_请看截图'.format(self.device))
            img=Screencap.GetScreen(time.time(), self.device, "")
            return False,self.device+'在游戏内找不到元素_可能原因：实名制弹窗|游戏副本加载状态|游戏不固定元素蒙层|网络异常弹框蒙层等',img[img.find(r'superdalan.com//')+16:][:-4]
        print('{}___主线程结束___'.format(self.device))

    @order_handle_wzjh
    def place_order_b5940085(self):
        '''小米9_调起微信'''
        if exists(Template(r"wzjh首充按钮.png", threshold=0.65,record_pos=(0.333, -0.16), resolution=(2340, 1080))):
            print('{}--{}找到首充按钮'.format(os.getpid(),self.device))
            touch(Template(r"wzjh首充按钮.png", threshold=0.65, record_pos=(0.333, -0.16), resolution=(2340, 1080)))
            sleep(2.0)
        #有时候可能直接弹出立即领取页面
        if exists(Template(r"wzjh立即领取.png", threshold=0.6, record_pos=(0.054, 0.161), resolution=(2340, 1080))):
            print('{}--{}有立即领取按钮'.format(os.getpid(),self.device))
            touch(Template(r"wzjh立即领取.png", threshold=0.6, record_pos=(0.054, 0.161), resolution=(2340, 1080)))
            sleep(4)#已在充值档位页面
        if exists(Template(r"wzjh_6元档位.png", threshold=0.75,record_pos=(-0.374, -0.016), resolution=(2340, 1080))):
            print('{}_已在充值档位页面'.format(self.device))
            #创建线程获取日志
            t = threading.Thread(target=get_order_log.say,args=('eve',self.device))
            t.setDaemon(True)
            t.start()
            touch(Template(r"wzjh_6元档位.png", record_pos=(-0.374, -0.016), resolution=(2340, 1080)))
            if  self.poco(text="微信").wait(8).exists():
                print('{}--{}拉起支付方式弹窗成功'.format(os.getpid(),self.device))
                self.poco(text="微信").click()
                time.sleep(4)
            else:
                print('{}--{}拉起支付方式失败'.format(os.getpid(),self.device))
            t.join()
        else:
            print('{}在游戏内找不到元素_可能原因：实名制弹窗|游戏副本加载页|游戏不固定元素蒙层|网络异常弹框蒙层_请看截图'.format(self.device))
            img=Screencap.GetScreen(time.time(), self.device, "")
            return False,self.device+'在游戏内找不到元素_可能原因：实名制弹窗|游戏副本加载状态|游戏不固定元素蒙层|网络异常弹框蒙层等',img[img.find(r'superdalan.com//')+16:][:-4]
        print('{}___主线程结束___'.format(self.device))

    @order_handle_wzjh
    def place_order_R8AYIJWO99999999(self):
        '''华为畅享7_调起微信'''
        if exists(Template(r"wzjh首充按钮.png", threshold=0.55,record_pos=(0.333, -0.16), resolution=(1920, 1080))):
            print('{}--{}找到首充按钮'.format(os.getpid(),self.device))
            touch(Template(r"wzjh首充按钮.png", record_pos=(0.333, -0.16), resolution=(1920, 1080)))
            sleep(2.0)
        #有时候可能直接弹出立即领取页面
        if exists(Template(r"wzjh立即领取.png", threshold=0.6, record_pos=(0.054, 0.161), resolution=(1920, 1080))):
            print('{}--{}有立即领取按钮'.format(os.getpid(),self.device))
            touch(Template(r"wzjh立即领取.png", threshold=0.6, record_pos=(0.054, 0.161), resolution=(1920, 1080)))
            sleep(4)#已在充值档位页面
        if exists(Template(r"wzjh_6元档位.png", record_pos=(-0.374, -0.016), resolution=(1920, 1080))):
            print('{}_已在充值档位页面'.format(self.device))
            #创建线程获取日志
            t = threading.Thread(target=get_order_log.say,args=('eve',self.device))
            t.setDaemon(True)
            t.start()
            touch(Template(r"wzjh_6元档位.png", record_pos=(-0.374, -0.016), resolution=(1920, 1080)))
            if  self.poco(text="微信").wait(8).exists():
                print('{}--{}拉起支付方式弹窗成功'.format(os.getpid(),self.device))
                self.poco(text="微信").click()
                time.sleep(4)
            else:
                print('{}--{}拉起支付方式失败'.format(os.getpid(),self.device))
            t.join()
        else:
            print('{}在游戏内找不到元素_可能原因：实名制弹窗|游戏副本加载页|游戏不固定元素蒙层|网络异常弹框蒙层_请看截图'.format(self.device))
            img=Screencap.GetScreen(time.time(), self.device, "")
            return False,self.device+'在游戏内找不到元素_可能原因：实名制弹窗|游戏副本加载状态|游戏不固定元素蒙层|网络异常弹框蒙层等',img[img.find(r'superdalan.com//')+16:][:-4]
        print('{}___主线程结束___'.format(self.device))

    # except:
    #     img=Screencap.GetScreen(time.time(), device, "True")
    #     print('{}--{}--已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'.format(os.getpid(),device))
    #     return False,device+'由于网络原因，或手机反应慢到导致元素无法找到_超时',img[img.find(r'superdalan.com//')+16:][:-4]



if __name__ == "__main__":
    order_1=Order('54a4c6159804')
    print(order_1.place_order_54a4c6159804())
