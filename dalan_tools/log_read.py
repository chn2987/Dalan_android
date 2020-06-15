#!/usr/bin/env python
# encoding: utf-8
__author__ = "晨晨"
class cd_file(object):
    def __init__(self,path):
        self.path=path

    def file(self):
        fd=open(self.path,'r') #获得一个句柄
        a=len(fd.readlines())
        fd.close() #关闭文件
        return a

    def write(self):
        with open(self.path,mode="a+",encoding="UTF-8",errors="ignore") as abc:
            abc.write('11111111111111111\n')

    def zai_read(self,label):
        #再次阅读文件
        reprt=''
        fd=open(self.path,'r')
        for line in fd.readlines()[label:]:
                reprt+=line
        return reprt

    def log_re(self):
        '''获取每次执行的关键节点log'''
        shuju=[]
        with open(self.path,mode="r",encoding="gbk",errors="ignore") as abc:
            fileContent=abc.readlines()
            for i in  range(len(fileContent)):
                if   "从数据库获取apk链接写入日志', ['http://pkg.superdalan.com" in fileContent[i]:
                    shuju.append(fileContent[i])
            for a in  range(len(fileContent)):
                if shuju[len(shuju)-1] in fileContent[a]:
                    return '\n'.join(fileContent[a:])


if __name__ == '__main__':
    read=cd_file(r'E:\Test_dalan_gzl_jiance_apk\all_log\part_log\2020-05-21执行关键点_日志.log')
    print(read.log_re())
    # read=cd_file(r'E:\Test_dalan_gzl_jiance_apk\all_log\all_print\2020-05-13.log')
    # weizhi=read.file()
    # read.write()
    # print(read.zai_read(weizhi))