# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:57:30 2019

@author: lenovo
"""
import cv2
import numpy as np
from scipy import linalg


def ransacMatching(A, B):
# A & B: List of List
'''
pseudo code:
    1.inlier ← random.sample(A,4) + random.sample(B,4)
      outlier ← []
      k ← 0 
      t ← 1
    2.compute homography of inlier:H
    3.while k < 1000 and t != 0:
        t ← 0
        if outlier isn't None:
            for points in outlier:
                e ← the error of points with H
                if e < threhold:
                    points is new inlier
                    t ← 1
                else:
                    pass
        if inlier isn't None:
            for points in outlier:
                e ← the error of points with H
                if e < threhold:
                    pass
                else:
                    points is new outlier
                    t ← 1
        sample_inlier ← random.sample(inlier,4)
        H ← homography of sample_inlier
        k ← k + 1
'''
    a = random.sample(A,4)
    b = random.sample(B,4)