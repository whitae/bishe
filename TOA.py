#!/usr/bin/python
#coding=utf-8

#这个函数的作用是传统的TOA算法

from anchors import *
from func import *
from map2 import *
import numpy as np
import math

#参数 初始点，运动的速度，测量的误差，单次实验的点的个数
def TOA(x1_=x1,v_=v1,std_=std,N_=N):
    #产生100个路径点
    X = lujing(R=v_,x=x1_,m=N_)
    
    #产生每一个点到锚点的距离
    D = map(juli2,X)
    arr1 = np.array(D)
    
    #产生观察误差
    arr2 = wucha(std_,N_*3).reshape((N_,3))
    
    #将误差与实际值相加，产生观测值
    arr3 = arr1 + arr2
    
    #由观测值产生估计位置
    X_ = []
    for i in range(N_):
        X_.append(triposition(arr3[i]))
    
    return [X,X_]

