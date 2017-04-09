#-*- coding:utf-8 -*-
from wechatpy.enterprise import WeChatClient
client = WeChatClient('wx2acb527aecbe406e','iCCSBYDiSSz2i8ICou_VyQqziPxd3TFdXVzxW_QhBFjg8JGFHDew_idzNnT2fPu3')
#client.message.send_text(12,'xzxhg','内容')
#print('汉字')
#dept = client.department.get('1')
#print(dept)
_file=open('/tmp/wechatpyutil.py','rb')
_s=client.media.upload('file',_file)
print(_s)
