#!/usr/bin/env python
# encoding: utf-8
from airtest.core.api import *
from dalan_tools import  Screencap,config
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

class Ddenglu_2(object):

    def __init__(self,device,name):
        self.device=device
        self.name=name
        connect_device("Android:///{}?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH".format(device))
        auto_setup(__file__)
        self.poco=AndroidUiautomationPoco()
        sleep(1.5)

    def hmzc_deng_lu_QDY4C17818002168(self):#华为畅享7
        try:
            if self.poco(text="帐号登录").exists():
                print('{}__欢迎进入登录选择方式页面'.format(self.device))
                sleep(2)
                self.poco("com.dalan.lgh:id/dalan_agreement_check").click()#默认没有勾选需要勾选
                sleep(2)
                self.poco(text="帐号登录").click()
                sleep(3)
                if self.poco(text="帐号登录").exists():
                    print('{}_需要反向勾选协议'.format(self.device));sleep(1.5)
                    self.poco("com.dalan.lgh:id/dalan_agreement_check").click()#默认没有勾选需要勾选
                    sleep(1.5)
                    self.poco(text="帐号登录").click()
                    sleep(3)
                #判断并输入帐号
                if  self.poco(textMatches='^忘记密码.*$').exists():
                    for i in range(len(config.devices())):#迭代设备个数
                        if self.device in config.devices()[i]:
                            print('已在登录_在输入账号密码页面_{}设备对应账号{}'.format(self.device,config.number()[i]))
                            self.poco('com.dalan.lgh:id/dalan_password_input').set_text(config.number()[i])
                    self.poco('com.dalan.lgh:id/dalan_msg_input').set_text('123456')
                    self.poco(text="进入游戏").click()
                    sleep(5.0)
                sleep(2.0)
                if exists(Template(r"hmzc_公告.png", record_pos=(0.001, 0.499), resolution=(720, 1280))):
                    print('{}游戏前_登录页有公告'.format(self.device))
                    touch(Template(r"hmzc_公告.png", record_pos=(0.001, 0.499), resolution=(720, 1280)))
                    sleep(2.5)
                if exists(Template(r"hmzc_开始游戏.png", record_pos=(0.004, 0.669), resolution=(720, 1280))):
                    touch(Template(r"hmzc_开始游戏.png", record_pos=(0.004, 0.669), resolution=(720, 1280)))
                    sleep(3)
                if exists(Template(r"hmzc_创角页面.png", record_pos=(-0.004, 0.767), resolution=(720, 1280))):
                    print('{}__已在创角页面_需要创角'.format(self.device))
                    touch(Template(r"hmzc_创角页面.png", record_pos=(-0.004, 0.767), resolution=(720, 1280)))
                    sleep(4);stop_app(self.name)#杀掉进程可跳过新手
                    sleep(2);start_app(self.name, activity = None)
                    sleep(15)
                #不走创角流程
                elif wait(Template(r"hmzc_游戏内断言.png", record_pos=(0.426, -0.846), resolution=(720, 1280)),timeout=20):
                    print('{}__登录游戏成功'.format(self.device))
                    img=Screencap.GetScreen(time.time(), self.device, "")
                    return True,'登录游戏成功',img[img.find(r'superdalan.com//')+16:][:-4]
            #创角后的操作
            if exists(Template(r"hmzc_公告.png", record_pos=(0.001, 0.499), resolution=(720, 1280))):
                print('{}_再次启动跳新手--登录页有公告'.format(self.device))
                touch(Template(r"hmzc_公告.png", record_pos=(0.001, 0.499), resolution=(720, 1280)))
                sleep(2.5)
            if exists(Template(r"hmzc_开始游戏.png", record_pos=(0.004, 0.669), resolution=(720, 1280))):
                touch(Template(r"hmzc_开始游戏.png", record_pos=(0.004, 0.669), resolution=(720, 1280)))
                if wait(Template(r"hmzc_游戏内断言.png", record_pos=(0.426, -0.846), resolution=(720, 1280)),timeout=25):
                    print('{}__登录游戏成功'.format(self.device))
                    img=Screencap.GetScreen(time.time(), self.device, "")
                    return True,'登录游戏成功',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print('{}__找不到游戏内元素_未能成功进入游戏'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "")
                return False,'找不到游戏内元素_未能成功进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('{}__已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'.format(self.device))
            img=Screencap.GetScreen(time.time(), self.device, "")
            return False,'由于网络原因，或手机反应慢到导致元素无法找到',img[img.find(r'superdalan.com//')+16:][:-4]

    def hmzc_deng_lu_54a4c6159804(self):#小米4x
        try:
            if self.poco(text="帐号登录").exists():
                print('{}__欢迎进入登录选择方式页面'.format(self.device));sleep(1.5)
                self.poco("com.dalan.lgh:id/dalan_agreement_check").click()#默认没有勾选需要勾选
                sleep(1.5)
                self.poco(text="帐号登录").click()
                sleep(3)
                #二次判断
                if self.poco(text="帐号登录").exists():
                    print('{}_需要反向勾选协议'.format(self.device));sleep(1.5)
                    self.poco("com.dalan.lgh:id/dalan_agreement_check").click()#默认没有勾选需要勾选
                    sleep(1.5)
                    self.poco(text="帐号登录").click()
                    sleep(3)
                #判断并输入帐号
                if  self.poco(textMatches='^忘记密码.*$').exists():
                    for i in range(len(config.devices())):#迭代设备个数
                        if self.device in config.devices()[i]:
                            print('已在登录_在输入账号密码页面_{}设备对应账号{}'.format(self.device,config.number()[i]))
                            self.poco('com.dalan.lgh:id/dalan_password_input').set_text(config.number()[i])
                    self.poco('com.dalan.lgh:id/dalan_msg_input').set_text('123456')
                    self.poco(text="进入游戏").click()
                    sleep(5.0)
                sleep(2.0)
                if exists(Template(r"hmzc_公告.png", record_pos=(0.001, 0.499), resolution=(720, 1280))):
                    print('{}游戏前_登录页有公告'.format(self.device))
                    touch(Template(r"hmzc_公告.png", record_pos=(0.001, 0.499), resolution=(720, 1280)))
                    sleep(2.5)
                if exists(Template(r"hmzc_开始游戏.png", record_pos=(0.004, 0.669), resolution=(720, 1280))):
                    touch(Template(r"hmzc_开始游戏.png", record_pos=(0.004, 0.669), resolution=(720, 1280)))
                    sleep(3)
                if exists(Template(r"hmzc_创角页面.png", record_pos=(-0.004, 0.767), resolution=(720, 1280))):
                    print('{}__已在创角页面_需要创角'.format(self.device))
                    touch(Template(r"hmzc_创角页面.png", record_pos=(-0.004, 0.767), resolution=(720, 1280)))
                    sleep(4);stop_app(self.name)#杀掉进程可跳过新手
                    sleep(2);start_app(self.name, activity = None)
                    sleep(15)
                #不走创角流程
                elif wait(Template(r"hmzc_游戏内断言.png", record_pos=(0.426, -0.846), resolution=(720, 1280)),timeout=20):
                    print('{}__登录游戏成功'.format(self.device))
                    img=Screencap.GetScreen(time.time(), self.device, "")
                    return True,'登录游戏成功',img[img.find(r'superdalan.com//')+16:][:-4]
            #创角后的操作
            if exists(Template(r"hmzc_公告.png", record_pos=(0.001, 0.499), resolution=(720, 1280))):
                print('{}_再次启动跳新手--登录页有公告'.format(self.device))
                touch(Template(r"hmzc_公告.png", record_pos=(0.001, 0.499), resolution=(720, 1280)))
                sleep(2.5)
            if exists(Template(r"hmzc_开始游戏.png", record_pos=(0.004, 0.669), resolution=(720, 1280))):
                touch(Template(r"hmzc_开始游戏.png", record_pos=(0.004, 0.669), resolution=(720, 1280)))
                if wait(Template(r"hmzc_游戏内断言.png", record_pos=(0.426, -0.846), resolution=(720, 1280)),timeout=25):
                    print('{}__登录游戏成功'.format(self.device))
                    img=Screencap.GetScreen(time.time(), self.device, "")
                    return True,'登录游戏成功',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print('{}__找不到游戏内元素_未能成功进入游戏'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "")
                return False,'找不到游戏内元素_未能成功进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('{}__已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'.format(self.device))
            img=Screencap.GetScreen(time.time(), self.device, "")
            return False,'由于网络原因，或手机反应慢到导致元素无法找到',img[img.find(r'superdalan.com//')+16:][:-4]

    def hmzc_deng_lu_R8AYIJWO99999999(self):
        try:
            if self.poco(text="帐号登录").exists():
                print('{}__欢迎进入登录选择方式页面'.format(self.device))
                sleep(2)
                self.poco("com.dalan.lgh:id/dalan_agreement_check").click()#默认没有勾选需要勾选
                sleep(2)
                self.poco(text="帐号登录").click()
                sleep(3)
                if self.poco(text="帐号登录").exists():
                    print('{}_需要反向勾选协议'.format(self.device));sleep(1.5)
                    self.poco("com.dalan.lgh:id/dalan_agreement_check").click()#默认没有勾选需要勾选
                    sleep(1.5)
                    self.poco(text="帐号登录").click()
                    sleep(3)
                #判断并输入帐号
                if  self.poco(textMatches='^忘记密码.*$').exists():
                    for i in range(len(config.devices())):#迭代设备个数
                        if self.device in config.devices()[i]:
                            print('已在登录_在输入账号密码页面_{}设备对应账号{}'.format(self.device,config.number()[i]))
                            self.poco('com.dalan.lgh:id/dalan_password_input').set_text(config.number()[i])
                    self.poco('com.dalan.lgh:id/dalan_msg_input').set_text('123456')
                    self.poco(text="进入游戏").click()
                    sleep(5.0)
                sleep(2.0)
                if exists(Template(r"hmzc_公告.png", record_pos=(0.001, 0.499), resolution=(720, 1280))):
                    print('{}游戏前_登录页有公告'.format(self.device))
                    touch(Template(r"hmzc_公告.png", record_pos=(0.001, 0.499), resolution=(720, 1280)))
                    sleep(2.5)
                if exists(Template(r"hmzc_开始游戏.png", record_pos=(0.004, 0.669), resolution=(720, 1280))):
                    touch(Template(r"hmzc_开始游戏.png", record_pos=(0.004, 0.669), resolution=(720, 1280)))
                    sleep(3)
                if exists(Template(r"hmzc_创角页面.png", record_pos=(-0.004, 0.767), resolution=(720, 1280))):
                    print('{}__已在创角页面_需要创角'.format(self.device))
                    touch(Template(r"hmzc_创角页面.png", record_pos=(-0.004, 0.767), resolution=(720, 1280)))
                    sleep(4);stop_app(self.name)#杀掉进程可跳过新手
                    sleep(2);start_app(self.name, activity = None)
                    sleep(15)
                #不走创角流程
                elif wait(Template(r"hmzc_游戏内断言.png", record_pos=(0.426, -0.846), resolution=(720, 1280)),timeout=20):
                    print('{}__登录游戏成功'.format(self.device))
                    img=Screencap.GetScreen(time.time(), self.device, "")
                    return True,'登录游戏成功',img[img.find(r'superdalan.com//')+16:][:-4]
            #创角后的操作
            if exists(Template(r"hmzc_公告.png", record_pos=(0.001, 0.499), resolution=(720, 1280))):
                print('{}_再次启动跳新手--登录页有公告'.format(self.device))
                touch(Template(r"hmzc_公告.png", record_pos=(0.001, 0.499), resolution=(720, 1280)))
                sleep(2.5)
            if exists(Template(r"hmzc_开始游戏.png", record_pos=(0.004, 0.669), resolution=(720, 1280))):
                touch(Template(r"hmzc_开始游戏.png", record_pos=(0.004, 0.669), resolution=(720, 1280)))
                if wait(Template(r"hmzc_游戏内断言.png", record_pos=(0.426, -0.846), resolution=(720, 1280)),timeout=25):
                    print('{}__登录游戏成功'.format(self.device))
                    img=Screencap.GetScreen(time.time(), self.device, "")
                    return True,'登录游戏成功',img[img.find(r'superdalan.com//')+16:][:-4]
            else:
                print('{}__找不到游戏内元素_未能成功进入游戏'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "")
                return False,'找不到游戏内元素_未能成功进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('{}__已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'.format(self.device))
            img=Screencap.GetScreen(time.time(), self.device, "")
            return False,'由于网络原因，或手机反应慢到导致元素无法找到',img[img.find(r'superdalan.com//')+16:][:-4]

    def hmzc_deng_lu_b5940085(self):
        if self.poco(text="帐号登录").exists():
            print('{}__欢迎进入登录选择方式页面'.format(self.device))
            self.poco("com.dalan.lgh:id/dalan_agreement_check").click()#默认没有勾选需要勾选
            sleep(1.5)
            self.poco(text="帐号登录").click()
            sleep(3)
            if self.poco(text="帐号登录").exists():
                print('{}_需要反向勾选协议'.format(self.device));sleep(1.5)
                self.poco("com.dalan.lgh:id/dalan_agreement_check").click()#默认没有勾选需要勾选
                sleep(1.5)
                self.poco(text="帐号登录").click()
                sleep(3)
            #判断并输入帐号
            if  self.poco(textMatches='^忘记密码.*$').exists():
                for i in range(len(config.devices())):#迭代设备个数
                    if self.device in config.devices()[i]:
                        print('已在登录_在输入账号密码页面_{}设备对应账号{}'.format(self.device,config.number()[i]))
                        self.poco('com.dalan.lgh:id/dalan_password_input').set_text(config.number()[i])
                self.poco('com.dalan.lgh:id/dalan_msg_input').set_text('123456')
                self.poco(text="进入游戏").click()
                sleep(5.0)
            sleep(2.0)
            if exists(Template(r"hmzc_公告_mi9.png", record_pos=(0.001, 0.532), resolution=(1080, 2340))):
                print('{}游戏前_登录页有公告'.format(self.device))
                touch(Template(r"hmzc_公告_mi9.png", record_pos=(0.001, 0.532), resolution=(1080, 2340)))
                sleep(2.5)
            if exists(Template(r"hmzc_开始游戏_mi9.png", record_pos=(-0.002, 0.706), resolution=(1080, 2340))):
                touch(Template(r"hmzc_开始游戏_mi9.png", record_pos=(-0.002, 0.706), resolution=(1080, 2340)))
                sleep(3)
            if exists(Template(r"hmzc_创角_mi9.png", record_pos=(0.001, 0.802), resolution=(1080, 2340))):
                print('{}__已在创角页面_需要创角'.format(self.device))
                touch(Template(r"hmzc_创角_mi9.png", record_pos=(0.001, 0.802), resolution=(1080, 2340)))
                sleep(4);stop_app(self.name)#杀掉进程可跳过新手
                sleep(2);start_app(self.name, activity = None)
                sleep(15)
            #不走创角流程
            elif wait(Template(r"hmzc_游戏内断言.png", record_pos=(0.426, -0.846), resolution=(720, 1280)),timeout=20):
                print('{}__登录游戏成功'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "")
                return True,'登录游戏成功',img[img.find(r'superdalan.com//')+16:][:-4]
        #创角后的操作
        if exists(Template(r"hmzc_公告_mi9.png", record_pos=(0.001, 0.532), resolution=(1080, 2340))):
            print('{}_再次启动跳新手--登录页有公告'.format(self.device))
            touch(Template(r"hmzc_公告_mi9.png", record_pos=(0.001, 0.532), resolution=(1080, 2340)))
            sleep(2.5)
        if exists(Template(r"hmzc_开始游戏_mi9.png", record_pos=(-0.002, 0.706), resolution=(1080, 2340))):
            touch(Template(r"hmzc_开始游戏_mi9.png", record_pos=(-0.002, 0.706), resolution=(1080, 2340)))
            if wait(Template(r"hmzc_游戏内断言.png", record_pos=(0.426, -0.846), resolution=(720, 1280)),timeout=25):
                print('{}__登录游戏成功'.format(self.device))
                img=Screencap.GetScreen(time.time(), self.device, "")
                return True,'登录游戏成功',img[img.find(r'superdalan.com//')+16:][:-4]
        else:
            print('{}__找不到游戏内元素_未能成功进入游戏'.format(self.device))
            img=Screencap.GetScreen(time.time(), self.device, "")
            return False,'找不到游戏内元素_未能成功进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
        # except:
        #     print('{}__已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'.format(self.device))
        #     img=Screencap.GetScreen(time.time(), self.device, "")
        #     return False,'由于网络原因，或手机反应慢到导致元素无法找到',img[img.find(r'superdalan.com//')+16:][:-4]




if __name__ == "__main__":
    denglu_2=Ddenglu_2('b5940085','com.nsmyfx.dalan')
    denglu_2.hmzc_deng_lu_b5940085()



