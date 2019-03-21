# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 19:00:12 2019

@author: 杜琛萍
"""

import re
import sys
import importlib
importlib.reload(sys)

#对评论文件提取中文预处理
def translate(str):

    p = re.compile(u'[\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5
    res = re.findall(p, str)
    outStr = ''.join(res)
    return outStr

#对用户id文件去重预处理
def non_copy():
    lines_seen = set() 
    outfile=open('noncopy_id.txt',"w") 
    f = open('idd.txt','r')
    for line in f: 
      if line not in lines_seen: 
        outfile.write(line) 
        lines_seen.add(line) 
    outfile.close() 
    print("success")

def main():
    #打开原始爬取文件
    file = open('content.txt','r', encoding='UTF-8')
    hotfile = open('hotcontent.txt','r', encoding='UTF-8')
    #创建新文件
    files = open('中文评论条.txt','w', encoding='UTF-8')
    filess = open('中文热评条.txt','w', encoding='UTF-8')
    #读取文件内容
    content = file.read()
    hotcontent = hotfile.read()
    #提取文件中文内容，并写入新文件
    abc = translate(content)
    files.write(abc)
    hotabc = translate(hotcontent)
    filess.write(hotabc)
    #关闭文件
    file.close()
    hotfile.close()
    files.close()
    filess.close()
    #处理用户id文件
    non_copy()
    
if __name__ == '__main__':
    main()