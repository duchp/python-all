# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:10:27 2019

@author: 杜琛萍
"""

import jieba.analyse
from os import path
from scipy.misc import imread
import matplotlib as mpl 
from wordcloud import WordCloud

def ciyun(file):

    mpl.rcParams['font.sans-serif'] = ['FangSong']

    content = open(file,"rb").read()

    # tags extraction based on TF-IDF algorithm
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=False)
    text =" ".join(tags)
    text = str(text)
    # read the mask
    d = path.dirname(__file__)
    trump_coloring = imread(path.join(d, "bears.jpg"))

    wc = WordCloud(font_path='simsun.ttc',width = 500, height = 500 ,
            background_color="white", max_words=300, mask=trump_coloring,
            max_font_size=40, random_state=42)
    # generate word cloud 
    wc.generate(text)
    return wc

def main():
#    content = ciyun('中文评论条.txt')
    content = ciyun('content.txt')
    content.to_file('评论词云图.png')
#    hotcontent = ciyun('中文热评条.txt')
    hotcontent = ciyun('hotcontent.txt')
    hotcontent.to_file('热评词云图.png')

if __name__ == '__main__':
    main()
