#!/usr/bin/env python
# encoding: utf-8
import time,shutil,os
from time import ctime
from multiprocessing import Process
from dalan_tools import config,sql_lianj
import mian

class ThreadFunc(object):
    def __init__(self,func,args,device,name=''):#进程标识，设备id,apk链接，进程名字
        self.name = name
        self.func = func
        self.device=device
        self.args = args
    def __call__(self):
        self.func(*self.args)

def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

def loop(nloop,device,apk_link):
    print('当前进程:{}--时间{}的设备:{}_apk链接：{}'.format(os.getpid(),time.strftime('%H:%M:%S'),device,apk_link))
    mian.run_body(device,apk_link)#调用程序
    time.sleep(2)
    print('{}__end 进程:{}--设备id:{}--{}'.format(nloop,os.getpid(),device,ctime()))


def dalan_main(devices_list,apk_list):
    print('start主线程 at:',ctime())#打印时间
    del_file(os.path.dirname(__file__)+'/File_directory')#创建进程前初始化目录
    threads = []#存放线程实例(或者叫线程对象)
    tt=[]
    nloops = list(range(len(devices_list)))#获取devices_list列表数并生成一个新的list(用于遍历创建线程实例),,如下：[0,1,2...........]
    def thread_1(count):
        if isinstance(count,int):
            for i in nloops:#device，，count从0开始  (count*len(devices_list.....控制进程批次)
                t = Process(target=ThreadFunc(loop,(i,devices_list[i],apk_list[i+(count*len(devices_list))]),loop.__name__))#循环创建线程对象(loop.__name__非必传)
                threads.append(t)#把生成线程对象追加到threads
            for i in nloops: #开始多线程(也可以这样写for i in range(len(threads)):threads[i].start())
                threads[i+(count*len(devices_list))].start()
            for i in nloops: #等待所有线程完成
                threads[i+(count*len(devices_list))].join()

        elif isinstance(count,list):#list为剩余的任务
            yu_threads=[]
            for i in range(len(count)):#device，，count从0开始  (count*len(devices_list.....控制进程批次)
                t = Process(target=ThreadFunc(loop,(i,devices_list[i],count[i]),loop.__name__))#循环创建线程对象(loop.__name__非必传)
                yu_threads.append(t)#把生成线程对象追加到threads
            for i in range(len(count)): #开始多线程(也可以这样写for i in range(len(threads)):threads[i].start())
                yu_threads[i].start()
            for i in  range(len(count)): #等待所有线程完成
                yu_threads[i].join()

    if len(devices_list)<len(apk_list):#设备数是否小于任务数
        count=len(apk_list)/len(devices_list)#比如4/2=2(创建两批进程)
        yu=len(apk_list)%len(devices_list)#剩余的apk链接
        for bb in range(int(count)):
            thread_1(bb)
        if yu >0:
            print('剩余_{}_任务需要减档执行_再次创建进程:{}'.format(yu,apk_list[-yu:]))
            thread_1(apk_list[-yu:])
        else:
            print('任务数是设备倍数_无需单独执行')

    elif len(devices_list)>len(apk_list):
        for i in nloops:
            if i>len(apk_list)-1:
                pass
            else:
                t = Process(target=ThreadFunc(loop,(i,devices_list[i],apk_list[i]),loop.__name__))#循环创建线程对象(loop.__name__非必传)
                threads.append(t)#把生成线程对象追加到threads
        for i in list(range(len(apk_list))): #开始多线程(也可以这样写for i in range(len(threads)):threads[i].start())
            threads[i].start()
        for i in list(range(len(apk_list))): #等待所有线程完成
            threads[i].join()
    else:
        for i in nloops:
            t =  Process(target=ThreadFunc(loop,(i,devices_list[i],apk_list[i]),loop.__name__))#循环创建线程对象(loop.__name__非必传)
            threads.append(t)#把生成线程对象追加到threads
        for i in nloops: #开始多线程(也可以这样写for i in range(len(threads)):threads[i].start())
            threads[i].start()
        for i in nloops: #等待所有线程完成
            threads[i].join()
    print('主进程 end at:',ctime())

if __name__ == '__main__':
    devices_list = config.devices()#控制进程数
    apk_list= sql_lianj.sql_select()
    dalan_main(devices_list,apk_list)


