# -*- coding:utf-8 -*-
# @Time    : 2019/1/16 13:24
# @Author  : Wangxiao
# @FileName: FormatData.py
import Calculate, Network, Storage, Database, Security


def format_cvm(Region_Id):
    response = Calculate.get_cvm(Region_Id)
    if response['TotalCount'] != 0:
        result = []
        for line in response['InstanceSet']:
            data = (
                line.get('InstanceId'),
                line.get('Placement')['Zone'],
                line.get('InstanceName'),
                line.get('InstanceType'),
                line.get('OsName'),
                line.get('PrivateIpAddresses')[0]
            )
            result.append(data)
        return result

def format_clb(Region_Id):
    response = Calculate.get_clb(Region_Id)
    if response['TotalCount'] != 0:
        result = []
        for line in response['LoadBalancerSet']:
            if line.get('Forward') == 1:
                Type = '应用型'
            else:
                Type = '传统型'
            if line.get('Status') == 1:
                Status = '正常运行'
            else:
                Status = '创建中'
            data = (
                line.get('LoadBalancerId'),
                Region_Id,
                line.get('LoadBalancerName'),
                Type,
                Status,
                line.get('LoadBalancerVips')[0]
            )
            result.append(data)
        return result

def format_vpc(Region_Id):
    response  = Network.get_vpc(Region_Id)
    if response['TotalCount'] != 0:
        result = []
        for line in response['VpcSet']:
            data = (
                line.get('VpcId'),
                Region_Id,
                line.get('VpcName'),
                line.get('CidrBlock'),
                line.get('IsDefault'),
                line.get('EnableMulticast')
            )
            result.append(data)
        return result
def format_EIP(Region_Id):
    response  = Network.get_EIP(Region_Id)
    if response['TotalCount'] != 0:
        result = []
        for line in response['AddressSet']:
            data = (
                line.get('AddressId'),
                Region_Id,
                line.get('AddressStatus'),
                line.get('AddressIp'),
                line.get('AddressType'),
                line.get('IsEipDirectConnection')
            )
            result.append(data)
        return result

def format_VPN(Region_Id):
    response  = Network.get_VPN(Region_Id)
    if response['TotalCount'] != 0:
        result = []
        for line in response['VpnGatewaySet']:
            data = (
                line.get('VpnGatewayId'),
                Region_Id,
                line.get('State'),
                line.get('PublicIpAddress'),
                line.get('Type'),
                line.get('InternetMaxBandwidthOut')
            )
            result.append(data)
        return result

def format_DirectConnect(Region_Id):
    response  = Network.get_DirectConnect(Region_Id)
    if response['TotalCount'] != 0:
        result = []
        for line in response['DirectConnectGatewaySet']:
            data = (
                line.get('DirectConnectGatewayId'),
                Region_Id,
                line.get('DirectConnectGatewayName'),
                line.get('DirectConnectGatewayIp'),
                line.get('GatewayType'),
                line.get('EnableBGP')
            )
            result.append(data)
        return result

def format_BandPackges(Region_Id):
    response  = Network.get_BandwidthPackages(Region_Id)
    if response['TotalCount'] != 0:
        result = []
        for line in response['BandwidthPackageSet']:
            data = (
                line.get('BandwidthPackageId'),
                Region_Id,
                line.get('BandwidthPackageName'),
                line.get('ChargeType'),
                line.get('NetworkType'),
                line.get('Status')
            )
            result.append(data)
        return result

def format_cbs(Region_Id):
    response  = Storage.get_cbs(Region_Id)
    if response['TotalCount'] != 0:
        result = []
        for line in response['DiskSet']:
            data = (
                line.get('DiskId'),
                Region_Id,
                line.get('Attached'),
                line.get('DiskState'),
                line.get('DiskSize'),
                line.get('DiskType')
            )
            result.append(data)
        return result

def format_mysql(Region_Id):
    response  = Database.get_mysql(Region_Id)
    if response['TotalCount'] != 0:
        result = []
        for line in response['Items']:
            if line.get('Status') == 0:
                Status = '创建中'
            elif line.get('Status') == 1:
                Status = '运行中'
            elif line.get('Status') == 4:
                Status = '隔离中'
            else:
                Status = '已隔离'
            data = (
                line.get('InstanceId'),
                Region_Id,
                Status,
                line.get('Volume'),
                line.get('Vip'),
                line.get('Vport')
            )
            result.append(data)
        return result

