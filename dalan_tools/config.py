#!/usr/bin/env python
# encoding: utf-8
import configparser
cf=configparser.ConfigParser()   #创建对象
cf.read(r'E:\Test_dalan_gzl_jiance_apk\config.ini')   #读取配置文件，直接读取ini文件内容
def devices():
    '''获取设备'''
    #print(cf.get('config_devices','device'))
    devices=cf.get('config_devices','device')
    return devices.split(",")

def number():
    '''获取设备'''
    #print(cf.get('config_devices','device'))
    number=cf.get('config_devices','number')
    return number.split(",")

def using_huanj():
    '''获取环境'''
    #print(cf.get('config_devices','device'))
    return cf.get('config_devices','environment')

def game():
    '''获取游戏资源'''
    game_list=cf.get('config_game','game_list')
    return eval(game_list)



if __name__ == '__main__':
    print(devices())
    print(number())
    #print(using_huanj())
    #print(game())








