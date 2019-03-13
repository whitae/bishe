#!/usr/bin/python
#coding=utf-8

#这个模块的作用是将观测的值与真实位置进行对比
#产生一个量化的评估结果
#初步选择的方法是 计算平均欧式距离

import math
import numpy as np
import sympy
from anchors import *
from func import *
from TOA import *
from map2 import *

#传入TOA函数产生的结果，计算出平均欧式距离
def e(A):
    E = []
    for i in range(len(A[0])):
        E.append(juli(A[0][i],A[1][i]))
    arr = np.array(E)
    return arr.mean()
