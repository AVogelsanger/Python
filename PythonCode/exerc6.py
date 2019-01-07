# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 14:45:18 2019

@author: 748418
"""

num = int(input("Digite um numero: "))
div = []

for i in range(1,num+1):
    if num % i == 0:
        div += [i]
print(div)        