# -*- coding:utf-8 -*-
# @Time    : 2019/1/16 9:34
# @Author  : Wangxiao
# @FileName: Client.py

from tencentcloud.common import credential
import configparser

config = configparser.ConfigParser()
config.read('config.txt')
SecretId = config['common']['secret_id']
SecretKey = config['common']['secret_key']
def get_cred():
    cred = credential.Credential(SecretId, SecretKey)
    return cred