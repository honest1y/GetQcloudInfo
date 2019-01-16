# -*- coding:utf-8 -*-
# @Time    : 2019/1/16 9:33
# @Author  : Wangxiao
# @FileName: Calculate.py

import json, Client
from tencentcloud.clb.v20180317 import clb_client
from tencentcloud.clb.v20180317 import models as clb_models
from tencentcloud.cvm.v20170312 import cvm_client
from tencentcloud.cvm.v20170312 import models as cvm_models
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

cred = Client.get_cred()
def get_cvm(Region_Id):
    """
    查询实例列表
    :param config_dict:
    :return: InstanceId
    """
    describe_request = cvm_models.DescribeInstancesRequest()
    try:
        clt = cvm_client.CvmClient(cred, Region_Id)
        response = clt.DescribeInstances(describe_request)
        result_content = response.to_json_string()
        return json.loads(result_content)
    except TencentCloudSDKException as e:
        print(e)

def get_clb(Region_Id):
    """
    查询 CLB 列表
    :param config_dict:
    :return: InstanceId
    """
    describe_request = clb_models.DescribeLoadBalancersRequest()
    try:
        clt = clb_client.ClbClient(cred, Region_Id)
        response = clt.DescribeLoadBalancers(describe_request)
        result_content = response.to_json_string()
        return json.loads(result_content)
    except TencentCloudSDKException as e:
        print(e)