# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:20:56 2019

@author: 748418
"""

a = [1,2,3]
b = [0,1,2,3,4,5,6,7,8,9,10]

soma = (a+b)

c = []

for i in soma:
    if soma.count(i) == 1:
        c.append(i)
print(c)        