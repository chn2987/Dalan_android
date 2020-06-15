#!/usr/bing/env python
# -*- coding: utf-8 -*-
import os
from time import ctime
from PIL import Image
from dalan_API import api_img_xiazai_main


#—————————————————功能：两张图片相似度对比————————————————————
class CompareImage():
    def calculate(self, image1, image2):
        g = image1.histogram()
        s = image2.histogram()
        assert len(g) == len(s), "error"
        data = []
        for index in range(0, len(g)):
            if g[index] != s[index]:
                data.append(1 - abs(g[index] - s[index]) / max(g[index], s[index]))
            else:
                data.append(1)
        return sum(data) / len(g)

    def split_image(self, image, part_size):
        pw, ph = part_size
        w, h = image.size
        sub_image_list = []
        assert w % pw == h % ph == 0, "error"
        for i in range(0, w, pw):
            for j in range(0, h, ph):
                sub_image = image.crop((i, j, i + pw, j + ph)).copy()
                sub_image_list.append(sub_image)
        return sub_image_list

    def compare_image(self, file_image1, file_image2, size=(256, 256), part_size=(64, 64)):
        '''
        'file_image1'和'file_image2'是传入的文件路径
         可以通过'Image.open(path)'创建'image1' 和 'image2' Image 对象.
         'size' 重新将 image 对象的尺寸进行重置，默认大小为256 * 256 .
         'part_size' 定义了分割图片的大小.默认大小为64*64 .
         返回值是 'image1' 和 'image2'对比后的相似度，相似度越高，图片越接近，达到1.0说明图片完全相同。
        '''
        try:
            image1 = Image.open(file_image1)
            image2 = Image.open(file_image2)
            img1 = image1.resize(size).convert("RGB")
            sub_image1 = self.split_image(img1, part_size)
            img2 = image2.resize(size).convert("RGB")
            sub_image2 = self.split_image(img2, part_size)
            sub_data = 0
            for im1, im2 in zip(sub_image1, sub_image2):
                sub_data += self.calculate(im1, im2)
            x = size[0] / part_size[0]
            y = size[1] / part_size[1]
            pre = round((sub_data / (x * y)), 6)
            # print(str(pre * 100) + '%')
            #print('Compare the image result is: ' + str(pre))
            return pre
        except:
            return 0

    def img_run(self,img_path,apk_path,pkgId,server_img,device):
        '''获取遍历图片'''
        try:
            jieguo=[]
            path=os.path.dirname(os.path.dirname(__file__))+'/File_directory/'+'img/'
            type1='.jpg'
            print('{}--{}--实际图片对应路径{}，拆包后后apk目录{}，对应pkg_id={}'.format(os.getpid(),device,img_path,apk_path,pkgId))
            print('%s--%s--%s服务端素材图片%s'%(ctime(),os.getpid(),device,server_img))
            for key,value in img_path.items():
                if value:
                    #print(value)
                    for i in range(len(server_img)):
                         jieguo.append(image.compare_image(path+server_img[i],apk_path+value))#img_path,, apk_img_path
            app_name= api_img_xiazai_main.get_images(pkgId)
            os.system(r"java -jar c:/test.jar "+apk_path+"/AndroidManifest.xml >> "+apk_path+"/test.txt")
            print('{}--apk的应用名称={}'.format(device,app_name['data']['game_app_name']))
            with open(apk_path+"test.txt",mode="r",encoding="gbk",errors="ignore") as abc:
                fileContent=abc.read()
            if len(server_img)==jieguo.count(1.0) and app_name['data']['game_app_name'] in fileContent:
                print('{}--素材及应用名验证成功,期望匹配数{}，实际匹配数{}'.format(device,len(server_img),jieguo.count(1.0)))
                return True,server_img
            elif len(server_img)==jieguo.count(1.0):
                #print('只有图片素材验证成功,期望匹配数{}，实际匹配数{}'.format(len(list_img),jieguo.count(1.0)))
                return False, '只有图片匹配成功_应用名失败'
            elif app_name['data']['game_app_name'] in fileContent:
                return False,'只有应用名称匹配成功_图片失败'
            else:
                print('{}素材及应用名验证失败,期望值={},实际值={}'.format(device,len(server_img),jieguo.count(1.0)))
                return False, '素材及应用名都匹配失败'
        except:
            return False, '素材验证时出现未知异常！需要调优'

image = CompareImage()


if __name__=="__main__":
    aaa={'splash': '', 'decompression': '', 'load': 'assets/loadingbg.jpg', 'login': 'assets/selectserverbg.jpg', 'mp3_file': '', 'logo': ''}
    bbb=r'D:\Downloads\zyrghb_dalan_dsdk_48_1.0.0_20200422_181857/'
    image=CompareImage()
    image.img_run(aaa,bbb,2590,['99de8fe120359e6c0283d85edf04971d.jpg', '33a5032c20d6e161ac107776183b27af.jpg'],'chenwei')
    #print(image.compare_image(r'D:\Downloads\img\123123.png',r'D:\Downloads\img\123123.png'))
    ###################################
    # yuan=r"D:\Downloads"
    # hou=r"E:\test\python\temp"
    # a={"3333.png":"33333.png","9999.png":"5551.png"}
    # image = CompareImage()
    # for key,value in a.items():
    #     image.compare_image(yuan+'\\'+key,hou+'\\'+value)



