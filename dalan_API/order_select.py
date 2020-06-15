#!/usr/bin/env python
# encoding: utf-8
__author__ = "晨晨"
import urllib.parse
import requests
import hashlib
import json
from dalan_tools import config
#——-------------------------------------------查询订单发货状态---------------------------------------------
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

def select_order(order_id):
    params = {
        'order_sn': order_id
    }
    key = '53f25fcd839690707c5c87f58e9715c4'
    params['sign'] = _sign(params, key)
    environment=config.using_huanj()
    print(environment)#读取环境
    if environment=='test':
        r = requests.post('http://authorize.local.aidalan.com/v1/PayNew/queryOrderDeliveryStatus', data=params)
    elif environment=='production':
        r = requests.post('https://authorize.aidalan.com/v1/PayNew/queryOrderDeliveryStatus', data=params)
    json_obj = json.loads(r.text)
    print(json_obj)
    return json_obj["msg"]


if __name__ == '__main__':
    select_order(2020042737087372351)