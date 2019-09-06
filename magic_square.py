# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:01:20 2019

@author: Administrator
"""

#def f2(x,y):
#    return x*y
#f2(5,7)
#
#val1 = lambda x,y:x+y
#val1 (5,5)
#

import numpy as np

N = int(input("enter the values of n for NXN matrix:"))
mg = np.zeros((N,N), dtype=int)

n = 1
i, j = 0, N//2

while n <= N**2:
    mg[i,j]=n
    n += 1
    newi, newj = (i-1) % N, (j+1)% N
    if mg[newi, newj]:
        i += 1
    else:
        i,j = newi,newj
print(mg)
