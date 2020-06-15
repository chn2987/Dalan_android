#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import time
####################------------------pkg打包成功后上报apk地址到数据库-----------------------------------
# 注册接口
import flask
import pymysql
from flask import request, jsonify  # 想获取到请求参数的话，就得用这个

server = flask.Flask(__name__)  # 把这个python文件当做一个web服务


def get_conn():
    return pymysql.connect(host='47.106.143.23', user='root', password='Chen_123', db='dalan', charset='utf8')
    # return pymysql.connect(host='192.168.20.214', user='root', password='', db='test', charset='utf8')


# 数据查询
def _select(sql, data=()):
    conn = get_conn()  # 获取操作游标
    with conn.cursor() as cursor:
        cursor.execute(sql, data)  # 执行sql
        res = cursor.fetchone()  # 获取查询结果
        server.logger.info(res)  # 记录日志
    conn.commit()  # 提交到数据库执行
    conn.close()  # 关闭数据库连接
    return res


# 数据写入
def _insert(sql, data=()):
    conn = get_conn()
    with conn.cursor() as cursor:
        # 执行sql
        res = cursor.execute(sql, data)
    conn.commit()
    conn.close()
    return res


# 响应
def respond(flag, code, msg='',user_id='',user_name=''):
    ret = {
        'code': code,
        'status': flag,
        'msg': msg,
        'user_id':user_id,
        'user_name':user_name
    }
    server.logger.info(ret)
    return jsonify(ret)


@server.route('/register', methods=['post'])  # router里面第一个参数，是接口的路径
def reg():
    apk_link = request.values.get('apk_link')  # 这里就是你调用接口的是传入的参数
    server.logger.info("request addr: {}".format(apk_link))
    server.logger.info("request url: {}".format(request.url))
    if apk_link is None:
	server.logger.info("request addr wrongful01")
        return respond(True, 500, msg='地址不合法')
    # 判断传参是否合法
    if re.match(r'^https?:/{2}.+$', apk_link) is None:
    #if re.match(r'^https?:/{2}pkg.superdalan.com.+$', apk_link) is None:
	server.logger.info("request addr wrongful02")
        return respond(True, 500, msg='地址不合法')
    if apk_link:
        try:
            sql = "select apk_link,creation_time from ceshi2 where apk_link=%s"
            res = _select(sql, (apk_link,))  # 执行sql
            server.logger.info(res)  # 把查询结果写入日志
            if res:
		server.logger.info("user exist")
                return respond(True, 300, msg='你注册的用户已经存在')
            else:
                date_time = time.strftime("%Y-%m-%d %H:%M:%S")
                sql = "insert into ceshi2(apk_link, creation_time) values(%s, %s)"
                _insert(sql, (apk_link, date_time))
		server.logger.info("register success")
                return respond(True, 200, msg="注册成功!",user_id="19878564",user_name="18520103625")
        except:
	    server.logger.info("handle error")
            return respond(False, 500, msg="异常!")
    else:
        return respond(False, 938, msg="必填参数未填，请看接口文档！")


if __name__ == '__main__':
    server.run(port=8000, debug=True, host='0.0.0.0')

