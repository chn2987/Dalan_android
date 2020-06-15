# -*- coding: utf-8 -*-
import os
# 文件的路径
def wen(path,apk_url=''):
    'u''判断包是否在目录中'''
    files = os.listdir(path)
    ai=[]
    for f in files:
        if '' in f and f.endswith('.apk'):#等价于if  f.endswith('.png'):
            if apk_url in  f:
                ai.append(f)
    return  ai


def img_mulu(path,type1,type2='.png'):
    'u''查询xx目录下，后缀为.apk的文件'''
    files = os.listdir(path)
    ai=[]
    for f in files:
        if '' in f and f.endswith(type1) or f.endswith(type2):#等价于if  f.endswith('.png'):
            #print(f)
            ai.append(f)
    return  ai


def chen():
    #print(os.listdir('.'))#打印当前目录所有文件
    # path = os.listdir(os.getcwd())
    # #获取当前目录下的文件夹
    # for p in path:
    #     if os.path.isdir(p):
    pass
    #         print(p)

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print('root_dir:', root)  # 当前目录路径
        print('sub_dirs:', dirs)  # 当前路径下所有子目录
        print('files:', files)  # 当前路径下所有非目录子文件(包括子文件夹下面的文件)

if __name__=="__main__":
    print(wen(r'D:\Downloads','417_174449.apk'))#获取目录下的apk文件
    # path=r'D:/Downloads/img/'
    # type1='.jpg'
    # print(img_mulu(path,type1))

#file_name('D:\Downloads')
#wenjian()
#a=wen()
#chen()
