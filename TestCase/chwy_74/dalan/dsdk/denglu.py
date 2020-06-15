#!/usr/bin/env python
# encoding: utf-8
import re
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from dalan_tools import  Screencap,config

#_____________________________________________冒险岛游戏________________________________________


def mxd_deng_lu(device,name):#冒险岛
    '''登录游戏处理操作'''
    connect_device("Android:///" + device)
    auto_setup(__file__)
    poco=AndroidUiautomationPoco()
    sleep(3.0)
    try:
        if poco(text="同意并进入游戏").exists():#首次进入游戏
            print('{}欢迎进入登录页'.format(device))
            sleep(2.0)
            poco(text="同意并进入游戏").click()
            sleep(6.0)
            #弹窗快速注册页面
            if  poco(textMatches='^我有账号.*$').exists():
                poco(textMatches='^我有账号.*$').click()
                sleep(2.0)
                if  poco(textMatches='^找回密码.*$').exists():
                     for i in range(len(config.devices())):#
                         if device in config.devices()[i]:
                             print('已在登录_在输入账号密码页面_{}设备对应账号{}'.format(device,config.number()[i]))
                             poco('com.xy.qjsg:id/xy_etx_account').set_text(config.number()[i])
                     poco('com.xy.qjsg:id/xy_etx_pwd').set_text('123456')
                     poco(text="进入游戏").click()
                     sleep(6.0)
                if exists(Template(r"mxd_公告.png", record_pos=(-0.004, -0.176), resolution=(1920, 1080))):
                    print('{}游戏前_登录页有公告'.format(device))
                    poco().click((0.484,0.824))#关闭公告
                    sleep(4.0)
            elif exists(Template(r"mxd_公告.png", record_pos=(-0.004, -0.176), resolution=(1920, 1080))):
                print('{}外部-游戏前_登录页有公告'.format(device))
                poco().click((0.484,0.824))#关闭公告
                sleep(3.0)
                if exists(Template(r"mxd_切换账号.png", record_pos=(0.444, -0.212), resolution=(1280, 720))):
                    touch(Template(r"mxd_切换账号.png", record_pos=(0.444, -0.212), resolution=(1280, 720)))
                    sleep(3.0)
            #判断是否在登录_输入账号密码页面
            if  poco(textMatches='^找回密码.*$').exists():
                print('{}外部--已在登录_在输入账号密码页面'.format(device))
                for i in range(len(config.devices())):
                    if device in config.devices()[i]:
                        print('{}设备对应账号{}'.format(device,config.number()[i]))
                        poco('com.xy.qjsg:id/xy_etx_account').set_text(config.number()[i])
                poco('com.xy.qjsg:id/xy_etx_pwd').set_text('123456')
                poco(text="进入游戏").click()
                sleep(6.0)
        elif poco(text="帐号登录").exists():#新版sdk
            print(device+'在登录方式选择页面')
            poco("com.dalan.lgh:id/dalan_agreement_check").click()#默认没有勾选需要勾选
            poco(text="帐号登录").click()
            sleep(3.0)
              #判断是否还在当前页面，如果在说明反复勾选了
            if poco(text="帐号登录").exists():
                print(device+'需要反向勾选用户协议')
                poco("com.dalan.lgh:id/dalan_agreement_check").click()#反向勾选
                sleep(1.0)
                poco(text="帐号登录").click()
                sleep(3.0)#即将进入帐号输入页面
            if  poco(textMatches='^忘记密码.*$').exists():
                 for i in range(len(config.devices())):#
                     if device in config.devices()[i]:
                         print('已在登录_在输入账号密码页面_{}设备对应账号{}'.format(device,config.number()[i]))
                         poco('com.dalan.lgh:id/dalan_password_input').set_text(config.number()[i])
                 poco('com.dalan.lgh:id/dalan_msg_input').set_text('123456')
                 poco(text="进入游戏").click()
                 sleep(6.0)
                 if exists(Template(r"mxd_公告.png", record_pos=(-0.004, -0.176), resolution=(1920, 1080))):
                     print('{}游戏前_登录页有公告'.format(device))
                     poco().click((0.484,0.824))#关闭公告
                     sleep(4.0)
        else:
            print('{}找不到_同意并进入游戏，或元素超时'.format(device))

        if exists(Template(r"mxd_开始冒险.png",threshold=0.6, record_pos=(0.003, 0.198), resolution=(1920, 1080))):
            poco().click((0.626,0.676))#点击进入选区
            sleep(3)
            poco().click((0.198,0.220))#点击我的角色模块
            print('{}游戏前_选择角色'.format(device))
            sleep(3.0)
            img_3625=Template(r"mxd_3625_角色.png", record_pos=(-0.037, -0.091), resolution=(1920, 1080))
            img_669=Template(r"mxd_669_角色.png", record_pos=(-0.041, -0.089), resolution=(1280, 720))
            img_list=[img_669,img_3625]
            for pic in img_list:
                pos = exists(pic)
                if pos:
                    print('{}_循环查询角色'.format(device))
                    touch(pos)
                    break # 只要找到图片列表中的任何一张图片，就执行touch
                else:
                    pass
        sleep(4.0)
        poco().click([0.500,0.845])#开始冒险
        try:
            if  wait(Template(r"mxd_进入游戏按钮.png",record_pos=(0.334, 0.231), resolution=(1280, 720)),18):
                touch(Template(r"mxd_进入游戏按钮.png", record_pos=(0.334, 0.231), resolution=(1280, 720)))
                try:
                    if  wait(Template(r"mxd_游戏内任务.png",record_pos=(0.334, 0.231), resolution=(1280, 720)),30):
                        print('{}进入游戏_成功'.format(device))
                        img=Screencap.GetScreen(time.time(), device, "True")
                        return True,'登录成功',img[img.find(r'superdalan.com//')+16:][:-4]
                except:
                    print('{}进入游戏异常_找不到元素'.format(device))
                    img=Screencap.GetScreen(time.time(), device, "True")
                    return False,'找不到游戏内元素_未能成功进入游戏',img[img.find(r'superdalan.com//')+16:][:-4]
        except:
            print('{}在选服后出现异常,可能在维护(-详情看截图)'.format(device))
            img=Screencap.GetScreen(time.time(), device, "True")
            return False,'在选服后出现异常,可能在维护,详情看截图',img[img.find(r'superdalan.com//')+16:][:-4]
    except:
        print('{}已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)'.format(device))
        img=Screencap.GetScreen(time.time(), device, "True")
        return False,'由于网络原因，或手机反应慢到导致元素无法找到',img[img.find(r'superdalan.com//')+16:][:-4]

if __name__ == "__main__":
    print(mxd_deng_lu('54a4c6159804','com.ywhc.xxyzhbb'))
    #Screencap.GetScreen(time.time(), '54a4c6159804', "test_01_of_10")#手动截图
