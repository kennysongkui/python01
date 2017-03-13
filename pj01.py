#!/usr/bin/evn python
#coding=utf-8

import urllib2
import urllib

# url="http://www.baidu.net"

url="https://www.douban.com/group/haixiuzu/"

# response = urllib.urlopen(url)
# print response.read()
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.read()

urllib2.urlopen()
