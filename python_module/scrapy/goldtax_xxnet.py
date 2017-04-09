import re,requests
from bs4 import BeautifulSoup as bs

def getTags(keywords):
	r = requests.get('http://search.xxnet.com.cn/search.php?q='+keywords+'&f=_all&s=PublishDate_DESC')
	soup = bs(r.content.decode('utf-8'),'lxml')
	l = soup.find_all(class_='res-doc')
	for tag in l:
		#tag_a = tag.find('a')
		#print(tag_a.attrs['href'],tag_a.text)
		print(tag.text)

getTags('税')
