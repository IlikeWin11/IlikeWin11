#-*-coding:GBK-*-
import os

# ���庯��
def getOSName():
    '''
    ����:��ȡϵͳƽ̨
    �����Windowsϵͳ������1
    ��Linux,UNIX��Mac OS������2
    �޷���ѯ����0
    '''
    names = os.name
    if names == "nt":
        return 1
    elif names == "posix":
        return 2
    else:
        return 0

# ��ʼ���ú���
namer = getOSName()
if namer == 1:
    print("��Windowsϵͳ")
elif namer == 2:
    print("��Linux,UNIX��Mac OSϵͳ")
else:
    print("�޷���ѯ")
