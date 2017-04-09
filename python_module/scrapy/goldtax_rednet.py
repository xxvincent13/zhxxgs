import re,requests
from bs4 import BeautifulSoup as bs

def getTags(keywords):
	Cookies = {
		'wdcid':'31b990fe69cb7189',
		'Hm_lvt_aaecf8414f59c3fb0127932014cf53c7':'1489833509',
		'wdlast':'1489833750',
		'Hm_lpvt_aaecf8414f59c3fb0127932014cf53c7':'1489833750',
		'yundun_captcha_marker':'d1adec1f-055c-40a7-b299-76abccbda65c',
		'yundun_captcha_marker2':'c30b143c9d71a3e1f5bbafcd742fabc7',
		'yd_clearance':'e47ed62ebbcf18eba0b964a095373bda9e4fa8bb72d15b2f-1489919925-86400',
		'PHPSESSID':'beo0tj8ocrfhub432268psp9v3'
	}

	headers={
		'Host':'s.rednet.cn',
		'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:35.0) Gecko/20100101 Firefox/35.0',
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
		'Accept-Encoding':'gzip, deflate',
		'Referer':'http://s.rednet.cn/?scope=8&q=%E7%A8%8E&orderby=1&date_range=4',
		'Connection':'keep-alive'
	}
	s = requests.Session()
	r = s.get('http://s.rednet.cn/?scope=7&q='+keywords+'&orderby=1&date_range=4',headers=headers,cookies=Cookies)
	soup = bs(r.text,'lxml')
	print(r.content.decode('utf-8'))
	l = soup.find_all(class_='module')
	for tag in l:
		print(tag)

getTags('国税')
