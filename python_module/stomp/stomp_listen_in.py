import time
import sys
import stomp
import json
import xml.etree.cElementTree as ET
class MyListener(object):
    def on_error(self, headers, message):
        print('received an error %s' % message)
    def on_message(self, headers, message):
        print('received a message ')
        print(message)
        xml_tree = ET.fromstring(message)
        content = xml_tree.find('Content').text
        touser = xml_tree.find('FromUserName').text
        agentid = xml_tree.find('AgentID').text
        print(touser,agentid,content)
        sys.path.append('/srv/python_module/weixin')
        import wechat
        wechat.message_send_text(touser,'','',int(agentid),'autoreplay:'+content)
#官方示例的连接代码也落后了，现在分协议版本
try:
    while True:
        conn = stomp.Connection10([('120.27.41.142',61613)])  
        conn.set_listener('', MyListener())
        conn.start()
        conn.connect()
        conn.subscribe(destination='/queue/queue_in', id=1, ack='auto')
        conn.disconnect()
except:
    pass
