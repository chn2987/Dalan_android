#!/usr/bin/env python
# encoding: utf-8
__author__ = "晨晨"
import smtplib,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def email(text):
    fromaddr = '646572031@qq.com'
    password = 'ufxuoifkuvutbcij'#第三方授权码(不能直接用密码)
    toaddrs = ['chenwei@aidalan.com']#接收人
    #邮件正文
    content =text
    textApart = MIMEText(content)

    #创建封装对象(实例化邮件对象)
    m = MIMEMultipart()
    m.attach(textApart)
    m['Subject'] = '工作流自动化测试log记录'+time.strftime('%Y-%m-%d %H:%M:%S')
    try:
        server = smtplib.SMTP('smtp.qq.com')#邮件服务器地址(不同邮件类型地址不一样)
        server.login(fromaddr,password)#登录邮箱
        server.sendmail(fromaddr, toaddrs, m.as_string())#发送邮件
        print('success')#发送状态
        server.quit()#退出邮件服务
    except smtplib.SMTPException as e:
        print('error:',e) #打印错误
    #input('等待_用于直接运行py文件避免闪退')

if __name__ == '__main__':
    email('这是一封测试邮件')

