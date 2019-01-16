# -*- coding:utf-8 -*-
# @Time    : 2019/1/16 10:10
# @Author  : Wangxiao
# @FileName: Network.py

import json, Client
from tencentcloud.vpc.v20170312 import vpc_client
from tencentcloud.vpc.v20170312 import models as vpc_models
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

cred = Client.get_cred()
def get_vpc(Region_Id):
    """
    查询 VPC 列表
    :param config_dict:
    :return: InstanceId
    """
    describe_request = vpc_models.DescribeVpcsRequest()
    try:
        clt = vpc_client.VpcClient(cred, Region_Id)
        response = clt.DescribeVpcs(describe_request)
        result_content = response.to_json_string()
        return json.loads(result_content)
    except TencentCloudSDKException as e:
        print(e)

def get_EIP(Region_Id):
    """
    查询 EIP 列表
    :param config_dict:
    :return: InstanceId
    """
    describe_request = vpc_models.DescribeAddressesRequest()
    try:
        clt = vpc_client.VpcClient(cred, Region_Id)
        response = clt.DescribeAddresses(describe_request)
        result_content = response.to_json_string()
        return json.loads(result_content)
    except TencentCloudSDKException as e:
        print(e)

def get_VPN(Region_Id):
    """
    查询 VPN 列表
    :param config_dict:
    :return: InstanceId
    """
    describe_request = vpc_models.DescribeVpnGatewaysRequest()
    try:
        clt = vpc_client.VpcClient(cred, Region_Id)
        response = clt.DescribeVpnGateways(describe_request)
        result_content = response.to_json_string()
        return json.loads(result_content)
    except TencentCloudSDKException as e:
        print(e)

def get_DirectConnect(Region_Id):
    """
    查询 DirectConnect专线网关 列表
    :param config_dict:
    :return: InstanceId
    """
    describe_request = vpc_models.DescribeDirectConnectGatewaysRequest()
    try:
        clt = vpc_client.VpcClient(cred, Region_Id)
        response = clt.DescribeDirectConnectGateways(describe_request)
        result_content = response.to_json_string()
        return json.loads(result_content)
    except TencentCloudSDKException as e:
        print(e)

def get_BandwidthPackages(Region_Id):
    """
    查询 带宽包 列表
    :param config_dict:
    :return: InstanceId
    """
    describe_request = vpc_models.DescribeBandwidthPackagesRequest()
    try:
        clt = vpc_client.VpcClient(cred, Region_Id)
        response = clt.DescribeBandwidthPackages(describe_request)
        result_content = response.to_json_string()
        return json.loads(result_content)
    except TencentCloudSDKException as e:
        print(e)