import requests
import re
import os
import sys

url = "http://www.qiushibaike.com/imgrank/page/1/"

user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
k = 1;
for i in range(1,35+1):
    try:
        url = re.sub('page/\d+',"page/%d"%i,url,re.S)
        # print url
        html = requests.get(url,headers = headers)
        #print html.text
        text1 = html.text
        text2 = re.findall('class="article block untagged mb15"(.*?)<div class="stats">',text1,re.S)

        for j in text2:
            text3 = re.findall('<div class="thumb">(.*?)</div>',j,re.S)
            # print text3
            text4 = re.findall('<img src=\"(.*?)\"',text3[0],re.S)
            # print text4[0]
            pic = requests.get(text4[0], stream=True)
            if not os.path.exists('e:/spider_file/qiubai_image/'):
                os.makedirs('e:/spider_file/qiubai_image/')
                print "create director"
            fp = open('e:/spider_file/qiubai_image/'+str(k)+'.jpg',"wb")
            for chunk in pic.iter_content(chunk_size=1024):
                if chunk:
                    fp.write(chunk)
                    fp.flush()
            fp.close()
            print k
            k = k + 1

    except requests.HTTPError as e:
        print e
        pass
    except:
        pass