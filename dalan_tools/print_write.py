#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import time

class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")#a表示追加，w覆盖写入

    def write(self, message):
        self.terminal.write(message)
        if '下载进度' not in message:
            #a=str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            self.log.write(message)

    def flush(self):
        pass



now = time.strftime("%Y-%m-%d", time.localtime())#获取当前日期
sys.stdout = Logger(os.path.dirname(__file__)[:-12]+'/all_log/all_print/'+now+'.log')#存放文件名

if __name__ == '__main__':
    __console__=sys.stdout
    print('------------------')
    print('222222222222222222222222')
    sys.stdout=__console__
    time.sleep(10)


