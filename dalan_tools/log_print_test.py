#!/usr/bin/env python
# encoding: utf-8
__author__ = "晨晨"
import sys,time
class __redirection__:

    def __init__(self):
        self.buff=''
        self.__console__=sys.stdout

    def write(self, output_stream):
        if '下载进度' not in output_stream:
            self.buff+=output_stream

    def to_console(self):
        sys.stdout=self.__console__
        print(self.buff)

    def to_file(self, file_path):
        f=open(file_path,'a+')
        sys.stdout=f
        print(self.buff)
        #f.close()

    def flush(self):
        self.buff=''

    def reset(self):
        sys.stdout=self.__console__

if __name__=="__main__":
    r_obj=__redirection__()#创建sys.stdout对象
    sys.stdout=r_obj
    print('3333333333')
    print('555555555555555')
    r_obj.to_console()#放在print的前，则不写print数据到文件，print直接打在控制台(如果放在print后就写入文件，不在控制台打印)
    r_obj.to_file(r'C:\Users\Administrator\Desktop\out.log')


