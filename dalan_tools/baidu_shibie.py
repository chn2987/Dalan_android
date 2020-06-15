#!/usr/bin/env python
# encoding: utf-8
from PIL import Image
import tesserocr
import pytesseract
import os,re,time
from aip import AipOcr
from dalan_tools import config
"""
PS:指定区域截取android屏幕，并识别区域中内容
"""
#使用装饰来修饰compressImage方法，装饰器可跟随参数
def shou_jie(func):
	def  wrapper(*path):
		os.system('adb -s '+path[0]+r' exec-out screencap -p > D:\tp_zancun\chen.png')#手动截图android
		return func(*path)
	return wrapper

#__________指定区域截取图片(在pc处理图片)______________________________
@shou_jie
def compressImage(device,path,x1,y1,w1,h1):
    'u''指定android区域截图'''
    img = Image.open(r'D:\tp_zancun\chen.png')
    # 图片尺寸
    img_size = img.size
    h = img_size[1]  # 图片高度
    w = img_size[0]  # 图片宽度
    #x,y 表示截取图片所在位置，， w，h表示截取图片宽，高
    x = x1 * w#0.77
    y =y1 * h#0.0955
    w = w1 * w#0.1
    h = h1 * h#0.03
    # 开始截取
    region = img.crop((x, y, x + w, y + h))
    # 保存图片
    region.save(r'D:\tp_zancun\chen.png')
    money=shibie(r'D:\tp_zancun\chen.png')
    return  money

#____________________________通过百度API识别图片内容______________________________________________________
""" 你的 APP_ID API_KEY SECRET_KEY，上面的图已经展示了如何找自己的这三个信息，只需要复制信息，放进去单引号里面就行，均为字符串 """
def shibie(path):
    '''
    先指定区域截图在通过百度API识别图片
    '''
    APP_ID = '17507919'
    API_KEY = 'FkTh0Ns2sr8G9ff094bCT891'
    SECRET_KEY = 'Zt1rLvtMZE0MLyoKNId5wGyOSlNlW8fX'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    i = open(path,'rb')
    img = i.read()
    message = client.basicGeneral(img)
    for i in message.get('words_result'):
        #print(i.get('words'))
        return i.get('words')

if __name__ == "__main__":
    #函数调用部分
    aa=compressImage('ea91a8e0','chen.png',0.16,0.52,0.2,0.08)#需要处理的图片及区域
    print('aa',aa)

'''
如果装饰想解释任意参数(如列表，字典等)，就可以这样写wrapper(*args, **kwargs)，，func(*args, **kwargs)
可以优化加入类的继承来封装，，同时可以加入特殊函数来构建
'''


