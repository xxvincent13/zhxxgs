from bs4 import BeautifulSoup as bs
import requests,urllib,re

def getTags(keywords):
	URL = 'http://www.07430743.com/search.php?mod=forum'
	UA = "Mozilla/5.0 (Windows NT 6.1; rv:51.0) Gecko/20100101 Firefox/51.0"
	header = { "User-Agent" : UA,"Referer": "http://www.07430743.com/","Content-Type": "application/x-www-form-urlencoded"}
	s = requests.Session()
	r = s.get(URL,headers=header)

	soup = bs(r.text,'lxml')
	formhash = soup.find(attrs={'name':'formhash'})['value']

	postData = { 'formhash': formhash,'srchtxt': keywords.encode('gbk'),'searchsubmit': 'yes'}
	r = s.post(URL,data=postData,headers=header,allow_redirects=False)
	location = r.headers['Location']
	searchid =   re.search(r'(?<=searchid=)\d+',location).group(0)
	URL='http://www.07430743.com/search.php?mod=forum&searchid='+searchid+'&orderby=lastpost&ascdesc=desc&searchsubmit=yes&kw='+keywords
	print(URL)
	r = s.get(URL,headers=header)

	soup = bs(r.text,'lxml')
	#print(soup)
	try:
		l = soup.find_all(id='threadlist')[0].find_all('li')
		for a in l:
			print(a.text)
			print(a['id'])
	except:
		print()

getTags('税')
