#!/usr/bin/env python
# encoding: utf-8
__author__ = "晨晨"
import time
import urllib.parse
import requests
import hashlib
import json
from dalan_tools import config
#——--------------------------查询节点数据---------------------------------------------
def _sign(params, key):
    change = ksort(params)
    encode_param = urllib.parse.urlencode(change)
    decode_param = urllib.parse.unquote_plus(encode_param)
    encode_str = decode_param + key

    m = hashlib.md5()
    m.update(encode_str.encode('utf-8'))
    sign = m.hexdigest()
    return sign

def ksort(d):
    return [(k, d[k]) for k in sorted(d.keys())]

def get_images(pkg_id,nodeName):
    sign_time = int(time.time())#获取当前时间戳
    params = {
        'time': 1578398968,
        'pkgId': pkg_id,
        'nodeName': nodeName
    }
    key = 'a0bec9ac4193440a9bd4afc4e38a9b10'
    params['sign'] = _sign(params, key)
    environment=config.using_huanj()
    if environment=='test':
        r = requests.get('http://pkg.local.superdalan.com/api.pkgFlowReport/data',  params=params)
    elif environment=='production':
        r = requests.get('http://pkg.superdalan.com/api.pkgFlowReport/data',  params=params)
    json_obj = json.loads(r.text)
    print(json_obj)


if __name__ == '__main__':
    get_images(2695,'打开游戏')

