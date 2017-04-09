#-*- coding:utf-8 -1 -8-*-
import base64 , binascii ,json,requests


def proxy(**kwargs) :
	p_url = 'http://120.27.41.142:3128'
	s = requests.post(p_url,**kwargs)
	return s

def proxy_request(**kwargs) :
	p_url = 'http://120.27.41.142:3128/weixinproxyrequest/'
	s = requests.post(p_url,**kwargs)
	return s

def proxy_media_upload(**kwargs) :
	p_url = 'http://120.27.41.142:3128/weixinproxymediaupload/'
	s = requests.post(p_url,**kwargs)
	return s


def message_send_text(touser,toparty,totag,agentid,scontent) :
	data = {
		'url':'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=ACCESS_TOKEN&debug=1',
		'request_type':'POST',
		'body':{
			'touser': touser,
			'toparty': toparty,
			'totag':totag,
			'msgtype':'text',
			'agentid':agentid,
			'text': {
				'content': scontent
			},
			'safe':'0'
		}
	}
	body = json.dumps(data,ensure_ascii=False)
	return proxy_request(files={'data':body})

def message_send_media(touser,toparty,totag,agentid,media_id) :
	data = {
		'url':'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=ACCESS_TOKEN',
		'request_type':'POST',
		'body':{
			'touser': touser,
			'toparty': toparty,
			'totag':totag,
			'msgtype':'file',
			'agentid':agentid,
			'file': {
				'media_id': media_id
			},
			'safe':'0'
		}
	}
	body = json.dumps(data,ensure_ascii=False)
	return proxy_request(files={'data':body})


def media_upload(filename) :
	data = {
		'url':'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE',
		'request_type':'POST',
		'body':{
			'type':'file'
		}
	}
	body = json.dumps(data,ensure_ascii=False)
	files={
		'media':(filename,open(filename),'rb'),
		'data':body
	}
	#files = json.dumps(files,ensure_ascii=False)
	#print(files)
	result = proxy_media_upload(files=files)
	print('debug:',result.text)
	result_json = json.loads(result.text)
	if 'media_id' in result_json:
		media_id = result_json['media_id']
		return media_id
	#return proxy_wechat(params=body,files=files)

def url_media_upload(url) :
	data = {
		'url':'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE',
		'request_type':'POST',
		'body':{
			'type':'file'
		}
	}
	body = json.dumps(data,ensure_ascii=False)
	import requests
	files={
		'media':(url,requests.get(url,stream=True).raw,'rb'),
		'data':body
	}
	#files = json.dumps(files,ensure_ascii=False)
	#print(files)
	result = proxy_media_upload(files=files)
	print('debug:',result.text)
	result_json = json.loads(result.text)
	if 'media_id' in result_json:
		media_id = result_json['media_id']
		return media_id
	#return proxy_wechat(params=body,files=files)



def url_media_upload_message_send(toname,totag,toparty,agentid,url):
	media_id=url_media_upload(url)
	r2=message_send_media(toname,totag,toparty,agentid,media_id)
	print(r2.text)

def media_upload_message_send(toname,totag,toparty,agentid,filename):
	media_id=media_upload(filename)
	r2=message_send_media(toname,totag,toparty,agentid,media_id)
	print(r2.text)

#message_send_upload('xzxhg','','',12,'test.html')
