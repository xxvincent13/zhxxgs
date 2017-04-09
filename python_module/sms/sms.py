import requests
uid = 'hnxzgs-xxzx'
pwd = 'e378c2e84341366774459db17ca9fc70'
def sendsms(mobile,content):
	url='http://api.sms.cn/mtutf8/'
	para={
		'uid': uid,
		'pwd': pwd,
		'mobile': mobile,
		'content': '【州国税局】'+content
	}
	s=requests.post(url,data=para)
	s.encoding='utf-8'
	return s.text
#print(sendsms('13508432413,18074350013','因昨天电力跳闸，纳税服务视频监控服务器down机，请重启。'))
