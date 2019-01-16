# -*- coding:utf-8 -*-
# @Time    : 2019/1/16 12:19
# @Author  : Wangxiao
# @FileName: Database.py

import json, Client
from tencentcloud.cdb.v20170320 import cdb_client
from tencentcloud.cdb.v20170320 import models as cdb_models
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sqlserver.v20180328 import sqlserver_client
from tencentcloud.sqlserver.v20180328 import models as sqlserver_models
from tencentcloud.redis.v20180412 import redis_client
from tencentcloud.redis.v20180412 import models as redis_models
from tencentcloud.mariadb.v20170312 import mariadb_client
from tencentcloud.mariadb.v20170312 import models as mariadb_models
from tencentcloud.postgres.v20170312 import postgres_client
from tencentcloud.postgres.v20170312 import models as postgres_models

cred = Client.get_cred()
def get_mysql(Region_Id):
    """
    查询 MySQL 列表
    :param config_dict:
    :return: InstanceId
    """
    describe_request = cdb_models.DescribeDBInstancesRequest()
    try:
        clt = cdb_client.CdbClient(cred, Region_Id)
        response = clt.DescribeDBInstances(describe_request)
        result_content = response.to_json_string()
        return json.loads(result_content)
    except TencentCloudSDKException as e:
        print(e)

def get_sqlserver(Region_Id):
    """
    查询 SQL Server 列表
    :param config_dict:
    :return: InstanceId
    """
    describe_request = sqlserver_models.DescribeDBInstancesRequest()
    try:
        clt = sqlserver_client.SqlserverClient(cred, Region_Id)
        response = clt.DescribeDBInstances(describe_request)
        result_content = response.to_json_string()
        return json.loads(result_content)
    except TencentCloudSDKException as e:
        print(e)

def get_redis(Region_Id):
    """
    查询 Redis 列表
    :param config_dict:
    :return: InstanceId
    """
    describe_request = redis_models.DescribeInstancesRequest()
    try:
        clt = redis_client.RedisClient(cred, Region_Id)
        response = clt.DescribeInstances(describe_request)
        result_content = response.to_json_string()
        return json.loads(result_content)
    except TencentCloudSDKException as e:
        print(e)

def get_mariadb(Region_Id):
    """
    查询 Mariadb 列表
    :param config_dict:
    :return: InstanceId
    """
    describe_request = mariadb_models.DescribeDBInstancesRequest()
    try:
        clt = mariadb_client.MariadbClient(cred, Region_Id)
        response = clt.DescribeDBInstances(describe_request)
        result_content = response.to_json_string()
        return json.loads(result_content)
    except TencentCloudSDKException as e:
        print(e)

def get_postgres(Region_Id):
    """
    查询 PostGreSQL 列表
    :param config_dict:
    :return: InstanceId
    """
    describe_request = postgres_models.DescribeDBInstancesRequest()
    try:
        clt = postgres_client.PostgresClient(cred, Region_Id)
        response = clt.DescribeDBInstances(describe_request)
        result_content = response.to_json_string()
        return json.loads(result_content)
    except TencentCloudSDKException as e:
        print(e)