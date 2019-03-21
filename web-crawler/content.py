# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 11:48:04 2019

@author: 杜琛萍
"""
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import json
import random
import sys
import importlib

def get_html_src(url):
# 可以任意选择浏览器,前提是要配置好相关环境
    driver = webdriver.Chrome()
    driver.get(url)
# 切换成frame
    driver.switch_to_frame("g_iframe")
# 休眠3秒,等待加载完成!
    time.sleep(3)
    page_src = driver.page_source
    driver.close()
    return page_src

def parse_html_page(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('span', 'txt')
    return items

def song_id(items):
    songid = []
    for item in items:
#        print('歌曲id:', item.a['href'].replace('/song?id=', ''))
#        song_name = item.b['title']
#        print('歌曲名字:', song_name)
        songid.append(str(item.a['href'].replace('/song?id=', '')))
    return songid

def get_response(offset,limit,muid):
    #参数
    para = {
        'offset':offset,#页数
        'limit':limit#总数限制
    }
    # 歌曲id
    musicid = muid  # 
    #歌曲api地址
    musicurl = "http://music.163.com/api/v1/resource/comments/R_SO_4_"+musicid+"?"+urlencode(para)
    #头结构
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':'vjuids=-13ac1c39b.1620457fd8f.0.074295280a4d9; vjlast=1520491298.1520491298.30; _ntes_nnid=3b6a8927fa622b80507863f45a3ace05,1520491298273; _ntes_nuid=3b6a8927fa622b80507863f45a3ace05; vinfo_n_f_l_n3=054cb7c136982ebc.1.0.1520491298299.0.1520491319539; __utma=94650624.1983697143.1521098920.1521794858.1522041716.3; __utmz=94650624.1521794858.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; JSESSIONID-WYYY=FYtmJTTpVwmbihVrUad6u76CKxuzXZnfYyPZfK9bi%5CarU936rIdoIiVU50pfQ6JwjGgBvSyZO0%2FR%2BcoboKdPuMztgHCJwzyIgx1ON4v%2BJ2mOvARluNGpRo6lmhA%5CfcfCd3EwdS88sPgxpiiXN%5C6HZZEMQdNRSaHJlcN%5CXY657Faklqdh%3A1522053962445; _iuqxldmzr_=32',
        'Host':'music.163.com',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
    }
    #代理IP
    proxies= {
        'http:':'http://121.232.146.184',
        'https:':'https://144.255.48.197',
        'https:':'https://94.240.33.242:3128',
        'http:':'http://221.4.150.7:8181',
        'https:' : 'https://123.163.117.246:33915',
        'https:' : 'https://180.125.17.139:49562',
        'https:' : 'https://117.91.246.244:36838',
        'https:' : 'https://121.227.24.195:40862',
        'https:' : 'https://180.116.55.146:37993',
        'https:' : 'https://117.90.7.57:28613',
        'https:' : 'https://193.112.111.90:51933',
        'https:' : 'https://61.130.236.216:58127',
        'https:' : 'https://60.189.203.144:16820',
        'https:' : 'https://111.177.185.148:9999',
        'http:' : 'http://140.207.50.246:51426'
        
    }
    try:
        #用post方式接收数据
        response = requests.post(musicurl,headers=headers,proxies=proxies)
        if response.status_code == 200:
            return response.content
    except RequestException:
        print("访问出错")

def parse_return(html):
    data = json.loads(html)#将返回的值格式化为json
    hotct = []
    ct = []
    if data.get('hotComments'):
        hotcomm = data['hotComments']
        for hotitem in hotcomm:
            hotct.append(hotitem['content'])
    if data.get('comments'):
        comm = data['comments']
        for item in comm:
            ct.append(item['content'].replace('\r', ' '))
            idd.write(str(item['user']['userId'])+'\n')
    return hotct,ct
        
def all_song():
    url = "https://music.163.com/artist?id=" + str(7763)
    html = get_html_src(url)
    items = parse_html_page(html)
    muidtol = song_id(items) 
    return(muidtol)     

def main(offset,muid):
       html = get_response(offset,200,muid)
       hotct,ct = parse_return(html)
       hotcontent.write(str(hotct))   
       content.write(str(ct))

    
if __name__ == '__main__':
    importlib.reload(sys)
    muidtol = all_song()
    songid = open('songid.txt','w')
    songid.write('\n'.join(muidtol))
    songid.close()
    idd = open('idd.txt','w')
    hotcontent = open('hotcontent.txt','w',encoding='utf-8')
    content = open('content.txt','w',encoding='utf-8')
    for muid in muidtol:
        for x in range(0,10): 
            time.sleep(random.random() * 0)  
            main(x,muid)
    hotcontent.close()
    content.close()
    idd.close()

    