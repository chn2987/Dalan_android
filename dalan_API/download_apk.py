# -*- coding: utf-8 -*-
import time,os
import requests
from multiprocessing import Pool
def downloader(url,path):
    'u''文件下载函数'''
    start = time.time()
    size = 0
    response = requests.get(url,stream=True)
    chunk_size=1024
    try:
        content_size=int(response.headers['content-length'])
        if response.status_code==200:
            print('[文件大小]:%0.2f MB'% (content_size / chunk_size /1024))
            with open(path,"wb")as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    size +=len(data)
                    print('\r'+'[下载进度'+url[-28:]+']:%s%.2f%%' % ('>'*int(size*50/ content_size),float(size / content_size * 100)),end='')
        end = time.time()
        print('\n'+"下载%s完成！ 用时%.2f秒"%(url,end-start))
        return  float(size / content_size * 100)
    except:
         return response.text

def Pretreatment(apk_link):
    'u''遍历包的链接_及调用函数'''
    url=apk_link
    jieguo=downloader(url=url,path=os.path.dirname(os.path.dirname(__file__))+'/File_directory'+'\\'+url[url.find('&f=')+3:])#调用函数,切片取后10位作为包名
    #downloader(url=url,path="快手.apk")#调用函数，并重命名下载文件
    #判断是否下载成功
    if jieguo==100.0:
        return True,apk_link
    else:
        return False,jieguo#失败时返回响应数据


if __name__ == "__main__":
    ps=Pool(2)#进程池
    apk_list=['http://pkg.superdalan.com/game.pkg/download?pkgId=2624&f=qyzol_rongyao_android_34_1.0.0_20200420_150803.apk','http://pkg.superdalan.com/game.pkg/download?pkgId=2623&f=shmykshb_dalan_dsdk_48_1.0.0_20200420_081329.apk']
    for i in range(len(apk_list)):
        ps.apply_async(Pretreatment,args=(apk_list[i],)) # 异步执行
    ps.close()
    # 阻塞进程
    ps.join()
    print("主进程终止")
    # pa=r'E:\Test_dalan_gzl_jiance_apk\File_directory'
    # url='http://pkg.local.superdalan.com/game.pkg/download?pkgId=583&f=flzcsdk_dalan_dsdk_10_1.0.0_20190906_104237.apk'
    # downloader(url=url,path=pa+'\\'+'333.apk')#调用函数,切片取后10位作为包名