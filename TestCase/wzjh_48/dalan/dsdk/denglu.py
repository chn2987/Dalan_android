#!/usr/bin/env python
# encoding: utf-8
import logging
from dalan_tools import config
from airtest.core.api import *
from dalan_tools import  Screencap
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)#过滤日志等级

#_____________________________________________我在江湖游戏________________________________________

class Ddenglu_2(object):
    def __init__(self,device,name):
        self.device=device
        self.name=name
        connect_device("Android:///{}?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH".format(device))
        auto_setup(__file__)
        self.poco=AndroidUiautomationPoco()
        sleep(1.8)
    def popup_wzjh(func):
        '''登录预处理'''
        def wrapped(self,*arg,**kwargs):
            if self.poco(text="帐号登录").exists():
                print(self.device+'在登录方式选择页面_有账号登录元素')
                self.poco("com.dalan.lgh:id/dalan_agreement_check").click()#默认没有勾选需要勾选
                self.poco(text="帐号登录").click()
                sleep(3.0)
                #判断是否还在当前页面，如果在说明反复勾选了
                if self.poco(text="帐号登录").exists():
                    print(self.device+'需要反向勾选用户协议')
                    self.poco("com.dalan.lgh:id/dalan_agreement_check").click()#反向勾选
                    sleep(1.5)
                    self.poco(text="帐号登录").click()
                    sleep(3.0)
                if  self.poco("com.dalan.lgh:id/dalan_password_input").exists():#判断账号框是否存在
                    for i in range(len(config.devices())):
                        if self.device in config.devices()[i]:
                            print('{}设备对应账号{}'.format(self.device,config.number()[i]))
                            self.poco("com.dalan.lgh:id/dalan_password_input").set_text(config.number()[i])
                            sleep(1.5)
                    self.poco(text="密码").set_text('123456')
                    sleep(1.5)
                    self.poco(text="进入游戏").click()
                    sleep(4.5)
            return func(self)#装饰完成，调用函数
        return wrapped

    @popup_wzjh
    def wzjh_deng_lu_54a4c6159804(self):#小米4x
        #判断是否有权限弹框
        try:
            if exists(Template(r"wzjh公告.png", threshold=0.60,record_pos=(0.003, -0.226), resolution=(1920, 1080))):#如果有公告就关闭
                touch(Template(r"wzjh关闭公告.png", record_pos=(0.351, -0.226), resolution=(1920, 1080)))
                print(self.device+'游戏前有公告')
                sleep(4)
            if exists(Template(r"wzjh进入游戏.png", record_pos=(-0.01, 0.136), resolution=(1920, 1080))):
                print(self.device+'进入登录页_有进入游戏按钮')
                touch(Template(r"wzjh进入游戏.png", record_pos=(-0.01, 0.136), resolution=(1920, 1080)))
                sleep(5)
                if exists(Template(r"wzjh_创建_2.png", record_pos=(0.362, 0.22), resolution=(1280, 720))) or exists(Template(r"wzjh创角.png", record_pos=(0.317, 0.194), resolution=(1920, 1080))):
                    print(self.device+'进入创角界面')
                    self.poco().click((0.860,0.885))
                    self.poco().click((0.860,0.885))#点击进入游戏
                    sleep(4)
                for i in range(0,14):
                    print(self.device+'循环判断游戏内元素')
                    sleep(3)
                    if  exists(Template(r"wzjh游戏内元素.png", record_pos=(-0.101, -0.06), resolution=(1920, 1080))) or exists(Template(r"wzjh首充按钮.png", record_pos=(0.331, -0.158), resolution=(1920, 1080))):
                        print(self.device+'登录游戏成功')
                        img=Screencap.GetScreen(time.time(), self.device, "True")
                        return True,'登录成功',img[img.find(r'superdalan.com//')+16:][:-4]
                    elif i>12:
                        print(self.device+'进入游戏异常_找不到元素')
                        img=Screencap.GetScreen(time.time(), self.device, "True")
                        return False,self.device+'找不到游戏内元素_未能成功进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print(self.device+'找不到进入游戏按钮(可能账号登录异常)_请看截图')
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return False,self.device+'找不到进入游戏按钮(可能账号登录异常)_请看截图',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print(self.device+'-已走异常流程_截图异常页面___(原因：主要是因为没有进入指定页面_)')
            img=Screencap.GetScreen(time.time(), self.device, "True")
            return False,self.device+'由于网络原因，或手机反应慢到导致元素无法找到',img[img.find(r'superdalan.com//')+16:][:-4]

    @popup_wzjh
    def wzjh_deng_lu_QDY4C17818002168(self):#华为畅享7
        #判断是否有权限弹框
        try:
            if exists(Template(r"wzjh公告.png", threshold=0.60,record_pos=(0.003, -0.226), resolution=(1920, 1080))):#如果有公告就关闭
                touch(Template(r"wzjh关闭公告.png", record_pos=(0.351, -0.226), resolution=(1920, 1080)))
                print(self.device+'游戏前有公告')
                sleep(4)
            if exists(Template(r"wzjh进入游戏.png", record_pos=(-0.01, 0.136), resolution=(1920, 1080))):
                print(self.device+'进入登录页_有进入游戏按钮')
                touch(Template(r"wzjh进入游戏.png", record_pos=(-0.01, 0.136), resolution=(1920, 1080)))
                sleep(5)
                if exists(Template(r"wzjh_创建_2.png", record_pos=(0.362, 0.22), resolution=(1280, 720))) or exists(Template(r"wzjh创角.png", record_pos=(0.317, 0.194), resolution=(1920, 1080))):
                    print(self.device+'进入创角界面')
                    self.poco().click((0.860,0.885))
                    self.poco().click((0.860,0.885))#点击进入游戏
                    sleep(4)
                for i in range(0,14):
                    print(self.device+'循环判断游戏内元素')
                    sleep(3)
                    if  exists(Template(r"wzjh弹框sdk.png",record_pos=(-0.486, 0.031), resolution=(1920, 1080))) or exists(Template(r"wzjh游戏内元素.png", record_pos=(-0.101, -0.06), resolution=(1920, 1080))) or exists(Template(r"wzjh首充按钮.png", record_pos=(0.331, -0.158), resolution=(1920, 1080))):
                        print(self.device+'登录游戏成功')
                        sleep(1)
                        img=Screencap.GetScreen(time.time(), self.device, "True")
                        return True,'登录成功',img[img.find(r'superdalan.com//')+16:][:-4]
                    elif i>12:
                        print(self.device+'进入游戏异常_找不到元素')
                        img=Screencap.GetScreen(time.time(), self.device, "True")
                        return False,self.device+'找不到游戏内元素_未能成功进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print(self.device+'找不到进入游戏按钮(可能账号登录异常)_请看截图')
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return False,self.device+'找不到进入游戏按钮(可能账号登录异常)_请看截图',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print(self.device+'-已走异常流程_截图异常页面___(原因：主要是因为没有进入指定页面_)')
            img=Screencap.GetScreen(time.time(), self.device, "True")
            return False,self.device+'由于网络原因，或手机反应慢到导致元素无法找到',img[img.find(r'superdalan.com//')+16:][:-4]

    @popup_wzjh
    def wzjh_deng_lu_R8AYIJWO99999999(self):#小米note3
        #判断是否有权限弹框
        try:
            if exists(Template(r"wzjh公告.png", threshold=0.60,record_pos=(0.003, -0.226), resolution=(1920, 1080))):#如果有公告就关闭
                touch(Template(r"wzjh关闭公告.png", record_pos=(0.351, -0.226), resolution=(1920, 1080)))
                print(self.device+'游戏前有公告')
                sleep(4)
            if exists(Template(r"wzjh进入游戏.png", record_pos=(-0.01, 0.136), resolution=(1920, 1080))):
                print(self.device+'进入登录页_有进入游戏按钮')
                touch(Template(r"wzjh进入游戏.png", record_pos=(-0.01, 0.136), resolution=(1920, 1080)))
                sleep(5)
                if exists(Template(r"wzjh_创建_2.png", record_pos=(0.362, 0.22), resolution=(1280, 720))) or exists(Template(r"wzjh创角.png", record_pos=(0.317, 0.194), resolution=(1920, 1080))):
                    print(self.device+'进入创角界面')
                    self.poco().click((0.860,0.885))
                    self.poco().click((0.860,0.885))#点击进入游戏
                    sleep(4)
                for i in range(0,14):
                    print(self.device+'循环判断游戏内元素')
                    sleep(3)
                    if  exists(Template(r"wzjh弹框sdk.png",record_pos=(-0.486, 0.031), resolution=(1920, 1080))) or exists(Template(r"wzjh游戏内元素.png", record_pos=(-0.101, -0.06), resolution=(1920, 1080))) or exists(Template(r"wzjh首充按钮.png", record_pos=(0.331, -0.158), resolution=(1920, 1080))):
                        print(self.device+'登录游戏成功')
                        sleep(1)
                        img=Screencap.GetScreen(time.time(), self.device, "True")
                        return True,'登录成功',img[img.find(r'superdalan.com//')+16:][:-4]
                    elif i>12:
                        print(self.device+'进入游戏异常_找不到元素')
                        img=Screencap.GetScreen(time.time(), self.device, "True")
                        return False,self.device+'找不到游戏内元素_未能成功进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print(self.device+'找不到进入游戏按钮(可能账号登录异常)_请看截图')
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return False,self.device+'找不到进入游戏按钮(可能账号登录异常)_请看截图',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print(self.device+'-已走异常流程_截图异常页面___(原因：主要是因为没有进入指定页面_)')
            img=Screencap.GetScreen(time.time(), self.device, "True")
            return False,self.device+'由于网络原因，或手机反应慢到导致元素无法找到',img[img.find(r'superdalan.com//')+16:][:-4]

    @popup_wzjh
    def wzjh_deng_lu_b5940085(self):#小米9
    #判断是否有权限弹框
        try:
            if exists(Template(r"wzjh公告.png", threshold=0.60,record_pos=(0.003, -0.226), resolution=(2340, 1080))):#如果有公告就关闭
                touch(Template(r"wzjh关闭公告.png", record_pos=(0.351, -0.226), resolution=(2340, 1080)))
                print(self.device+'游戏前有公告')
                sleep(4)
            if exists(Template(r"wzjh_进入游戏_mi9.png", record_pos=(-0.011, 0.106), resolution=(2340, 1080))):
                print(self.device+'进入登录页_有进入游戏按钮')
                touch(Template(r"wzjh_进入游戏_mi9.png", record_pos=(-0.011, 0.106), resolution=(2340, 1080)))
                sleep(5)
                if exists(Template(r"wzjh_创建_2.png", record_pos=(0.362, 0.22), resolution=(2340, 1080))) or exists(Template(r"wzjh创角.png", record_pos=(0.317, 0.194), resolution=(2340, 1080))):
                    print(self.device+'进入创角界面')
                    touch((2070,960))
                    touch((2070,960))#点击进入游戏
                    sleep(4)
                for i in range(0,14):
                    print(self.device+'循环判断游戏内元素')
                    sleep(3)
                    if  exists(Template(r"wzjh弹框sdk.png",record_pos=(-0.486, 0.031), resolution=(2340, 1080))) or exists(Template(r"wzjh游戏内元素.png", record_pos=(-0.101, -0.06), resolution=(2340, 1080))) or exists(Template(r"wzjh首充按钮.png", record_pos=(0.331, -0.158), resolution=(2340, 1080))):
                        print(self.device+'登录游戏成功')
                        sleep(1)
                        img=Screencap.GetScreen(time.time(), self.device, "True")
                        return True,'登录成功',img[img.find(r'superdalan.com//')+16:][:-4]
                    elif i>12:
                        print(self.device+'进入游戏异常_找不到元素')
                        img=Screencap.GetScreen(time.time(), self.device, "True")
                        return False,self.device+'找不到游戏内元素_未能成功进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print(self.device+'找不到进入游戏按钮(可能账号登录异常)_请看截图')
                img=Screencap.GetScreen(time.time(), self.device, "True")
                return False,self.device+'找不到进入游戏按钮(可能账号登录异常)_请看截图',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print(self.device+'-已走异常流程_截图异常页面___(原因：主要是因为没有进入指定页面_)')
            img=Screencap.GetScreen(time.time(), self.device, "True")
            return False,self.device+'由于网络原因，或手机反应慢到导致元素无法找到',img[img.find(r'superdalan.com//')+16:][:-4]



if __name__ == "__main__":
    denglu=Ddenglu_2('b5940085','com.dalan.zyrg.toutiao2')
    denglu.wzjh_deng_lu_b5940085()
    #Screencap.GetScreen(time.time(), '54a4c6159804', "test_01_of_10")#手动截图
