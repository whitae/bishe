#!/usr/bin/python
#coding=utf-8

#妈的之前误删了一次 所以有些备注就不写了
#下次一定记得传github

import numpy as np
import math
from anchors import *
from func import *
from map2 import *
from scipy.integrate import *
import sympy

#第一个先写一个正态分布
def zhengtai(x,std_=std):
    return 1/math.sqrt(2*math.pi*std_**2)*math.e**(-(x)**2/(2*std_**2))

#第二个是p(Dt|Xt) 在当前位置下，目标的与锚点距离向量的概率密度
def demo1(d_0,d_1,d_2,x,std_=std):
    d0 = juli(x,a1)
    d1 = juli(x,a2)
    d2 = juli(x,a3)
    #这个正态分布的标准差是距离测量的误差
    return  zhengtai(d_0-d0,std_)*zhengtai(d_1-d1,std_)*zhengtai(d_2-d2,std_)

#第三个是p(Xt|Xt_1)的概率密度 
#这里x0,x1,x2应该是自变量，他们的变化导致两点距离的变化
def demo2(x0,x1,x2,Xt_1,v_=v1,stdv_=stdv):
    Xt = [x0,x1,x2]
    #这是两个点的真实距离
    r = juli(Xt,Xt_1)
    #我觉得上面这个不行，所以换个表达方式
    ######不过暂时想不出来
    #平均距离应该是平均速度乘以时间
    #然而这个正太分布的标准差大小代表的是速度的误差

    #在这里将速度的误差直接等效成为距离的误差，
    #因为步长选择为1s,所以距离的误差等于速度的误差
    return zhengtai(r-v_*t,stdv_)

########################
########################
#下面该做什么呢，一脸蒙蔽呀
#应该写SPA的整体算法了
#这玩应能好使么
#第一步应该先产生数据点
#参数分别时速度，初始点，个数
#返回的是产生的点的列表
lujing(v1,x1,N)
#边缘概率密度是一个迭代的过程，要对第一个边缘概率赋值
#不如先假设第一个点是准确的如何？？？？




