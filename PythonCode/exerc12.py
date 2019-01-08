# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 13:44:56 2019

@author: 748418
"""

class Calculator:
    
    def soma(self, x , y):
        result = x + y
        print(str(result))
        
    def sub(self, x , y):
        result = x - y
        print(str(result))  
        
    def mult(self, x , y):
        result = x * y
        print(str(result))
        
    def div(self, x , y):
        if (y == 0):
           print("esse numero não tem como ser div.")
        else:
            result = x / y
            print(str(result))    
        
calc = Calculator()

calc.soma(2,2)
calc.sub(2,2)
calc.mult(2,2)
calc.div(4,0)