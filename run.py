# -*- coding:utf-8 -*-
# @Time    : 2019/1/16 9:43
# @Author  : Wangxiao
# @FileName: run.py

import FormatData, xlsxwriter

def excel(workbook):
    CVMTitle = ['实例ID', '可用区', '名称','类型','系统', 'IP']
    VPCTitle = ['VpcID', '地域', 'VPC名称','网段', '是否默认', '是否开启组播']
    EIPTitle = ['EIPID', '地域', '状态','地址','类型', '是否支持直通模式']
    VPNTitle = ['VPNID', '地域', '状态', 'IP', '类型', '带宽']
    BPSTitle = ['带宽包ID', '地域', '名称', '付费方式', '类型', '状态']
    CLBTitle = ['CLBID', '地域', '名称', '类型', '状态', 'VIP']
    DCTitle = ['专线ID', '地域', '专线名称', '专线IP', '网关类型', '是否启用BGP']
    DSKTitle = ['磁盘ID', '地域', '是否挂载', '状态', '大小', '类型']
    MSQTitle = ['CDBID', '地域', '状态', '磁盘', 'VIP地址', '端口']
    SQSTitle = ['SQSID', '地域', '状态', '磁盘', 'VIP地址', '端口']
    RESTitle = ['RedisID', '地域', '状态', '磁盘', 'VIP地址', '端口']
    MRDTitle = ['MariadbID', '地域', '状态', '磁盘', 'VIP地址', '端口']
    PGSTitle = ['PostGreSQLID', '地域', '类型', '磁盘', '状态', '版本']
    YUJTitle = ['服务器在线数', '专业服务器数', '木马文件数', '异地登录数', '暴力破解成功数', '漏洞数']

    category_merge_format = workbook.add_format({
        'font_size': 20,
        'font_color': '#FFFFFF',
        'bold': True,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#171717'
    })
    merge_format = workbook.add_format({
        'bold': True,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#A2A2A2'
    })
    Title_format = workbook.add_format({
        'bold': True,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#87CEFF'
    })
    data_format = workbook.add_format({
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#EED8AE'
    })
    return CVMTitle, CLBTitle, VPCTitle, EIPTitle, VPNTitle, DCTitle, BPSTitle, DSKTitle, MSQTitle, SQSTitle, RESTitle, MRDTitle, PGSTitle, YUJTitle, category_merge_format, merge_format, Title_format, data_format
