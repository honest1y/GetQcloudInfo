# -*- coding:utf-8 -*-
# @Time    : 2019/1/16 9:34
# @Author  : Wangxiao
# @FileName: Client.py

from tencentcloud.common import credential
SecretId = ""
SecretKey = ""
def get_cred():
    cred = credential.Credential(SecretId, SecretKey)
    return cred