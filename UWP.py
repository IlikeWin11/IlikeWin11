#-*-coding:GBK-*-
import os

# 定义函数
def getOSName():
    '''
    功能:获取系统平台
    如果是Windows系统，返回1
    是Linux,UNIX或Mac OS，返回2
    无法查询返回0
    '''
    names = os.name
    if names == "nt":
        return 1
    elif names == "posix":
        return 2
    else:
        return 0

# 开始引用函数
namer = getOSName()
if namer == 1:
    print("是Windows系统")
elif namer == 2:
    print("是Linux,UNIX或Mac OS系统")
else:
    print("无法查询")
