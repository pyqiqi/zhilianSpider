#coding=utf-

import urllib2
import random
import time
from bs4 import BeautifulSoup
import socket


#verilog','python','java','javascript',['c++','php','c#','html','objective-c']
#language_list = ['verilog','perl','ruby','python','java','javascript','php','lisp','html','objective-c','vb','c++','c#']

language_list = ['c#']

#url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%B7%B1%E5%9C%B3&kw=PYTHON%20&sm=0&p=3"
#url = "http://sou.zhaopin.com/jobs/searchresult.ashx?in=210500%3b160400%3b300100%3b160100&jl=%E6%B7%B1%E5%9C%B3&kw=python&isadv=0&sg=3bee56b33a1941fea5918872ef2af808&p="
USER_AGENTS = [
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
	"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
	"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
	"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
								        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
def get_content(url,USER_AGENTS):
	random_agent = random.choice(USER_AGENTS)
	req = urllib2.Request(url)
	req.add_header("User-Agent",random_agent)
	req.add_header("Host","sou.zhaopin.com")
#	req.add_header("Referer","http://blog.csdn.net/")
	req.add_header("GET",url)
	try:
		con = urllib2.urlopen(req,timeout = 20)
		content = con.read()
		return content
	except Exception,e:
		return ''
		print 'error:',str(e)


for language in language_list:
	i = 0
	p = 1
	fl=open('/root/zhilian/language/'+language+'.txt', 'w')


	url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?in=210500%3B160400&jl=%E6%B7%B1%E5%9C%B3&kw='+language+'&p='+str(p)+'&isadv=0'
	cont =  get_content(url,USER_AGENTS)
	if (cont == ''):
		print 'error 1'
		continue
	soup = BeautifulSoup(cont)
	lis = soup.findAll("li",{"class":"newlist_deatil_two"})
	while(len(lis) != 0):
		for li in lis:
#			fl.write(str(li)+'\n')
#			print "debug:",language
			spans = li.findAll("span")
			for span in spans:
				fl.write(str(span)[6:-7]+'|')
				i = i + 1
			fl.write('\n')
#time.sleep(1)
		p = p + 1
		print 'language:',language,'page:',p,'count:',i
		url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?in=210500%3B160400&jl=%E6%B7%B1%E5%9C%B3&kw='+language+'&p='+str(p)+'&isadv=0'
		cont =  get_content(url,USER_AGENTS)
		if (cont == ''):
			print 'error 2'
			continue
		soup = BeautifulSoup(cont)
		lis = soup.findAll("li",{"class":"newlist_deatil_two"})
	print 'language:',language,'page:',p,'count:',i
	fl.close()


#if (len(lis) == 0):
#	print 'null'

#for li in lis:
#	print li


#print '我'
