#coding=utf-8
#!/usr/bin/python

import matplotlib.pyplot as plt 

def huatu():
    ax = plt.axes([0.025, 0.025, 0.95, 0.95]) #[xmin,ymin,xmax,ymax] 
    ax.set_xlim(0,4) 
    ax.set_ylim(0,3) 
    ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))#设置x主坐标间隔 1 
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))#设置x从坐标间隔 0.1 
    ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))#设置y主坐标间隔 1 
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))#设置y从坐标间隔 0.1 
    ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
    #由每个x主坐标出发对x主坐标画垂直于x轴的线段
    ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
    #由每个x主坐标出发对x主坐标画垂直于x轴的线段
    ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
    ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
    ax.set_xticklabels([])
    #标记x轴主坐标的值,在这里设为空值，则表示坐标无数值标定；其他情况如
    #ax.set_xticklabels([i for i in range(10)])
    ax.set_yticklabels([])
    plt.show()
