# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 15:09:13 2019

@author: 748418
"""

with open("Lutador.txt") as f:
    texto = f.read()
    print(texto)
    
print(list(texto))

class TextAnalyzer:
    
    def count_str(self, texto, counter=0):
        for txt in texto:
            if txt.isalpha():
                counter+=1
        return counter
    
    def count_number(self, texto, counter=0):
        for txt in texto:
            if txt.isdigit():
                counter+=1
        return counter
    
    
letras = TextAnalyzer()
    
print(texto)
print(letras.count_str) 
print(letras.count_number)   
                