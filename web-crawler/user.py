# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:01:53 2019

@author: 杜琛萍
"""
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import xlwt

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
    city = soup.find('div', 'inf s-fc3')
    if(city != None):
        city = city.get_text().replace('所在地区：','')
    year = soup.find('div','sep')
    gender = soup.find('i','icn')
    if(gender != None):
        gender = re.sub("\D", "", str(gender))
    if(year != None):
        year = year.get_text().replace('年龄：','')
    return city,year,gender

def write(city,year,gender,idd,num):    
    worksheet.write(num, 0, str(idd))
    worksheet.write(num, 1, city)
    worksheet.write(num, 2, gender)
    worksheet.write(num, 3, year)

     
def main():
    num = 1
    for line in open('noncopy_id.txt','r'):
        idd = line
        url = "https://music.163.com/#/user/home?id=" + str(idd)
        html = get_html_src(url)
        city,year,gender = parse_html_page(html)
        write(city,year,gender,idd,num)
        num += 1
        
if __name__ == '__main__':
   # 创建excel工作表
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    # 设置表头
    worksheet.write(0, 0, label='ID')
    worksheet.write(0, 1, label='省份城市')
    worksheet.write(0, 2, label='性别')
    worksheet.write(0, 3, label='年龄')
    main()    
    workbook.save('OK.xls')