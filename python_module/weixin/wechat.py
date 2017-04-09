#-*- coding:utf-8 -1 -8-*-
# import 这边需要注意的是只有一个rsa这个模块是需要install的，其他的都是内置
import base64,binascii,rsa,json,simplejson,requests

def get_token(sid,ssecrect):
	url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='+sid+'&corpsecret='+ssecrect
	result = json.loads(requests.get(url).text)
	if 'access_token' in result:
		stokenn  = result['access_token']
		return stokenn

def ACCESS_TOKEN():
	return get_token('wx2acb527aecbe406e','iCCSBYDiSSz2i8ICou_VyQqziPxd3TFdXVzxW_QhBFjg8JGFHDew_idzNnT2fPu3')

def message_send(body) :
	p_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=ACCESS_TOKEN&debug=1'
	p_url = p_url.replace('ACCESS_TOKEN',ACCESS_TOKEN())
	body = body.encode('utf-8').decode('iso-8859-1')
	s = requests.post(p_url,data=body)
	print(s.text)
	return s

def  chat_create():
	url='https://qyapi.weixin.qq.com/cgi-bin/chat/create?access_token=ACCESS_TOKEN'
	body={
	"chatid":"12",
	"name":"企业应用中心测试",
	"owner":"xzxhg",
	"userlist":["xzxhg","xzgb1","xzxgb"]
	}
	s = requests.post(url.replace('ACCESS_TOKEN',ACCESS_TOKEN()),data=json.dumps(body,ensure_ascii=False).encode('utf-8').decode('iso-8859-1'))
	print(s.text)
	return s

def message_send_media(touser,toparty,totag,agentid,media_id) :
	data={
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
	body = json.dumps(data,ensure_ascii=False)
	return message_send(body)	
	
def message_send_text(touser,toparty,totag,agentid,scontent) :
	data ={
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
	body = json.dumps(data,ensure_ascii=False)
	return message_send(body)


def test_message_send_text():
	message_send_text('xzxhg','','',12,'这是一个测试测试!')

def media_upload(filename):
	url='https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE'
	files={
		'media':(open(filename,'rb'))
	}
	body={
		'type':'file'
	}
	url = url.replace('ACCESS_TOKEN',ACCESS_TOKEN())
	url = url.replace('TYPE','file')
	s=requests.post(url,files=files,data=body)
	print(s.text)
	return s

def media_upload_message_send(toname,totag,toparty,agentid,filename):
	r = media_upload(filename)
	print(r.text)
	r_json = json.loads(r.text)
	if 'media_id' in r_json:
		media_id = r_json['media_id']
		r2=message_send_media(toname,totag,toparty,agentid,media_id)
	else:
		pass
#media_upload()
#测试方法
#test_send_wechat()
#chat_create()
