#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import urllib.parse
import requests
import hashlib
import json
from dalan_tools import config
#----------------------查询服务端资源用于拆包校验__需要签名(只查询不做其他操作)------------------------------
def _sign(params, key):
    change = ksort(params)
    encode_str = urllib.parse.urlencode(change) + key
    sign = hashlib.md5(encode_str.encode()).hexdigest()
    return sign

def ksort(d):
    return [(k, d[k]) for k in sorted(d.keys())]


def get_images(pkgId):
    'u''根据pkg_id获取资源接口__需要签名'''
    params = {
        'time': int(time.time()),
        'pkgId': pkgId#998
    }
    key = 'a0bec9ac4193440a9bd4afc4e38a9b10'
    params['sign'] = _sign(params, key)
    environment=config.using_huanj()
    if environment=='test':
        r = requests.get('http://pkg.local.superdalan.com/api.pkgFlowReport/pkgParam', params=params)
    elif environment=='production':
        r = requests.get('http://pkg.superdalan.com/api.pkgFlowReport/pkgParam', params=params)

    json_obj = json.loads(r.text)
    return  json_obj


if __name__ == '__main__':
    ##通过pkgId获取apk资源链接
    dict=get_images(2857)#调用获取apk资
    print(dict)
    print(dict['data']['file'])