def format_sqlserver(Region_Id):
    response  = Database.get_sqlserver(Region_Id)
    if response == None:
        pass
    else:
        if response['TotalCount'] != 0:
            result = []
            for line in response['InstanceSet']:
                if line.get('Status') == 1:
                    Status = '申请中'
                elif line.get('Status') == 2:
                    Status = '运行中'
                elif line.get('Status') == 3:
                    Status = '受限运行中'
                elif line.get('Status') == 4:
                    Status = '已隔离'
                elif line.get('Status') == 5:
                    Status = '回收中'
                elif line.get('Status') == 6:
                    Status = '已回收'
                elif line.get('Status') == 7:
                    Status = '任务执行中'
                elif line.get('Status') == 8:
                    Status = '已下线'
                elif line.get('Status') == 9:
                    Status = '实例扩容中'
                elif line.get('Status') == 10:
                    Status = '实例迁移中'
                elif line.get('Status') == 11:
                    Status = '只读'
                elif line.get('Status') == 12:
                    Status = '重启中'
                data = (
                    line.get('InstanceId'),
                    Region_Id,
                    Status,
                    line.get('Storage'),
                    line.get('Vip'),
                    line.get('Vport')
                )
                result.append(data)
            return result

def format_redis(Region_Id):
    response  = Database.get_redis(Region_Id)
    if response == None:
        pass
    else:
        if response['TotalCount'] != 0:
            result = []
            for line in response['InstanceSet']:
                if line.get('Status') == 0:
                    Status = '待初始化'
                elif line.get('Status') == 1:
                    Status = '流程中'
                elif line.get('Status') == 2:
                    Status = '运行中'
                elif line.get('Status') == -2:
                    Status = '已隔离'
                elif line.get('Status') == -3:
                    Status = '待删除'
                data = (
                    line.get('InstanceId'),
                    Region_Id,
                    Status,
                    line.get('Size'),
                    line.get('WanIp'),
                    line.get('Port')
                )
                result.append(data)
            return result

def format_mariadb(Region_Id):
    response  = Database.get_mariadb(Region_Id)
    if response == None:
        pass
    else:
        if response['TotalCount'] != 0:
            result = []
            for line in response['Instances']:
                if line.get('Status') == 0:
                    Status = '创建中'
                elif line.get('Status') == 1:
                    Status = '流程处理中'
                elif line.get('Status') == 2:
                    Status = '运行中'
                elif line.get('Status') == 3:
                    Status = '实例未初始化'
                elif line.get('Status') == -1:
                    Status = '已隔离'
                elif line.get('Status') == -2:
                    Status = '已删除'
                data = (
                    line.get('InstanceId'),
                    Region_Id,
                    Status,
                    line.get('Storage'),
                    line.get('Vip'),
                    line.get('Vport')
                )
                result.append(data)
            return result


def format_postgres(Region_Id):
    response = Database.get_postgres(Region_Id)
    if response == None:
        pass
    else:
        if response['TotalCount'] != 0:
            result = []
            for line in response['DBInstanceSet']:
                if line.get('Status') == 1:
                    Type = '主实例'
                elif line.get('Status') == 1:
                    Type = '只读实例'
                elif line.get('Status') == 3:
                    Type = '灾备实例'
                else:
                    Type = '临时实例'
                data = (
                    line.get('DBInstanceId'),
                    Region_Id,
                    Type,
                    line.get('DBInstanceStorage'),
                    line.get('DBInstanceStatus'),
                    line.get('DBVersion')
                )
                result.append(data)
            return result

def format_yunjing(Region_Id):
    response  = Security.get_yunjing(Region_Id)
    result = (
        response['OnlineMachineNum'],
        response['ProVersionMachineNum'],
        response['MalwareNum'],
        response['NonlocalLoginNum'],
        response['BruteAttackSuccessNum'],
        response['VulNum'],
    )
    return result