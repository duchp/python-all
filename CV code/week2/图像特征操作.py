# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 21:20:32 2019

@author: lenovo
"""

import cv2
import numpy as np

#img show

img = cv2.imread('cat.jpg')
cv2.imshow('cat', img)
print(img.shape)


# Gaussian Kernel Effect

g_img = cv2.GaussianBlur(img,(7,7),5)
#(7, 7)表示高斯矩阵的长与宽都是7，标准差取5
cv2.imshow('gaussian_blur_cat1', g_img)
g_img = cv2.GaussianBlur(img,(17,17),5)
# 图像变更模糊，因为范围更大，平均效果更明显
cv2.imshow('gaussian_blur_cat2', g_img)
g_img = cv2.GaussianBlur(img,(7,7),1)
# 图像更清晰，因为方差更小，高斯图像更尖锐，中心点起的作用更大
cv2.imshow('gaussian_blur_cat3', g_img)

# 来看看高斯核
kernel = cv2.getGaussianKernel(7, 5)
print(kernel)
# 为啥一维，因为一维运算快
# 理论解释
# 用显式地代码看隐式地高斯和显示地分步高斯地效果
g1_img = cv2.GaussianBlur(img,(7,7),5)
g2_img = cv2.sepFilter2D(img, -1, kernel, kernel) # ori, depth, kernelX, kernelY
#sepFilter2D() 用分解的核函数对图像做卷积。首先，图像的每一行与一维的核kernelX做卷积；然后，运算结果的每一列与一维的核kernelY做卷积
cv2.imshow('g1_blur_cat', g1_img)
cv2.imshow('g2_blur_cat', g2_img)

######## Other Applications #########
# 2nd derivative: laplacian （双边缘效果）
kernel_lap = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], np.float32)
lap_img = cv2.filter2D(img, -1, kernel=kernel_lap)
cv2.imshow('lap_cat', lap_img)

# 应用： 图像锐化 = edge+ori
# app: sharpen
# 图像+edge=更锐利地图像，因为突出边缘
kernel_sharp = np.array([[0, 1, 0], [1, -3, 1], [0, 1, 0]], np.float32) 
lap_img = cv2.filter2D(img, -1, kernel=kernel_sharp)
cv2.imshow('sharp_cat1', lap_img)
# 这样不对，因为，周围有4个1，中间是-3，虽然有边缘效果，但是周围得1会使得原kernel有滤波效果，使图像模糊；
# 解决：所以取kernel_lap得相反数，再加上原图像，这样突出了中心像素，效果类似于小方差的高斯，所以
#      可以既有边缘效果，又保留图像清晰度
kernel_sharp = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) 
lap_img = cv2.filter2D(img, -1, kernel=kernel_sharp)
cv2.imshow('sharp_cat2', lap_img)
# 更“凶猛”的边缘效果
# 不仅考虑x-y方向上的梯度，同时考虑了对角线方向上的梯度
kernel_sharp = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]], np.float32) 
lap_img = cv2.filter2D(img, -1, kernel=kernel_sharp)
cv2.imshow('sharp_cat3', lap_img)

######## Edge #########
# x轴
edgex = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], np.float32)
sharp_img = cv2.filter2D(img, -1, kernel=edgex)
# y轴
edgey = np.array([[-1, 0, -1], [-2, 0, 2], [-1, 0, 1]], np.float32)
sharpy_img = cv2.filter2D(img, -1, kernel=edgey)
cv2.imshow('edgex_cat', sharp_img)
cv2.imshow('edgey_cat', sharpy_img)

######### 角点 ###########
img = cv2.imread('cat.jpg')
img = cv2.resize(img, (640, 480))
img_gray = np.float32(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
print(img_gray)

img_harris = cv2.cornerHarris(img_gray, 2, 3, 0.05)    # 2： blockSize: window size; 3: Sobel kernel size
cv2.imshow('img_harris1 ', img_harris)

# 没法看原因：1. float类型； 2. img_harris本质上是每个pixel对于Harris函数的响应值
# 没有看的价值
print(img_harris)

# 为了显示清楚
#img_harris = cv2.dilate(img_harris , None)
#cv2.imshow('img_harris2 ', img_harris)

thres = 0.05 * np.max(img_harris)
img[img_harris > thres] = [0, 0, 255]
cv2.imshow('img_harris3 ', img)

########### SIFT ###########
img = cv2.imread('cat.jpg')
# create sift class
sift = cv2.xfeatures2d.SIFT_create()
# detect SIFT
kp = sift.detect(img,None)   # None for mask
# compute SIFT descriptor
kp,des = sift.compute(img,kp)
print(des.shape)
img_sift= cv2.drawKeypoints(img,kp,outImage=np.array([]), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('cat_sift.jpg', img_sift)

key = cv2.waitKey()
if key == 27:
    cv2.destroyAllWindows()
    
