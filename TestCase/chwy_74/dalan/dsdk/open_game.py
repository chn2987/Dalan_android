#!/usr/bin/env python
# encoding: utf-8
from airtest.core.api import *
from dalan_tools import  Screencap,config
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

class Ddenglu(object):

    def __init__(self,device,name):
        self.device=device
        self.name=name
        connect_device("Android:///" +device)
        time.sleep(2)
        auto_setup(__file__)
        self.poco=AndroidUiautomationPoco()
        sleep(1.5)
        start_app(name, activity = None)

    def popup(func):
        '''处理权限弹框'''
        def wrapped(self,*arg,**kwargs):
            sleep(12)
            if self.poco(text="始终允许").exists() or self.poco(text="确认").exists() or self.poco(text="关闭公告").exists() or self.poco(text="允许").exists():#判断是否有权限弹框
                print('{}装饰器处理弹窗'.format(self.device))
                for i in range(0,6):#弹框处理
                    sleep(3)
                    if self.poco(text="始终允许").exists():
                        self.poco(text="始终允许").click()
                    elif self.poco(text="允许").exists():
                        self.poco(text="允许").click()
                    elif self.poco(text="关闭公告").exists():#处理公告弹框
                        self.poco(text="关闭公告").click()
                    elif self.poco(text="确认").exists():#处理公告弹框
                        self.poco(text="确认").click()
                    else:
                        print("{}已授权_或无需授权_{}次".format(self.device,i));break
            return func(self)#装饰完成，调用函数
        return wrapped

    @popup
    def mxd_open_b5940085(self):#小米9
        '''判断游戏是否能够进入到登录页面'''
        try:
            try:
                if wait(Template(r"mxd_热更按钮.png", record_pos=(0.128, 0.146), resolution=(1920, 1080)),12):#判断热更新
                    print('{}_有热更资源'.format(self.device))
                    self.poco().click((0.616,0.745))#点击热更
            except:
                pass
            if self.poco(text="帐号登录").wait(60).exists():
                print('{}-打开app成功==在选择登录方式页面'.format(self.device))
                img=Screencap.GetScreen(time.time(),self.device, "True")
                return True,'进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            elif self.poco(text="同意并进入游戏").exists():
                print('{}打开app成功==同意并进入游戏'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return True,'同意并进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            #新手机或大蓝缓存被清理
            elif self.poco(text="进入游戏").exists():
                 print('{}-打开app成功==进入游戏'.format(self.device))
                 img=Screencap.GetScreen(time.time(),self.device, "True")
                 return True,'进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print('{}找不到登录元素，或元素超时'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return False,'找不到登录元素_或元素超时',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('{}已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'.format(self.device))
            img=Screencap.GetScreen(time.time(), self.device, "True")
            return False,'主要是因为没有进入指定页面_',img[img.find(r'superdalan.com//')+16:][:-4]

    @popup
    def mxd_open_54a4c6159804(self):#小米4x
        '''判断游戏是否能够进入到登录页面'''
        try:
            try:
                if wait(Template(r"mxd_热更按钮.png", record_pos=(0.128, 0.146), resolution=(1920, 1080)),12):#判断热更新
                    print('{}_有热更资源'.format(self.device))
                    self.poco().click((0.616,0.745))#点击热更
            except:pass
            if self.poco(text="帐号登录").wait(60).exists():
                print('{}-打开app成功==在选择登录方式页面'.format(self.device))
                img=Screencap.GetScreen(time.time(),self.device, "True")
                return True,'进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            elif self.poco(text="同意并进入游戏").exists():
                print('{}打开app成功==同意并进入游戏'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return True,'同意并进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            #新手机或大蓝缓存被清理
            elif self.poco(text="进入游戏").exists():
                 print('{}-打开app成功==进入游戏'.format(self.device))
                 img=Screencap.GetScreen(time.time(),self.device, "True")
                 return True,'进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print('{}找不到登录元素，或元素超时'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return False,'找不到登录元素_或元素超时',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('{}已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'.format(self.device))
            img=Screencap.GetScreen(time.time(), self.device, "True")
            return False,'主要是因为没有进入指定页面_',img[img.find(r'superdalan.com//')+16:][:-4]

    @popup
    def mxd_open_R8AYIJWO99999999(self):#小米note3
        '''判断游戏是否能够进入到登录页面'''
        if self.poco(text="始终允许").exists():#华为
            for i in range(0,5):#弹框处理
                sleep(3)
                if self.poco(text="始终允许").exists():
                    self.poco(text="始终允许").click()
                elif self.poco(desc="关闭公告").exists():#小米note3
                    self.poco(desc="关闭公告").click()
                else:
                    print("{}已授权_或无需授权".format(self.device));break
        try:
            try:
                if wait(Template(r"mxd_热更按钮.png", record_pos=(0.128, 0.146), resolution=(1920, 1080)),12):#判断热更新
                    print('{}_有热更资源'.format(self.device))
                    self.poco().click((0.616,0.745))#点击热更
            except:pass
            if self.poco(text="帐号登录").wait(60).exists():
                print('{}-打开app成功==在选择登录方式页面'.format(self.device))
                img=Screencap.GetScreen(time.time(),self.device, "True")
                return True,'进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            elif self.poco(text="同意并进入游戏").exists():
                print('{}打开app成功==同意并进入游戏'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return True,'同意并进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            #新手机或大蓝缓存被清理
            elif self.poco(text="进入游戏").exists():
                 print('{}-打开app成功==进入游戏'.format(self.device))
                 img=Screencap.GetScreen(time.time(),self.device, "True")
                 return True,'进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print('{}找不到登录元素，或元素超时'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return False,'找不到登录元素_或元素超时',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('{}已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'.format(self.device))
            img=Screencap.GetScreen(time.time(), self.device, "True")
            return False,'主要是因为没有进入指定页面_',img[img.find(r'superdalan.com//')+16:][:-4]

    @popup
    def mxd_open_QDY4C17818002168(self):#华为畅享7
        '''判断游戏是否能够进入到登录页面'''
        try:
            try:
                if wait(Template(r"mxd_热更按钮.png", record_pos=(0.128, 0.146), resolution=(1920, 1080)),12):#判断热更新
                    print('{}_有热更资源'.format(self.device))
                    self.poco().click((0.616,0.745))#点击热更
            except:pass
            if self.poco(text="帐号登录").wait(60).exists():
                print('{}-打开app成功==在选择登录方式页面'.format(self.device))
                img=Screencap.GetScreen(time.time(),self.device, "True")
                return True,'进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            elif self.poco(text="同意并进入游戏").exists():
                print('{}打开app成功==同意并进入游戏'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return True,'同意并进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            #新手机或大蓝缓存被清理
            elif self.poco(text="进入游戏").exists():
                 print('{}-打开app成功==进入游戏'.format(self.device))
                 img=Screencap.GetScreen(time.time(),self.device, "True")
                 return True,'进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print('{}找不到登录元素，或元素超时'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return False,'找不到登录元素_或元素超时',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('{}已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'.format(self.device))
            img=Screencap.GetScreen(time.time(), self.device, "True")
            return False,'主要是因为没有进入指定页面_',img[img.find(r'superdalan.com//')+16:][:-4]


if __name__ == "__main__":
    #denglu=Ddenglu('b5940085','com.tencent.tmgp.ttqymxw')
    denglu=Ddenglu('54a4c6159804','com.tencent.tmgp.ttqymxdxc')
    print(eval('denglu.mxd_open_'+'54a4c6159804()'))
    #Screencap.GetScreen(time.time(),'b5940085', "")#调用截图


