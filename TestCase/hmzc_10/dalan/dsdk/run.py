#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from TestCase.hmzc_10.dalan.dsdk import open_game,denglu,order_wechat
from dalan_tools import device_xinxi
from dalan_API import report_API

def _run(device,name,pkg_id):
    '''打开游戏'''
    node_start_time_4=int(time.time())
    devie_xinxi=device_xinxi.Android_device_xinxi(device).device_xinxi()
    object_1=open_game.Ddenglu(device,name)#调用打开app函数(##_工作流第四节点-----打开)
    open_apk=eval('object_1.hmzc_open_'+device)()
    if open_apk[0]==True:
        report_API.get_images({'model':devie_xinxi['model'],'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '打开游戏', '打开游戏成功', 1,node_start_time_4,open_apk[2])
        return True
    elif open_apk[0]==False:
         report_API.get_images({'model':devie_xinxi['model'],'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '打开游戏', '打开游戏失败=='+open_apk[1],0,node_start_time_4,open_apk[2])
         return False
    else:
        return False

def _denglu(device,name,pkg_id):
    '''登录游戏'''
    node_start_time_5=int(time.time())
    devie_xinxi=device_xinxi.Android_device_xinxi(device).device_xinxi()
    object_2=denglu.Ddenglu_2(device,name)####(##_工作流第五节点-----登录)
    hmgame_denglu=eval('object_2.hmzc_deng_lu_'+device)()
    if hmgame_denglu[0]==True:
        report_API.get_images({'model':devie_xinxi['model'],'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '登录', '登录游戏成功',1,node_start_time_5,hmgame_denglu[2])
        return True
    elif hmgame_denglu[0]==False:
        report_API.get_images({'model':devie_xinxi['model'],'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '登录', '登录游失败：'+hmgame_denglu[1], 0,node_start_time_5,hmgame_denglu[2])
        return False
    else:
        return False

def xia_order(device,pkg_id):
    '''游戏内下单_跳转到微信'''
    node_start_time_6=int(time.time())
    devie_xinxi=device_xinxi.Android_device_xinxi(device).device_xinxi()
    object_3=order_wechat.Order(device)
    order_jieguo=eval('object_3.order_weixi_'+device)()###(工作流第五节点-----下单调微信)
    if order_jieguo[0]==True:
        report_API.get_images({'model':devie_xinxi['model'],'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network'],'order_id':order_jieguo[1]}, pkg_id, '下单调起微信', '下单调起微信成功', 1,node_start_time_6,order_jieguo[2])
        return True
    elif order_jieguo[0]==False:
        report_API.get_images({'model':devie_xinxi['model'],'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '下单调起微信', '下单调起微信失败：'+order_jieguo[1], 0,node_start_time_6,order_jieguo[2])
        return False
    else:
        return False

if __name__ == '__main__':
    #print(_run('b5940085','com.shfy.hmzc.gw','12345'))
    print(_denglu('b5940085','com.shfy.hmzc.gw','2020'))
    print(xia_order('b5940085','2020'))
    print(order_wechat.place_order())