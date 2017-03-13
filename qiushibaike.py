#!/usr/bin/env python
#coding=utf-8

import requests,re,json,html2text,sys,time
from bs4 import BeautifulSoup
import urllib

url="http://www.qiushibake.com/imgrank/pake/"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Aget' : user_agent}

def getTopicContext():
    for x in range(1,30):
        page = x
        get_url = requests.get(url+str(x),headers=headers)
        soup = BeautifulSoup(get_url.text,"html.parser")
        topicDiv = soup.find_all("div",class_='content')
        for div in topicDiv:
            if len(div.contents) > 1:
                img = div.img
                saveImage(img.get("src"))

def saveImage(imgUrl):
    fileName = imgUrl[imgUrl.rfind("/")+1:]
    path = r"/home/kennys/qiushibaike/"+fileName
    urllib.urlretrieve(imgUrl,path)

if __name__ == '__main__':
    getTopicContext()
