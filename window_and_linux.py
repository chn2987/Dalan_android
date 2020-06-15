#!/usr/bin/env python
# -*- coding: utf-8 -*-
import winrm
'''
Python中的pywirm模块可以很好的解决远程调用的问题
'''
wintest=winrm.Session('192.168.10.32:5985/wsman',auth=('Administrator','123456'))
wintest.run_cmd("python D:/dalan/python/xuexi/test3/661.py")

