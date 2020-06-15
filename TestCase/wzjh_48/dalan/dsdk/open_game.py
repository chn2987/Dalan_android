#!/usr/bin/env python
# encoding: utf-8
import logging
from airtest.core.api import *
from dalan_tools import  Screencap
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

class Ddenglu(object):

    def __init__(self,device,name):
        self.device=device
        self.name=name
        logger = logging.getLogger("airtest")
        logger.setLevel(logging.ERROR)#过滤日志等级
        connect_device("Android:///{}?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH".format(device))
        time.sleep(2)
        auto_setup(__file__)
        self.poco=AndroidUiautomationPoco()
        clear_app(self.name)
        sleep(1.5)
        start_app(self.name, activity = None)
        sleep(8.0)

    def wzjh_open_R8AYIJWO99999999(self):
        '''判断游戏是否能够进入到登录页面_红米note3'''
        print(self.device,self.name)
        #判断是否有权限弹框
        if self.poco(text="允许").exists() or self.poco(text="确认").exists() or self.poco(text="关闭公告").exists()  or self.poco(desc="关闭公告").exists():#判断是否有权限弹框
            print('%s启动游戏时_有权限弹框'%self.device)
            for i in range(0,8):#弹框处理
                sleep(3.0)
                if self.poco(text="允许").exists():
                    self.poco(text="允许").click()
                elif self.poco(text="确认").exists():
                    self.poco(text="确认").click()
                elif self.poco(text="关闭公告").exists():
                    self.poco(text="关闭公告").click()
                elif self.poco(desc="关闭公告").exists():
                    self.poco(desc="关闭公告").click()
                else:
                    print("%s已授权_或无需授权=%d"%(self.device,i));break
        try:
            #加载游戏_若包有热更时，有可能超时(初次登录)
            if self.poco(text="选择登录方式").wait(80).exists():
                print('{}--{}打开app成功==到了登录页面'.format(os.getpid(),self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return True,'同意并进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print('{}--{}找不到登录元素，或元素超时'.format(os.getpid(),self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return False,'找不到登录元素_或元素超时',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('%s已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'%self.device)
            img=Screencap.GetScreen(time.time(), self.device, "True")
            return False,'主要是因为没有进入指定页面_',img[img.find(r'superdalan.com//')+16:][:-4]

    def wzjh_open_QDY4C17818002168(self):
        '''判断游戏是否能够进入到登录页面_华为畅享7'''
        print(self.device,self.name)
        if self.poco(text="始终允许").exists() or self.poco(text="确认").exists() or self.poco(text="关闭公告").exists():#判断是否有权限弹框
            print('%s启动游戏时_有权限弹框'%self.device)
            for i in range(0,8):#弹框处理
                sleep(3)
                if self.poco(text="始终允许").exists():
                    self.poco(text="始终允许").click()
                elif self.poco(text="确认").exists():
                    self.poco(text="确认").click()
                elif self.poco(text="关闭公告").exists():
                    self.poco(text="关闭公告").click()
                else:
                    print("%s--%s已授权_或无需授权=%d"%(os.getpid(),self.device,i));break
        try:
            #加载游戏_若包有热更时，有可能超时(初次登录)
            if self.poco(text="选择登录方式").wait(80).exists():
                print('{}--{}打开app成功==到了登录页面'.format(os.getpid(),self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return True,'同意并进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print('{}--{}找不到登录元素，或元素超时'.format(os.getpid(),self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return False,'找不到登录元素_或元素超时',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('%s已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'%self.device)
            img=Screencap.GetScreen(time.time(), self.device, "True")
            return False,'主要是因为没有进入指定页面_',img[img.find(r'superdalan.com//')+16:][:-4]

    def wzjh_open_54a4c6159804(self):
        '''判断游戏是否能够进入到登录页面_红米note4x'''
        print(self.device,self.name)
         #判断是否有权限弹框
        if self.poco(text="允许").exists() or self.poco(text="确认").exists() or self.poco(text="关闭公告").exists():#判断是否有权限弹框
            print('%s启动游戏时_有权限弹框'%self.device)
            for i in range(0,8):#弹框处理
                sleep(3)
                if self.poco(text="允许").exists():
                    self.poco(text="允许").click()
                elif self.poco(text="确认").exists():
                    self.poco(text="确认").click()
                elif self.poco(text="关闭公告").exists():
                    self.poco(text="关闭公告").click()
                else:
                    print("%s已授权_或无需授权=%d"%(self.device,i));break
        try:
            #加载游戏_若包有热更时，有可能超时(初次登录)
            if self.poco(text="选择登录方式").wait(80).exists():
                print('{}--{}打开app成功==到了登录页面'.format(os.getpid(),self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return True,'同意并进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print('{}--{}找不到登录元素，或元素超时'.format(os.getpid(),self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return False,'找不到登录元素_或元素超时',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('%s已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'%self.device)
            img=Screencap.GetScreen(time.time(), self.device, "True")
            return False,'主要是因为没有进入指定页面_',img[img.find(r'superdalan.com//')+16:][:-4]

    def wzjh_open_b5940085(self):
        '''判断游戏是否能够进入到登录页面_小米9'''
        print(self.device,self.name)
         #判断是否有权限弹框
        if self.poco(text="始终允许").exists() or self.poco(text="确认").exists() or self.poco(text="关闭公告").exists():#判断是否有权限弹框
            print('%s启动游戏时_有权限弹框'%self.device)
            for i in range(0,8):#弹框处理
                sleep(3)
                if self.poco(text="始终允许").exists():
                    self.poco(text="始终允许").click()
                elif self.poco(text="确认").exists():
                    self.poco(text="确认").click()
                elif self.poco(text="关闭公告").exists():
                    self.poco(text="关闭公告").click()
                else:
                    print("%s已授权_或无需授权=%d"%(self.device,i));break
        try:
            #加载游戏_若包有热更时，有可能超时(初次登录)
            if self.poco(text="选择登录方式").wait(80).exists():
                print('{}--{}打开app成功==到了登录页面'.format(os.getpid(),self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return True,'同意并进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print('{}--{}找不到登录元素，或元素超时'.format(os.getpid(),self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return False,'找不到登录元素_或元素超时',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('%s已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'%self.device)
            img=Screencap.GetScreen(time.time(), self.device, "True")
            return False,'主要是因为没有进入指定页面_',img[img.find(r'superdalan.com//')+16:][:-4]



if __name__ == "__main__":
    denglu=Ddenglu('54a4c6159804','com.tencent.tmgp.ttqymxdxc')
    print(eval('denglu.wzjh_open_'+'54a4c6159804()'))
    # #Screencap.GetScreen(time.time(), config.devices(), "hm_deng_lu异常")#调用截图