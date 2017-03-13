#!/usr/bin/env python
#coding=utf-8

# import requests,re,json,html2text,sys,time
import requests
from bs4 import BeautifulSoup
import urllib

url="https://www.douban.com/group/haixiuzu"

def getTopicList():
    for x in range(10,20):
        print x
        page = x * 25
        get_url = requests.get(url+"discussion?start="+str(page))
        # print get_url.text
        soup = BeautifulSoup(get_url.text,"html.parser")
        tdlist = soup.find_all("td",class_="title")
        print tdlist

if __name__ == '__main__':
    getTopicList()
