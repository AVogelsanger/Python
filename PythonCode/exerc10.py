# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:45:34 2019

@author: 748418
"""

with open('palindrome.txt',"a+") as f:
    line = f.readline()    
    palavra = str(line)
 
reverso = palavra[::-1]

print(reverso)
if palavra == reverso:
    print("É um palindrome.")
else:
    print(palavra + "Não é um palindrome")
    