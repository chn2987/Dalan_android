# -*- coding: utf-8 -*-
import os
import time
import  requests
from dalan_tools import config
from dalan_API import api_img_xiazai_main


#———————————————下载图片资源(下载前需要先获取)——————————————————————
def downloader(url,path):
    'u''文件下载函数'''
    start = time.time()
    size = 0
    response = requests.get(url,stream=True)
    chunk_size=1024
    #content_size=int(response.headers['content-length'])
    if response.status_code==200:
        with open(path,"wb")as file:
            for data in response.iter_content():
                file.write(data)
                size +=len(data)
    end = time.time()
    #print('\n'+"下载完成！ 用时%.2f秒"%(end-start))

def obtain_img(pkgid):
    '''调用获取服务端资源'''
    return api_img_xiazai_main.get_images(pkgid)

unpacking_path={}
file=[]
def run_img(pkgid):
    '''对下载的apk资源遍历_处理'''
    apk_resources=obtain_img(pkgid)#调用服务端接口_获取资源
    print(apk_resources)
    environment=config.using_huanj()
    if environment=='test':
        url=r"http://file.local.superdalan.com/"
    elif environment=='production':
        url=r"http://file.superdalan.com/"
    path=os.path.dirname(os.path.dirname(__file__))+'/File_directory/img/'
    if not os.path.exists(path):
        os.mkdir(path)
    for key,value in apk_resources['data'].items():
        if key == 'file':
            dict=eval(str(value).strip('[]'))
            if dict is not  None:
                for key1,value1 in dict.items():
                    if  value1:
                        file.append(value1+'.jpg')
                        downloader(url+value1,path+value1+'.jpg')#调用下载函数(url,路径+文件名)
                return '下载成功',file, eval(str(apk_resources['data']['asset']).strip('[]'))#返回实际图片路径
            else:
                return '后台没有配置资源图片'

if __name__ == "__main__":
    print(run_img(2901))









