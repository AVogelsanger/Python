# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:48:18 2019

@author: 748418
"""

palavra = input("Digite uma palavra: ")
    
palavra = str(palavra)
 
reverso = palavra[::-1]

print(reverso)
if palavra == reverso:
    print("Palindrome")
else:
    print("Não é um palindrome")
    