def main():
    workbook = xlsxwriter.Workbook('D:/Qcloud.xlsx')
    RegionList = ['ap-beijing', 'ap-shanghai', 'ap-guangzhou', 'ap-chengdu', 'ap-singapore']
    CVMTitle, CLBTitle, VPCTitle, EIPTitle, VPNTitle, DCTitle, BPSTitle, DSKTitle, MSQTitle, SQSTitle, RESTitle, MRDTitle, PGSTitle, YUJTitle, category_merge_format, merge_format, Title_format, data_format = excel(workbook)
    for region in RegionList:
        print('正在导出地区： {}'.format(region))
        worksheet = workbook.add_worksheet(region)
        # 计算类
        worksheet.merge_range('A1:F1', '计算类', category_merge_format)
        # 写入 CVM
        worksheet.merge_range('A2:F2', 'CVM信息', merge_format)
        worksheet.set_column('A:F', 35)
        worksheet.set_row(0, 25)
        global ECSNUM
        ECSNUM = 4
        cvm = FormatData.format_cvm(region)
        if cvm != None:
            worksheet.write_row('A3', CVMTitle, Title_format)
            # 如果结不为空，则代表有资源，则写入数据
            for item in cvm:
                worksheet.write_row('A' + str(ECSNUM), item, data_format)
                ECSNUM += 1
        # 否则，代表该地域无资源，写入 NULL
        else:
            worksheet.merge_range('A3:F3', 'NOT Found CVM', data_format)
        # 写入 CLB
        worksheet.merge_range('A{}:F{}'.format(ECSNUM, ECSNUM), '负载均衡信息', merge_format)
        worksheet.set_column('A:F', 35)
        worksheet.set_row(0, 25)
        clbs = FormatData.format_clb(region)
        if clbs != None:
            worksheet.write_row('A{}'.format(ECSNUM + 1), CLBTitle, Title_format)
            for clb in clbs:
                worksheet.write_row('A' + str(ECSNUM + 2), clb, data_format)
                ECSNUM += 1
        else:
            worksheet.merge_range('A{}:F{}'.format(ECSNUM + 1, ECSNUM + 1), 'NOT Found CLB', data_format)

        # 网络类
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 3, ECSNUM + 3), '网络类', category_merge_format)
        # 写入 VPC
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 4, ECSNUM + 4), 'VPC信息', merge_format)
        worksheet.set_column('A:F', 30)
        worksheet.set_row(0, 25)
        vpcs = FormatData.format_vpc(region)
        if len(vpcs) != 0:
            worksheet.write_row('A{}'.format(ECSNUM + 5), VPCTitle, Title_format)
            for vpc in vpcs:
                worksheet.write_row('A' + str(ECSNUM + 6), vpc, data_format)
                ECSNUM += 1
            ECSNUM -= 1
        else:
            worksheet.merge_range('A{}:F{}'.format(ECSNUM + 5, ECSNUM + 5), 'NOT Found VPC', data_format)
            ECSNUM -= 1


        # 写入 EIP
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 7, ECSNUM + 7), 'EIP信息', merge_format)
        worksheet.set_column('A:F', 30)
        worksheet.set_row(0, 25)
        eips = FormatData.format_EIP(region)
        if eips != None:
            worksheet.write_row('A{}'.format(ECSNUM + 8), EIPTitle, Title_format)
            for eip in eips:
                worksheet.write_row('A' + str(ECSNUM + 9), eip, data_format)
                ECSNUM += 1
            ECSNUM -= 1
        else:
            worksheet.merge_range('A{}:F{}'.format(ECSNUM + 8, ECSNUM + 8), 'NOT Found EIP', data_format)
            ECSNUM -= 1

        # 写入 VPN
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 10, ECSNUM + 10), 'VPN网关信息', merge_format)
        worksheet.set_column('A:F', 30)
        worksheet.set_row(0, 25)
        vpns = FormatData.format_VPN(region)
        if vpns != None:
            worksheet.write_row('A{}'.format(ECSNUM + 11), VPNTitle, Title_format)
            for vpn in vpns:
                worksheet.write_row('A' + str(ECSNUM + 12), vpn, data_format)
                ECSNUM += 1
            ECSNUM -= 1
        else:
            worksheet.merge_range('A{}:F{}'.format(ECSNUM + 11, ECSNUM + 11), 'NOT Found VPN', data_format)
            ECSNUM -= 1

        # 写入专线网关
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 13, ECSNUM + 13), '专线网关信息', merge_format)
        worksheet.set_column('A:F', 30)
        worksheet.set_row(0, 25)
        dcs = FormatData.format_DirectConnect(region)
        if dcs != None:
            worksheet.write_row('A{}'.format(ECSNUM + 14), DCTitle, Title_format)
            for dc in dcs:
                worksheet.write_row('A' + str(ECSNUM + 15), dc, data_format)
                ECSNUM += 1
            ECSNUM -= 1
        else:
            worksheet.merge_range('A{}:F{}'.format(ECSNUM + 14, ECSNUM + 14), 'NOT Found 专线网关', data_format)
            ECSNUM -= 1

        # 写入带宽包
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 16, ECSNUM + 16), '带宽包信息', merge_format)
        worksheet.set_column('A:F', 30)
        worksheet.set_row(0, 25)
        bps = FormatData.format_BandPackges(region)
        if bps != None:
            worksheet.write_row('A{}'.format(ECSNUM + 17), BPSTitle, Title_format)
            for bp in bps:
                worksheet.write_row('A' + str(ECSNUM + 18), bp, data_format)
                ECSNUM += 1
        else:
            worksheet.merge_range('A{}:F{}'.format(ECSNUM + 17, ECSNUM + 17), 'NOT Found 带宽包', data_format)

        # 存储类
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 19, ECSNUM + 19), '存储类', category_merge_format)
        # 写入云硬盘
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 20, ECSNUM + 20), '云硬盘信息', merge_format)
        worksheet.set_column('A:F', 30)
        worksheet.set_row(0, 25)
        cbs = FormatData.format_cbs(region)
        if cbs != None:
            worksheet.write_row('A{}'.format(ECSNUM + 21), DSKTitle, Title_format)
            for cb in cbs:
                worksheet.write_row('A' + str(ECSNUM + 22), cb, data_format)
                ECSNUM += 1
        else:
            worksheet.merge_range('A{}:F{}'.format(ECSNUM + 21, ECSNUM + 21), 'NOT Found 带宽包', data_format)
            ECSNUM -= 1

        # 数据库类
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 23, ECSNUM + 23), '数据库类', category_merge_format)
        # 写入 MySQL
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 24, ECSNUM + 24), 'MySQL信息', merge_format)
        worksheet.set_column('A:F', 30)
        worksheet.set_row(0, 25)
        mysqls = FormatData.format_mysql(region)
        if mysqls != None:
            worksheet.write_row('A{}'.format(ECSNUM + 25), MSQTitle, Title_format)
            for mysql in mysqls:
                worksheet.write_row('A' + str(ECSNUM + 26), mysql, data_format)
                ECSNUM += 1
            ECSNUM -= 1
        else:
            worksheet.merge_range('A{}:F{}'.format(ECSNUM + 25, ECSNUM + 25), 'NOT Found MySQL', data_format)
            ECSNUM -= 1

        # 写入 SQLServer
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 27, ECSNUM + 27), 'SQL Server信息', merge_format)
        worksheet.set_column('A:F', 30)
        worksheet.set_row(0, 25)
        sqls = FormatData.format_sqlserver(region)
        if sqls != None:
            worksheet.write_row('A{}'.format(ECSNUM + 28), SQSTitle, Title_format)
            for sql in sqls:
                worksheet.write_row('A' + str(ECSNUM + 29), sql, data_format)
                ECSNUM += 1
            ECSNUM -= 1
        else:
            worksheet.merge_range('A{}:F{}'.format(ECSNUM + 28, ECSNUM + 28), 'NOT Found SQL Server', data_format)
            ECSNUM -= 1

        # 写入 Redis
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 30, ECSNUM + 30), 'Redis信息', merge_format)
        worksheet.set_column('A:F', 30)
        worksheet.set_row(0, 25)
        rediss = FormatData.format_redis(region)
        if rediss != None:
            worksheet.write_row('A{}'.format(ECSNUM + 31), RESTitle, Title_format)
            for redis in rediss:
                worksheet.write_row('A' + str(ECSNUM + 32), redis, data_format)
                ECSNUM += 1
            ECSNUM -= 1
        else:
            worksheet.merge_range('A{}:F{}'.format(ECSNUM + 31, ECSNUM + 31), 'NOT Found Redis', data_format)
            ECSNUM -= 1

        # 写入 Mariadb
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 33, ECSNUM + 33), 'Mariadb信息', merge_format)
        worksheet.set_column('A:F', 30)
        worksheet.set_row(0, 25)
        mariadbs = FormatData.format_mariadb(region)
        if mariadbs != None:
            worksheet.write_row('A{}'.format(ECSNUM + 34), MRDTitle, Title_format)
            for mariadb in mariadbs:
                worksheet.write_row('A' + str(ECSNUM + 35), mariadb, data_format)
                ECSNUM += 1
            ECSNUM -= 1
        else:
            worksheet.merge_range('A{}:F{}'.format(ECSNUM + 34, ECSNUM + 34), 'NOT Found Mariadb', data_format)
            ECSNUM -= 1

        # 写入 PostGreSQL
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 36, ECSNUM + 36), 'PostgreSQL信息', merge_format)
        worksheet.set_column('A:F', 30)
        worksheet.set_row(0, 25)
        postgres = FormatData.format_postgres(region)
        if postgres != None:
            worksheet.write_row('A{}'.format(ECSNUM + 37), PGSTitle, Title_format)
            for postgre in postgres:
                worksheet.write_row('A' + str(ECSNUM + 38), postgre, data_format)
                ECSNUM += 1
            ECSNUM -= 1
        else:
            worksheet.merge_range('A{}:F{}'.format(ECSNUM + 37, ECSNUM + 37), 'NOT Found PostgreSQL', data_format)

        # 安全类
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 39, ECSNUM + 39), '安全类', category_merge_format)
        # 写入 云镜
        worksheet.merge_range('A{}:F{}'.format(ECSNUM + 40, ECSNUM + 40), '云镜信息', merge_format)
        worksheet.set_column('A:F', 30)
        worksheet.set_row(0, 25)
        yunjing = FormatData.format_yunjing(region)
        if yunjing != None:
            worksheet.write_row('A{}'.format(ECSNUM + 41), YUJTitle, Title_format)
            worksheet.write_row('A' + str(ECSNUM + 42), yunjing, data_format)
        else:
            worksheet.merge_range('A{}:F{}'.format(ECSNUM + 41, ECSNUM + 41), 'NOT Found 云镜', data_format)
            ECSNUM -= 1

    workbook.close()
if __name__ == '__main__':
    main()