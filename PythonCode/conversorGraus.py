# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:18:54 2019

@author: 748418
"""
class Conversor:
    
    def celsios(self, f):
        c = (f - 32) / 1.8
        return c
    
    def fahrenheit(self, c):
        f = c * 1.8 + 32
        return f
    
temp = Conversor()

celsios = [23,15,32]
faren = [14,73,56]


print(list(map(temp.fahrenheit, celsios)))
print(list(map(temp.celsios, faren)))
    