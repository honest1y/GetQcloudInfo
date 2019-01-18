## GetQcloudInfo
### Export resources
- CVM
- CLB
- VPC
- EIP
- VPNGateway
- DirectConnectGateway
- BindWidthPackages
- CBS
- CDB For MySQL
- CDB For SQL Server
- CDB For Redis
- CDB For Maroadb
- CDB For PostgreSQL
- YunJing
- CWS

### Known Problems
- Not set Offset and Limit,That means if the number of CVMs and CDBs exceeds 100, they cannot be exported properly.

### Preview

![img](https://www.cloudcared.cn/wp-content/uploads/2019/01/img1.png)
![img](https://www.cloudcared.cn/wp-content/uploads/2019/01/img2.png)
![img](https://www.cloudcared.cn/wp-content/uploads/2019/01/img3.png)

### How to Use

- 1、pip3 install -r requirements.txt
- 2、Fill in your cloud `SecretId`、`SecretKey`、`FilePath` in `config.txt`
- 3、python3 run.py
