#!/usr/bin/env python
# encoding: utf-8
__author__ = "晨晨"
from dalan_tools import device_xinxi
from dalan_API import report_API,order_select
from TestCase.fzzj_61.dalan.dsdk import denglu,open_game,order_wechat
from multiprocessing import Process
import time


def _run(device,name,pkg_id):
    '''打开游戏-我在江湖'''
    node_start_time_4=int(time.time())
    devie_xinxi=device_xinxi.Android_device_xinxi(device).device_xinxi()
    object_1=open_game.Ddenglu(device,name)#调用打开app函数(##_工作流第四节点-----打开)
    open_apk=eval('object_1.fzzj_open_'+device)()
    if open_apk[0]==True:
        report_API.get_images({'model':devie_xinxi['model'], 'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '打开游戏', '打开游戏成功', 1,node_start_time_4,open_apk[2])
        return True
    elif open_apk[0]==False:
         report_API.get_images({'model':devie_xinxi['model'], 'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '打开游戏', '打开游戏失败=='+open_apk[1],0,node_start_time_4,open_apk[2])
         return False
    else:
        return False

def _denglu(device,package_name,pkg_id):
    '''登录游戏-我在江湖'''
    node_start_time_5=int(time.time())
    devie_xinxi=device_xinxi.Android_device_xinxi(device).device_xinxi()
    object_2=denglu.Ddenglu_2(device,package_name)###(##_工作流第五节点-----登录)
    fzzj_denglu=eval('object_2.fzzj_deng_lu_'+device)()
    if fzzj_denglu[0]==True:
        report_API.get_images({'model':devie_xinxi['model'], 'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '登录', '登录游戏成功',1,node_start_time_5,fzzj_denglu[2])
        return True
    elif fzzj_denglu[0]==False:
        report_API.get_images({'model':devie_xinxi['model'], 'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '登录', '登录游失败：'+fzzj_denglu[1], 0,node_start_time_5,fzzj_denglu[2])
        return False
    else:
        return False

def xia_order(device,pkg_id):
    '''游戏内下单_跳转到微信'''
    node_start_time_6=int(time.time())
    devie_xinxi=device_xinxi.Android_device_xinxi(device).device_xinxi()
    object_3=order_wechat.Order(device)
    order_jieguo=eval('object_3.place_order_'+device)()###(工作流第五节点-----下单调微信)
    print(order_jieguo)
    if order_jieguo[0]==True:
        order_result=order_select.select_order(order_jieguo[1])#订单状态
        if order_result=='success':
            report_API.get_images({'model':devie_xinxi['model'], 'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network'],'order_id':order_jieguo[1]}, pkg_id, '下单调起微信', '下单调起微信成功', 1,node_start_time_6,order_jieguo[2])
            return True
        else:
             return False
    elif order_jieguo[0]==False:
        report_API.get_images({'model':devie_xinxi['model'], 'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '下单调起微信', '下单调起微信失败：'+order_jieguo[1], 0,node_start_time_6,order_jieguo[2])
        return False
    else:
        return False


if __name__ == '__main__':
    # p1=Process(target=wzjh_run,args=('54a4c6159804','com.dalan.shjyssr',202))
    # p2=Process(target=wzjh_run,args=('QDY4C17818002168','com.dalan.shjyssr',5000))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    # print('主进程结束')
    print(_run('54a4c6159804','com.fzzj.hxjy.gdt','2020'))
    print(_denglu('54a4c6159804',' com.fzzj.hxjy.gdt','2020'))
    print(xia_order('54a4c6159804','2020'))
