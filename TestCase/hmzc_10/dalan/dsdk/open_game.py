#!/usr/bin/env python
# encoding: utf-8

from airtest.core.api import *
from dalan_tools import  Screencap
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

class Ddenglu(object):

    def __init__(self,device,name):
        self.device=device
        self.name=name
        connect_device("Android:///{}?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH".format(self.device))
        time.sleep(2)
        clear_app(name)
        auto_setup(__file__)
        self.poco=AndroidUiautomationPoco()
        sleep(2)
        start_app(name, activity = None)

    def hmzc_open_b5940085(self):#小米9
        sleep(8)
        for i in range(0,5):
            sleep(3)
            if self.poco(text="始终允许").exists():
                self.poco(text="始终允许").click()
            elif self.poco(text="确认").exists():
                self.poco(text="确认").click()
            else:
                print('{}启动游戏时_限弹框_{}'.format(self.device,i));break
        sleep(4)
        # if exists(Template(r"hmzc_开始游戏_mi9.png", record_pos=(-0.002, 0.706), resolution=(1080, 2340))):
        #     pass
        #     #touch(Template(r"hmzc_开始游戏_mi9.png", record_pos=(-0.002, 0.706), resolution=(1080, 2340)))
        try:
            #加载游戏_若包有热更时，有可能超时(已登录过大蓝游戏_或有缓存的)
            if self.poco(text="同意并进入游戏") or self.poco(text="帐号登录").wait(70).exists() :
                print('{}打开app成功==同意并进入游戏'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "")
                return True,'同意并进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print('{}找不到登录元素，或元素超时'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "")
                return False,'找不到登录元素_或元素超时',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)')
            img=Screencap.GetScreen(time.time(), self.device, "")
            return False,'主要是因为没有进入指定页面_',img[img.find(r'superdalan.com//')+16:][:-4]

    def hmzc_open_54a4c6159804(self):#小米4x
        sleep(10)
        for i in range(0,5):
            sleep(3)
            if self.poco(text="允许").exists():
                self.poco(text="允许").click()
            elif self.poco(text="确认").exists():
                self.poco(text="确认").click()
            else:
                print('{}启动游戏时_限弹框_{}'.format(self.device,i));break
        try:
            #加载游戏_若包有热更时，有可能超时(已登录过大蓝游戏_或有缓存的)
            if self.poco(text="同意并进入游戏") or self.poco(text="帐号登录").wait(70).exists() :
                print('{}打开app成功==同意并进入游戏'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "")
                return True,'同意并进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print('{}找不到登录元素，或元素超时'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "")
                return False,'找不到登录元素_或元素超时',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)')
            img=Screencap.GetScreen(time.time(), self.device, "")
            return False,'主要是因为没有进入指定页面_',img[img.find(r'superdalan.com//')+16:][:-4]

    def hmzc_open_QDY4C17818002168(self):#华为畅享7
        sleep(10)
        for i in range(0,5):
            sleep(3)
            if self.poco(text="始终允许").exists():
                self.poco(text="始终允许").click()
            elif self.poco(text="确认").exists():
                self.poco(text="确认").click()
            else:
                print('{}启动游戏时_限弹框_{}'.format(self.device,i));break
        try:
            #加载游戏_若包有热更时，有可能超时(已登录过大蓝游戏_或有缓存的)
            if self.poco(text="同意并进入游戏") or self.poco(text="帐号登录").wait(70).exists() :
                print('{}打开app成功==同意并进入游戏'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "")
                return True,'同意并进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print('{}找不到登录元素，或元素超时'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "")
                return False,'找不到登录元素_或元素超时',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)')
            img=Screencap.GetScreen(time.time(), self.device, "")
            return False,'主要是因为没有进入指定页面_',img[img.find(r'superdalan.com//')+16:][:-4]

    def hmzc_open_R8AYIJWO99999999(self):#小米note3
        sleep(10)
        for i in range(0,5):
            sleep(3)
            if self.poco(text="允许").exists():
                self.poco(text="允许").click()
            if self.poco(text="始终允许").exists():
                self.poco(text="始终允许").click()
            elif self.poco(text="确认").exists():
                self.poco(text="确认").click()
            else:
                print('{}启动游戏时_限弹框_{}'.format(self.device,i));break
        try:
            #加载游戏_若包有热更时，有可能超时(已登录过大蓝游戏_或有缓存的)
            if self.poco(text="同意并进入游戏") or self.poco(text="帐号登录").wait(70).exists() :
                print('{}打开app成功==同意并进入游戏'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "")
                return True,'同意并进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print('{}找不到登录元素，或元素超时'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "")
                return False,'找不到登录元素_或元素超时',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)')
            img=Screencap.GetScreen(time.time(), self.device, "")
            return False,'主要是因为没有进入指定页面_',img[img.find(r'superdalan.com//')+16:][:-4]

if __name__ == "__main__":
    denglu=Ddenglu('b5940085','com.nsmyfx.dalan')
    print(denglu.hmzc_open_b5940085())
    #Screencap.GetScreen(time.time(), config.devices(), "hm_deng_lu异常")#调用截图


