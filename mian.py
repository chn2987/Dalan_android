#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime,time,importlib
from dalan_email import log_email
import os,shutil,sys,process
from time import ctime
from dalan_API import report_API, download_apk,api_img_xiazai_main
from dalan_tools import apk_all_install, sql_lianj,log_file,wenjian_mulu,device_xinxi,screen_state,config,lujin_qubaoming,log_read,print_write,log_print_test
from dalan_unpacking import download_img, mulu_apk_unzip,similarity_degree
os.chdir(r'E:\Test_dalan_gzl_jiance_apk')

def dalan_test():
    '''获取数据库链接'''
    ###获取当前时间
    now = datetime.datetime.now()
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S")
    print('''========================================start程序1111=============================================
    ===================================={}==========================================='''.format(otherStyleTime))
    apk_list= sql_lianj.sql_select() #从数据库获取apk链接(获取所有连接)
    log_file.log('从数据库获取apk链接写入日志',apk_list)#写入日志
    print('%s获取数据库中apk链接=%s'%(ctime(),apk_list))
    if not apk_list:
        exit()#如果没有获取到连接，就终止程序
    return apk_list

def run_body(device,apk_url):
    '''通过多进程方式启动_节点脚本'''
    pkg_id=apk_url[apk_url.find('pkgId')+6:apk_url.find('&')]
    node_start_time_1=int(time.time())
    devie_xinxi=device_xinxi.Android_device_xinxi(device).device_xinxi()#获取设备信息
    print('{}--设备{}:{}'.format(ctime(),device,devie_xinxi))
    pkg= download_apk.Pretreatment(apk_url)##########调用下载(工作流第一节点----下载apk)
    time.sleep(0.5)
    print('---------------------------设备:{}____{}----节点1-----------------------------------下载校验结果：{}'.format(device,apk_url[apk_url.find('&')+3:],pkg[0]))
    log_file.log('-----------{}__{}----节点1-----------下载校验结果：{}'.format(device,apk_url[apk_url.find('&')+3:][-20:],pkg[0]))
    if pkg[0]!=True:
        report_API.get_images({}, pkg_id, '包体下载', '包体下载失败==' + str(pkg), 0,node_start_time_1)
        print('包url异常下载失败',sql_lianj.delete_sql(apk_url))#删除数据库记录
        exit()#出去当前进程
    else:
        report_API.get_images({'url_apk':pkg[1]}, pkg_id, '包体下载', '包体下载成功', 1,node_start_time_1)
    mulu_apk=wenjian_mulu.wen(os.path.dirname(__file__)+'/File_directory',apk_url[-20:])#获取目录对应的任务包
    print('{}--{}--{}:File_directory下包有{}'.format(ctime(),os.getpid(),device,mulu_apk))

    node_start_time_2=int(time.time())
    install_result=apk_all_install.auto_install(device,mulu_apk[0])#######安装apk到手机(##工作流第二节点----安装)
    time.sleep(0.5)
    print('------------------------------%s__%s----节点2-------------------------------------安装返回结果：%s'%(device,mulu_apk[0],install_result))
    log_file.log('---------%s__%s-------节点2------安装返回结果：%s'%(device,mulu_apk[0][-20:],install_result))
    if  install_result==True:
        report_API.get_images({'model':devie_xinxi['model'],'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '安装apk', '安装apk成功', 1,node_start_time_2)
    else:
        report_API.get_images({'model':devie_xinxi['model'],'imei':devie_xinxi['imei'], 'system_version':devie_xinxi['system_version'], 'network':devie_xinxi['network']}, pkg_id, '安装apk', '安装apk失败==' + install_result, 0,node_start_time_2)
        print(device+'包损坏安装不了需要删除',sql_lianj.delete_sql(apk_url))#删除数据库记录
        exit()#出去当前进程

    node_start_time_3=int(time.time())
    package_name=lujin_qubaoming.ApkInfo(os.path.dirname(__file__)+'/File_directory/'+ mulu_apk[0]).getApkBaseInfo()#直接创建对象调用getApkBaseInfo()方法
    img_download= download_img.run_img(pkg_id)#根据pkg_id获取相关资源去下载图片，并返回下载结果(如果下载成功返回结果+实际路径),,(工作流第三节点--------素材校验)
    if img_download[0] =='下载成功':
        unpacking= mulu_apk_unzip.main(apk_url[apk_url.find('&')+3:])#本地拆包
        unpacking_verification=similarity_degree.image.img_run(img_download[2],os.path.dirname(__file__)+'/File_directory/'+unpacking[8:]+'/',pkg_id,img_download[1],device)#校验素材
        print('--------------------------{}--{}---{}----节点3------------------------------------拆包校验结果：{}'.format(os.getpid(),device,apk_url[apk_url.find('&')+3:],unpacking_verification[0]))
        log_file.log('------------{}__{}----节点3---------拆包校验结果：{}:{}'.format(device,apk_url[apk_url.find('&')+3:][-20:],unpacking_verification[0],unpacking_verification[1]))
        time.sleep(0.5)
        if unpacking_verification[0]==True:
            report_API.get_images({'server_img':unpacking_verification[1]}, pkg_id, '拆包校验', '拆包校验成功', 1,node_start_time_3)
        else:
             print('失败原因:'+unpacking_verification[1])
             report_API.get_images({}, pkg_id, '拆包校验', '拆包校验失败=' + unpacking_verification[1], 0,node_start_time_3)
             print(device+'包的素材不一致需要删除',sql_lianj.delete_sql(apk_url))#素材校验失败删库
             sys.exit()
    else:
        print('-------------------pid:{}---{}__{}---节点3------------------------------后台没有配置素材无需校验'.format(os.getpid(),device,apk_url[apk_url.find('&')+3:]))
        log_file.log('--------{}__{}---节点3--------后台没有配置素材无需校验'.format(device,apk_url[apk_url.find('&')+3:][-20:]))
        report_API.get_images({}, pkg_id, '拆包校验', '后台没有配置素材无需校验', 1,node_start_time_3)
        time.sleep(5)
    print(screen_state.isAwaked(device))#保证手机在亮屏状态
    #若打开app成功后，就登录游戏
    aa=api_img_xiazai_main.get_images(pkg_id)#调用获取apk资源信息
    game_list=[]
    if aa['data']['channel_pinyin']=='dsdk' or aa['data']['channel_pinyin']== 'xy_dsdk':
        for key,value in config.game().items():
            game_list.append(key)
            print(key,value)
            params = importlib.import_module(value) #绝对导入
            print(value)
            if aa['data']['game_original_name']==key:
                os.system('adb -s {} shell input keyevent 3'.format(device))#初始化home页面(回到桌面)
                #os.system('adb -s {} shell rm -rf /sdcard/.dalan'.format(device))#删除本地数据库
                jieguo=params._run(device,package_name,pkg_id)#打开游戏(工作流第四节点-----打开)
                print('----------{}--{}--{}--{}----节点4------------------------------打开游戏结果:{}'.format(ctime(),os.getpid(),device,apk_url[apk_url.find('&')+3:],jieguo))
                log_file.log('-----------{}__{}----节点4----------打开游戏结果:{}'.format(device,apk_url[apk_url.find('&')+3:][-20:],jieguo))
                if  jieguo==False:
                    apk_cont=sql_lianj.condition_select(apk_url)#查询是否有标记
                    if apk_cont == None:sql_lianj.updata_sql(apk_url);os.system('adb -s {} shell rm -rf /sdcard/.dalan'.format(device));sys.exit()#如果没有标记就需要做标记
                    elif apk_cont == 1:
                        print(device+'执行2次了还是失败，需要删除链接',sql_lianj.delete_sql(apk_url))#删除数据库记录
                        sys.exit()

                denglu=params._denglu(device,package_name,pkg_id)#登录(工作流第五节点-----登录)
                print('--------------------{}--{}--{}---节点5----------------------------登录游戏结果:{}'.format(os.getpid(),device,apk_url[apk_url.find('&')+3:],denglu))
                log_file.log('-----------{}__{}----节点5----------登录游戏结果:{}'.format(device,apk_url[apk_url.find('&')+3:][-20:],denglu))
                if  denglu==False:
                    apk_cont=sql_lianj.condition_select(apk_url)
                    if apk_cont == None:sql_lianj.updata_sql(apk_url);os.system('adb -s {} shell rm -rf /sdcard/.dalan'.format(device));sys.exit()
                    elif apk_cont == 1:
                        print(device+'执行2次了还是失败，需要删除链接',sql_lianj.delete_sql(apk_url))#删除数据库记录
                        sys.exit()

                order=params.xia_order(device,pkg_id)#游戏内下单拉微信(工作流第五节点-----下单)
                print('-------------------{}--{}--{}__{}---节点6----------------------------下单调起微信结果:{}'.format(ctime(),os.getpid(),device,apk_url[apk_url.find('&')+3:],order))
                log_file.log('------{}__{}---节点6-------下单调起微信结果:{}'.format(device,apk_url[apk_url.find('&')+3:][-20:],order))
                if order==False:
                    apk_cont=sql_lianj.condition_select(apk_url)
                    if apk_cont == None:sql_lianj.updata_sql(apk_url);os.system('adb -s {} shell rm -rf /sdcard/.dalan'.format(device));sys.exit()
                    elif apk_cont == 1:
                        print(device+'执行2次了还是失败，需要删除链接',sql_lianj.delete_sql(apk_url))#删除数据库记录
                        sys.exit()
            continue
        if  aa['data']['game_original_name'] not in game_list:
            node_start_time_n=int(time.time())
            print('{}--{}--{}--{}此原名游戏尚未接入，敬请期待'.format(ctime(),os.getpid(),device,apk_url))
            log_file.log('{}__{}此原名游戏尚未接入，敬请期待'.format(device,apk_url[apk_url.find('&')+3:][-20:]))
            report_API.get_images({'Game_link':apk_url}, pkg_id, '游戏未接入', '此原名游戏尚未接入，敬请期待', 0,node_start_time_n)
    else:
        node_start_time_n1=int(time.time())
        print('{}--{}--{}--{}_非Dalan_Dsdk渠道包，不走自动化流程'.format(ctime(),os.getpid(),device,apk_url))
        log_file.log('{}__{}_非Dalan_Dsdk渠道包，不走自动化流程'.format(device,apk_url[apk_url.find('&')+3:][-20:]))
        report_API.get_images({'Game_link':apk_url}, pkg_id, '非大蓝渠道', '非Dalan_Dsdk渠道包，不走自动化流程', 0,node_start_time_n1)
    print(device+'执行完成清除链接',sql_lianj.delete_sql(apk_url))#删除数据库记录
    os.system('adb -s {} uninstall {}'.format(device,package_name))#卸载执行成功的包


def test_run():
    current_time = time.strftime("%Y-%m-%d")
    if os.path.exists(os.path.dirname(__file__)+'/all_log/all_print/'+current_time+'.log'):
        pass
    else:
        open(os.path.dirname(__file__)+'/all_log/all_print/'+current_time+'.log','w')
    #执行前获取文件总行数
    object=log_read.cd_file(os.path.dirname(__file__)+'/all_log/all_print/'+current_time+'.log')
    count=object.file()
    #创建sys.stdout并准备
    r_obj=log_print_test.__redirection__()#创建sys.stdout对象
    sys.stdout=r_obj
    r_obj.to_file(os.path.dirname(__file__)+'/all_log/all_print/'+current_time+'.log')#把print写入的文件路径
    apk_list=dalan_test()#获取数据库链接
    r_obj.to_console()#放在print的前，则不写print数据到文件，print直接打在控制台(如果放在print后就写入文件，不在控制台打印)
    #开始实现多进程
    process.dalan_main(config.devices(),apk_list)
    print('------------------------------------------------重新获取log增量文件---------------------------------------------------------------------------')
    time.sleep(5)
    report=object.zai_read(count)#读取增量
    re_read=log_read.cd_file(os.path.dirname(__file__)+'/all_log/part_log/'+current_time+'执行关键点_日志.log')
    log_log=re_read.log_re()
    log_email.email(report+'\n'+log_log)

if __name__ == '__main__':
    #apk_list=dalan_test()#获取数据库链接
    #开始实现多进程
    #process.dalan_main(config.devices(),apk_list)
    test_run()#被调

