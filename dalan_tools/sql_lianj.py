#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
# 打开数据库连接
def sql_select():
    'u''查数据'''
    db = pymysql.connect(host='192.168.20.187',user='root',password='',db='dalan',charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "SELECT * FROM ceshi2"
    list_apk=[]
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            #print(row)# 打印结果
            #print("fname=%s,\t lname=%s" %(fname, lname))
            list_apk.append(row[0])
    except:
       print ("Error: unable to fetch data")
    #print(list_apk)
    return list_apk
    # 关闭数据库连接
    db.close()


def condition_select(apk_link):
    '''条件查询'''
    db = pymysql.connect(host='192.168.20.187',user='root',password='',db='dalan',charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "SELECT apk_count FROM ceshi2 where apk_link='%s';"%apk_link
    cursor.execute(sql)
    results = cursor.fetchone()
    return results[0]
    db.close()




def updata_sql(apk_link):
    '''更新数据'''
    db = pymysql.connect(host='192.168.20.187',user='root',password='',db='dalan',charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql="UPDATE ceshi2 set apk_count='1' where apk_link='%s';"%apk_link
    cursor.execute(sql)
    db.commit()
    return True
    db.close()


def delete_sql(apk):
    'u''清空表'''
    db = pymysql.connect(host='192.168.20.187',user='root',password='',db='dalan',charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = "delete from ceshi2 where apk_link='%s';"%apk
    cursor.execute(sql)#执行sql
    db.commit()# 提交修改(相当于确定)
    return  '-------------------------------------------------------------delete OK-----------------------------------------------------------'
    # 关闭数据库连接
    db.close()

#print(sql_select())
#print(condition_select('http://pkg.superdalan.com/game.pkg/download?pkgId=2715&f=chwymxdzjtt_dalan_xy_dsdk_74_1.0.0_20200515_163704.apk'))
#print(delete_sql())




