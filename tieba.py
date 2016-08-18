#coding:utf-8
import requests
import re
import os

class BDTB:

    def __init__(self,baseUrl,seeLZ):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz'+str(seeLZ)
    #哈哈哈
    def getPage(self,pageNum):
        try:
            url = self.baseUrl+self.seeLZ+"&pn="+str(pageNum)
            response = requests.get(url)
            # print response.text
            return response.text
        except requests.HTTPError, e:
            print e
            return None
    def getTitle(self):
        #获取标题
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt pull-left text-overflow.*?>(.*?)</h3>',re.S)
        result = re.search(pattern,page)
        # print result.group(1).strip()
        # print page
        if result:
            return result.group(1).strip()
        else:
            return None
    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?<span class="red">(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None
    def getContent(self,pageNum):
        page = self.getPage()


baseUrl = 'http://tieba.baidu.com/p/3842009384'
bdtb = BDTB(baseUrl,1)
page = bdtb.getPageNum()
print page
