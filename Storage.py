# -*- coding:utf-8 -*-
# @Time    : 2019/1/16 11:42
# @Author  : Wangxiao
# @FileName: Storage.py

import json, Client
from tencentcloud.vpc.v20170312 import vpc_client
from tencentcloud.cbs.v20170312 import cbs_client
from tencentcloud.cbs.v20170312 import models as cbs_models
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

cred = Client.get_cred()

def get_cbs(Region_Id):
    """
    查询 云硬盘 列表
    :param config_dict:
    :return: InstanceId
    """
    describe_request = cbs_models.DescribeDisksRequest()
    try:
        clt = cbs_client.CbsClient(cred, Region_Id)
        response = clt.DescribeDisks(describe_request)
        result_content = response.to_json_string()
        return json.loads(result_content)
    except TencentCloudSDKException as e:
        print(e)

