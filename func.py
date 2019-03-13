#!/usr/bin/python
#coding=utf-8
import sympy
import numpy as np
import math
from anchors import *
#这个是计算两点之间距离的函数
#传入的数据是列表形式的两个点
def juli(x1,x2):
    p1 = np.array(x1)
    p2 = np.array(x2)
    p3 = p2-p1
    p4 = math.hypot(p3[0],p3[1])
    return p4

#三角定位算法，根据距离计算出坐标
def triposition(d,x1=a1[0],y1=a1[1],x2=a2[0],y2=a2[1],x3=a3[0],y3=a3[1]):
    x,y = sympy.symbols('x y')
    f1 = 2*x*(x1-x3)+np.square(x3)-np.square(x1)+2*y*(y1-y3)+np.square(y3)-np.square(y1)-(np.square(d[2])-np.square(d[0]))  
    f2 = 2*x*(x2-x3)+np.square(x3)-np.square(x2)+2*y*(y2-y3)+np.square(y3)-np.square(y2)-(np.square(d[2])-np.square(d[1]))
    result = sympy.solve([f1,f2],[x,y])
    locx,locy = result[x],result[y]
    return [locx,locy]

#函数的功能，内置锚点坐标，传入任意一点，输出距离三个锚点的距离
def juli2(p):
    d1 = juli(p,a1)
    d2 = juli(p,a2)
    d3 = juli(p,a3)
    d = [d1,d2,d3]
    return d

#用于产生速度和距离上的误差
#默认产生的个数是1
def wucha(a=std,b=N):
    arr = np.random.randn(b)*a
    return arr

#用于在一个圆周上随机的取点
#由速度确定半径的大小
#还要考虑圆心的位置
def qudian(r=1,x=x1):
    c_x=math.cos(np.random.rand()*2*math.pi)*r
    c_y=math.sin(np.random.rand()*2*math.pi)*r
    return [c_x+x[0],c_y+x[1]]

#迭代的产生100个点
def lujing(R=v1,x=x1,m=N):
    #存住每一个点
    X = [x]
    x_=x
    #迭代
    for i in range(1,m):
        a=qudian(r=R,x=x_)
        X.append(a)
        x_ = a
    return X
