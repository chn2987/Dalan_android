#!/usr/bin/env python
# encoding: utf-8
__author__ = "晨晨"
import logging
import threading,re
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from TestCase.hmzc_10.dalan.dsdk import get_order_log
from dalan_tools import  Screencap


class Order(object):

    def __init__(self,device):
        self.device=device
        logger = logging.getLogger("airtest")
        logger.setLevel(logging.ERROR)
        connect_device("Android:///{}?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH".format(device))
        time.sleep(2)
        auto_setup(__file__)
        self.poco=AndroidUiautomationPoco()
        sleep(1.5)

    def order_handle(func):
        def wrapped(self,*arg,**kwargs):
            result=func(self)#调用函数
            if result is None:
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

    @order_handle
    def order_weixi_54a4c6159804(self):#小米4x
        try:
            print('{}__在游戏首页'.format(self.device))
            self.poco().click((0.850,0.105))#点击-进入充值入口
            sleep(3.0)
            if exists(Template(r"hmzc_60档位.png", record_pos=(-0.312, 0.09), resolution=(1080, 1920))):
                print('{}__已在充值档位页面'.format(self.device))
                #创建线程获取日志
                t = threading.Thread(target=get_order_log.say,args=('eve',self.device))
                t.setDaemon(True)
                t.start()
                touch(Template(r"hmzc_60档位.png", record_pos=(-0.312, 0.09), resolution=(1080, 1920)))
                if  self.poco(text="微信").wait(8).exists():
                    print('{}--{}拉起支付方式弹窗成功'.format(os.getpid(),self.device))
                    self.poco(text="微信").click()
                    time.sleep(4)
                else:
                    print('{}--{}拉起支付方式失败'.format(os.getpid(),self.device))
                t.join()
            else:
                print('{}进入充值档位失败_请看截图'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "")
                return False, self.device+'进入充值档位失败_请看截图',img[img.find(r'superdalan.com//')+16:][:-4]
            print('{}___主线程结束___'.format(self.device))

        except:
            img=Screencap.GetScreen(time.time(), self.device, "")
            print('{}--{}--已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'.format(os.getpid(),device))
            return False,device+'由于网络原因，或手机反应慢到导致元素无法找到_超时',img[img.find(r'superdalan.com//')+16:][:-4]

    @order_handle
    def order_weixi_R8AYIJWO99999999(self):#小米note3
        try:
            print('{}__在游戏首页'.format(self.device))
            self.poco().click((0.850,0.105))#点击-进入充值入口
            sleep(4.0)
            if exists(Template(r"hmzc_60档位.png", record_pos=(-0.312, 0.09), resolution=(1080, 1920))):
                print('{}__已在充值档位页面'.format(self.device))
                #创建线程获取日志
                t = threading.Thread(target=get_order_log.say,args=('eve',self.device))
                t.setDaemon(True)
                t.start()
                touch(Template(r"hmzc_60档位.png", record_pos=(-0.312, 0.09), resolution=(1080, 1920)))
                if  self.poco(text="微信").wait(8).exists():
                    print('{}--{}拉起支付方式弹窗成功'.format(os.getpid(),self.device))
                    self.poco(text="微信").click()
                    time.sleep(4)
                else:
                    print('{}--{}拉起支付方式失败'.format(os.getpid(),self.device))
                t.join()
            else:
                print('{}进入充值档位失败_请看截图'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "")
                return False, self.device+'进入充值档位失败_请看截图',img[img.find(r'superdalan.com//')+16:][:-4]
            print('{}___主线程结束___'.format(self.device))

        except:
            img=Screencap.GetScreen(time.time(), self.device, "")
            print('{}--{}--已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'.format(os.getpid(),device))
            return False,device+'由于网络原因，或手机反应慢到导致元素无法找到_超时',img[img.find(r'superdalan.com//')+16:][:-4]

    @order_handle
    def order_weixi_QDY4C17818002168(self):#华为畅享7
        print('{}__在游戏首页'.format(self.device))
        self.poco().click((0.850,0.105))#点击-进入充值入口
        sleep(3.0)
        if exists(Template(r"hmzc_60档位.png", record_pos=(-0.312, 0.09), resolution=(1080, 1920))):
            print('{}__已在充值档位页面'.format(self.device))
            #创建线程获取日志
            t = threading.Thread(target=get_order_log.say,args=('eve',self.device))
            t.setDaemon(True)
            t.start()
            touch(Template(r"hmzc_60档位.png", record_pos=(-0.312, 0.09), resolution=(1080, 1920)))
            if  self.poco(text="微信").wait(8).exists():
                print('{}--{}拉起支付方式弹窗成功'.format(os.getpid(),self.device))
                self.poco(text="微信").click()
                time.sleep(4)
            else:
                print('{}--{}拉起支付方式失败'.format(os.getpid(),self.device))
            t.join()
        else:
            print('{}进入充值档位失败_请看截图'.format(self.device))
            img=Screencap.GetScreen(time.time(), self.device, "")
            return False, self.device+'进入充值档位失败_请看截图',img[img.find(r'superdalan.com//')+16:][:-4]
        print('{}___主线程结束___'.format(self.device))

    @order_handle
    def order_weixi_b5940085(self):
        print('{}__在游戏首页'.format(self.device))
        touch((844,445))#点击-进入充值入口
        sleep(3.0)
        if exists(Template(r"hmzc_60档位.png", record_pos=(-0.312, 0.09), resolution=(1080, 1920))):
            print('{}__已在充值档位页面'.format(self.device))
            #创建线程获取日志
            t = threading.Thread(target=get_order_log.say,args=('eve',self.device))
            t.setDaemon(True)
            t.start()
            touch(Template(r"hmzc_60档位.png", record_pos=(-0.312, 0.09), resolution=(1080, 1920)))
            if  self.poco(text="微信").wait(8).exists():
                print('{}--{}拉起支付方式弹窗成功'.format(os.getpid(),self.device))
                self.poco(text="微信").click()
                time.sleep(4)
            else:
                print('{}--{}拉起支付方式失败'.format(os.getpid(),self.device))
            t.join()
        else:
            print('{}进入充值档位失败_请看截图'.format(self.device))
            img=Screencap.GetScreen(time.time(), self.device, "")
            return False, self.device+'进入充值档位失败_请看截图',img[img.find(r'superdalan.com//')+16:][:-4]
        print('{}___主线程结束___'.format(self.device))




if __name__ == "__main__":
    order_1=Order('R8AYIJWO99999999')
    print(order_1.order_weixi_R8AYIJWO99999999())
