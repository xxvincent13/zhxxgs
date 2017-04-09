import time
import sys
import stomp
import json

#向out队列发消息
def send_queue_out(data):
	conn = stomp.Connection10([('120.27.41.142',61613)])  
	conn.start()
	conn.connect()
	conn.send(body=data, destination='/queue/queue_out')
	conn.disconnect()	

#向out队列发消息——微信
def send_queue_out_weixin(touser,content,agentid):
	data ={
	 	'touser': touser,
	  	'toparty': '',
	  	'totag':'',
	  	'msgtype':'text',
	  	'agentid':agentid,
	  	'text': {
		    'content': content
	 	 },
	  	'safe':'0'
		}
	data = json.dumps(data,ensure_ascii=False)
	send_queue_out(data)

#向out队列发消息——短信
def send_queue_out_sms(touser,content):
	data ={
	 	'touser': touser,
	  	'toparty': '',
	  	'totag':'',
	  	'msgtype':'sms',
	  	'agentid':12,
	  	'text': {
		    'content': content
	 	 },
	  	'safe':'0'
		}
	data = json.dumps(data,ensure_ascii=False)
	send_queue_out(data)

#向in队列发消息
def send_queue_in(data):
	conn = stomp.Connection10([('120.27.41.142',61613)])  
	conn.start()
	conn.connect()
	conn.send(body=data, destination='/queue/queue_in')
	conn.disconnect()


#send_queue_out_sms('13508432413','机房停电，请及时重启设备！')
#send_queue_in('测试：机房停电，请及时重启设备！456')
