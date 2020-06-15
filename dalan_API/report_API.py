#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import urllib.parse
import requests
import hashlib
import json
from dalan_tools import config
#——--------------------------节点结果上报接口---------------------------------------------
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

def get_images(node_args,pkg_id,nodeName,nodeResult,nodeStatus,node_start_time,file_code=' '):
    sign_time = int(time.time())
    print(sign_time)
    node_end_time = int(time.time())
    params = {
        'time': sign_time,
        'pkgId': pkg_id,
        'nodeName': nodeName,
        'nodeArgs': json.dumps(node_args),
        'nodeResult': nodeResult ,
        'nodeFinishTime': node_end_time,
        'nodeStartTime': node_start_time,
        'fileCode': file_code,
        'nodeStatus': nodeStatus
    }
    key = 'a0bec9ac4193440a9bd4afc4e38a9b10'
    params['sign'] = _sign(params, key)
    environment=config.using_huanj()
    print(environment)#读取环境
    if environment=='test':
        r = requests.post('http://pkg.local.superdalan.com/api.pkgFlowReport/receiptData', data=params)
    elif environment=='production':
        r = requests.post('http://pkg.superdalan.com/api.pkgFlowReport/receiptData', data=params) #http://pkg.local.superdalan.com/api.game/images(测试环境)
    json_obj = json.loads(r.text)
    print(json_obj)


if __name__ == '__main__':
    node_start_time = int(time.time())
    get_images({},1282,'包体下载','包体下载成功',0,node_start_time)
