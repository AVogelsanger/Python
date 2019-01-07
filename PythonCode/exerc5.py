# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 14:26:42 2019

@author: 748418
"""

a = [0,1,2,3,4,5,6,7,9,10,11,12,13,14,15]

num = int(input("Quantos elementos você deseja que seja imprimido: "))

for i in a:
    if i <= num:
        print(i)
