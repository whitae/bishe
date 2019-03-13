#!/usr/bin/python
#coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from anchors import *

#该函数的目的：传入坐标点参数，能够绘制出网格图，并绘制出所有的点

def zuobiao(X):
    #设置坐标系的范围和大小
    fig = plt.figure(num=1,figsize=(15,9),dpi=80)
    ax = fig.add_subplot(1,1,1)
    plt.axis([0,50,0,30])
    #设置主从坐标间隔
    ax.xaxis.set_major_locator(plt.MultipleLocator(5))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(5))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
    #画线
    ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
    ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
    ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
    ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')

    #画出锚点
    #x1 = [10,40,25]
    #y1 = [22,22,8]
    arr1=np.array(a)
    plt.scatter(arr1.T[0],arr1.T[1],marker='o',color='red',s=40)
    #画出生成的点
    arr2=np.array(X[0])
    plt.scatter(arr2.T[0],arr2.T[1],marker='o',color='green',s=30)
    #画出测绘的点
    arr3=np.array(X[1])
    plt.scatter(arr3.T[0],arr3.T[1],marker='o',color='blue',s=30)
    plt.show()
