#!/usr/bin/env python
# encoding: utf-8
#____________________________功能：获取_解压目录下的apk文件____________________________________
import os
import zipfile


path1=os.path.dirname(os.path.dirname(__file__))+'/File_directory/'

def chong_name(name):
    'u''文件重命名为zip格式'''
    print(path1+name[:-4]+'.zip')
    if not os.path.exists(path1+name[:-4]+'.zip'):
        os.rename(path1+name,path1+name[:-4]+'.zip')
        return name[:-4]
    else:
        pass

def un_zip(file_name):
    """zip文件解压"""
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name[:-4]):
        pass
    else:
        os.mkdir(file_name[:-4])
    for names in zip_file.namelist():
        #print(names)
        zip_file.extract(names,file_name[:-4])
    zip_file.close()

def main(apk_url):
    '''控制重命名和解压文件'''
    list=chong_name(apk_url)#调用重命名函数
    if list:
        un_zip(path1+list+'.zip')
        return '本地拆包解压完成'+list
    else:
        return r'File_directory目录没有apk文件'

if __name__ == '__main__':
    print(main('flzcgdt_dalan_dsdk_10_1.0.0_20200417_174449.apk'))















