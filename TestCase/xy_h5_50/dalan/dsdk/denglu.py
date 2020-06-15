#!/usr/bin/env python
# encoding: utf-8

from airtest.core.api import *

from dalan_tools import  Screencap,config, baidu_shibie

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
connect_device("Android://127.0.0.1:5037"+'/'+config.devices())
poco=AndroidUiautomationPoco()
sleep(1.5)
def xy_deng_lu(name):
    clear_app(name)
    start_app(name)
    sleep(2.0)
    #判断是否有权限弹框
    if poco("com.android.packageinstaller:id/permission_deny_button").exists():
        for i in range(0,7):#弹框处理
            if poco("com.android.packageinstaller:id/permission_deny_button").exists():
                poco(text="始终允许").click()
            else:
                print("已授权_或无需授权=%d"%i)
                break
    try:
        #已有账号记录
        if poco(text="同意并进入游戏").wait(15).exists():
            poco(text="同意并进入游戏").click()
            print('已进入登录_协议页面')
            sleep(20.0)
        pd_gonggao= baidu_shibie.compressImage('chen.png', 0.42, 0.09, 0.17, 0.05)#获取公告
        if  pd_gonggao=='公告':
            print('有公告')
            poco().click((0.947,0.101))
            if exists(Template(r"开始游戏.png", record_pos=(0.0, 0.592), resolution=(720, 1280))):
                poco().click((0.502,0.825))#开始游戏
                print('点击开始游戏')
                sleep(25.0)
                poco().click((0.500,0.900))#选择角色页面_可能不用选择，为了保险还是点下
            if wait(Template(r"游戏内元素.png", record_pos=(-0.408, 0.831), resolution=(720, 1280)),30):
                print('成功进入游戏')
            else:
                print('进入游戏失败_未找到元素')
#新注册账号_新手机或清缓存会有
        elif poco(text="进入游戏").exists():
            poco(text="进入游戏").click()
            if poco(text="我知道了").wait(10).exists():
                poco(text="我知道了").click()
                print('注册账号成功')
                sleep(10.0)
                poco().click((0.500,0.900))#选择角色页面
                sleep(25.0)
                paduan= baidu_shibie.compressImage('chen.png', 0.5, 0.01, 0.15, 0.03)
            if paduan==0:
                print('进入游戏成功')
            else:
                print('进入游戏失败_未找到元素')
        chongzhi_q= baidu_shibie.compressImage('chen.png', 0.43, 0.01, 0.21, 0.03)#充值前获取用户拥有的金额
        print('充值前的金额',chongzhi_q)
        poco().click((0.582,0.028))#点击顶部充值
        sleep(3.0)
        chongzhi_y= baidu_shibie.compressImage('chen.png', 0.81, 0.68, 0.13, 0.03)#获取充值页元素
        if chongzhi_y=='充值6元':
            print('已进入充值档位页面_首次充值')
            sleep(4.0)
            poco().click((0.9,0.689))#点击充值6元
        elif baidu_shibie.compressImage('chen.png', 0.60, 0.60, 0.20, 0.10)== '6元':
            print('已进入充值档位页面_非首次充值')
            poco().click((0.696,0.628))#点击充值6元
        else:
            print('进入充值页面失败')
        poco(text="微信").click()#微信支付
        sleep(4.0)
        poco(text="立即支付").click()
        print('微信支付_输入密码页')
        sleep(3.0)
        #输入支付密码
        touch((220.0,2060.0))#4
        touch((1202.0,1844.0))
        touch((720.0,1850.0))
        touch((222.0,2268.0))
        touch((752.0,2435.0))
        touch((777.0,2048.0))
        sleep(2.0)
        poco(text="完成").click()#完成后自动跳转到充值档位页面
        sleep(2.5)
        poco().click((0.934,0.032))#关闭充值档位_回到首页
        sleep(1.5)
        chongzhi_h= baidu_shibie.compressImage('chen.png', 0.43, 0.01, 0.15, 0.03)#充值前获取用户拥有的金额
        if int(chongzhi_h)==int(chongzhi_q)+600:
            print('充值成功')
            return True
        elif int(chongzhi_h)==int(chongzhi_q)+1200:
            print('首次充值双倍')
            return True
        elif int(chongzhi_h)<int(chongzhi_q)+600:
            print('充值未到账')
            return False
        else:
            print('充值判断失败')
            return False

    except:
        print('已走异常流程_截图异常页面(原因：主要是因为没有进入指定页面_)')
        Screencap.GetScreen(time.time(), config.devices(), "mxd_deng_lu")#手动截图





if __name__ == "__main__":
    xy_deng_lu('com.tencent.tmgp.scycjxyb')

