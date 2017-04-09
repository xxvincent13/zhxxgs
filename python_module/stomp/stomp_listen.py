import time
import sys
import stomp
import json
class MyListener(object):
    def on_error(self, headers, message):
        print('received an error %s' % message)
    def on_message(self, headers, message):
        sys.path.append('../')
        import weixin.wechat as wechat
        print('received a message ')
        print(message)
        json_message = json.loads(message)
        if(json_message['msgtype']=='news'):
            wechat.message_send(message)
            print('news')
        elif(json_message['msgtype']=='text'):
        #    from wechatpy.enterprise import WeChatClient
         #   client = WeChatClient('wx2acb527aecbe406e','iCCSBYDiSSz2i8ICou_VyQqziPxd3TFdXVzxW_QhBFjg8JGFHDew_idzNnT2fPu3')
          #  client.message.send_text(json_message['agentid'],json_message['touser'],json_message['text']['content'],'',json_message['totag'])
           # print('text')
            wechat.message_send(message)
        elif(json_message['msgtype']=='sms'):
            #通过短信网关发送短信
            import sms.sms as sms
            ret = sms.sendsms(json_message['touser'],json_message['text']['content'])
            print(ret)
            print('sms')
            #向queue_in队列返回短信回复
            import stomp.stomp_send as stomp_send
            send_queue_in(ret)

#官方示例的连接代码也落后了，现在分协议版本
print('start stomp listen ......')
try:
    while True:
        conn = stomp.Connection10([('120.27.41.142',61613)])  
        conn.set_listener('', MyListener())
        conn.start()
        conn.connect(wait=True)
        conn.subscribe(destination='/queue/queue_out',ack='auto')
        conn.disconnect()
except:
    pass
