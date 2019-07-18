# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:36:41 2019

@author: lenovo
"""

import cv2
import numpy as np

def median(img,start_x,start_y,w,h):#指定范围内求中位数的函数
    s = []
    for i in range(start_x,start_x+w):
        for j in range(start_y,start_y+h):
            s.append(img[i][j])
    s.sort()
    if len(s)%2 == 0:
        med = (s[len(s)/2]+s[len(s)/2-1])/2
    else:
        med = s[int((len(s)+1)/2)-1]
    return med
    

def medianBlur(img, kernel, padding_size, padding_way):
#  img & kernel is List of List; padding_way a string
#  Please finish your code under this blank
    top, bottom, left, right = padding_size
    w, h = kernel
    if padding_way == 'REPLICA':
        replicate = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REPLICATE)
    else:
        replicate = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=0)
    W,H = replicate.shape
    #print(W,H)
    median_img = np.zeros((W-w,H-h))
    for i in range(0,W-w):
        for j in range(0,H-h):
            median_img[i][j]=median(replicate,i,j,w,h)
    return median_img

if __name__ == "__main__":
    img = cv2.imread('cat.jpg',0)
    #print(img.shape)
    kernel = (7,3)
    padding_size = (3,3,3,3)
    med_zero_img = medianBlur(img,kernel,padding_size,padding_way = 'ZEROS')
    med_replica_img = medianBlur(img,kernel,padding_size,padding_way = 'REPLICA')
    #print(med_zero_img.shape)
    #print(med_replica_img.shape)
    cv2.imwrite("med_zero_cat.png", med_zero_img)
    cv2.imwrite("med_replica_cat.png", med_replica_img)
    cv2.imwrite("med_cat_start.png", img)
