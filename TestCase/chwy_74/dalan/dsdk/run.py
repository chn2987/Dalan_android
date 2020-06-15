#!/usr/bin/env python
# encoding: utf-8
__author__ = "晨晨"
import time
from dalan_tools import device_xinxi
from dalan_API import report_API,order_select
from TestCase.chwy_74.dalan.dsdk import denglu,open_game,order_wechat

def _run(device,name,pkg_id):
    '''打开游戏-彩虹无语'''
    node_start_time_4=int(time.time())
    devie_xinxi=device_xinxi.Android_device_xinxi(device).device_xinxi()
    object_1=open_game.Ddenglu(device,name)#调用打开app函数(##_工作流第四节点-----打开)
    open_apk=eval('object_1.mxd_open_'+device)()
    if open_apk[0]==True:
        report_API.get_images({'model':devie_xinxi['model'],'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '打开游戏', '打开游戏成功', 1,node_start_time_4,open_apk[2])
        return True
    elif open_apk[0]==False:
         report_API.get_images({'model':devie_xinxi['model'],'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '打开游戏', '打开游戏失败=='+open_apk[1],0,node_start_time_4,open_apk[2])
         return False
    else:
        return False

def _denglu(device,package_name,pkg_id):
    '''登录游戏--彩虹无语'''
    node_start_time_5=int(time.time())
    devie_xinxi=device_xinxi.Android_device_xinxi(device).device_xinxi()
    hmgame_denglu=denglu.mxd_deng_lu(device,package_name)####(##_工作流第五节点-----登录)
    if hmgame_denglu[0]==True:
        report_API.get_images({'model':devie_xinxi['model'],'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '登录', '登录游戏成功',1, node_start_time_5,hmgame_denglu[2])
        return True
    elif hmgame_denglu[0]==False:
        report_API.get_images({'model':devie_xinxi['model'],'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '登录', '登录游失败：'+hmgame_denglu[1], 0, node_start_time_5,hmgame_denglu[2])
        return False
    else:
        return False

def xia_order(device,pkg_id):
    '''游戏内下单_跳转到微信'''
    node_start_time_6=int(time.time())
    devie_xinxi=device_xinxi.Android_device_xinxi(device).device_xinxi()
    order_jieguo=order_wechat.place_order(device)###(工作流第五节点-----下单调微信)
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
    print(_run('QDY4C17818002168','com.tencent.tmgp.ttqymxw','681'))
    #print(_denglu('R8AYIJWO99999999','com.yzmxw.ttqy.toutiao','681'))
    print(xia_order('R8AYIJWO99999999','681'))
    print(denglu.hm_deng_lu(1,'com.shfy.hmzc.toutiao'))
    print(order_wechat.place_order())