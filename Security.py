# -*- coding:utf-8 -*-
# @Time    : 2019/1/16 13:51
# @Author  : Wangxiao
# @FileName: Security.py

import json, Client
from tencentcloud.yunjing.v20180228 import yunjing_client
from tencentcloud.yunjing.v20180228 import models as yunjing_models
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

cred = Client.get_cred()
def get_yunjing(Region_Id):
    """
    查询 云镜 列表
    :param config_dict:
    :return: InstanceId
    """
    describe_request = yunjing_models.DescribeOverviewStatisticsRequest()
    try:
        clt = yunjing_client.YunjingClient(cred, Region_Id)
        response = clt.DescribeOverviewStatistics(describe_request)
        result_content = response.to_json_string()
        return json.loads(result_content)
    except TencentCloudSDKException as e:
        print(e)