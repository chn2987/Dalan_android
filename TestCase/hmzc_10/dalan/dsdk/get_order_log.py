#!/usr/bin/env python
# encoding: utf-8
import subprocess
import time,os,re,psutil
path=os.path.dirname(__file__)
def log_get(device):
    #####------------------------获取并写入文件----------------------
    subprocess.call('adb -s '+device+' logcat -c')#每次获取—先清理缓存
    proc=subprocess.Popen(r'adb -s '+device+' logcat *:D|find "union_order_sn">'+path+'/order_log/'+device+'.txt', shell=True)
    time.sleep(15)#获取18秒内的日志
    pobj = psutil.Process(proc.pid)
    #杀掉proc实例对应的进程
    for c in pobj.children(recursive=True):
        c.kill()
    pobj.kill()

def say(name,device):
    global order_id
    print('%s__子线程 %s__start '%(device,name))
    order_id=log_get(device)
    print('%s__子线程%s__stop'%(device,name))


if __name__=='__main__':
    say('sry','QDY4C17818002168')





