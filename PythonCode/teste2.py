# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 20:28:47 2019

@author: 748418
"""

import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import lightFM

#buscar(fetch) dados e formata-los
data = fetch_movielens(min_rating=4.0)
#printtraining and testing data 
print(repr(data['train']))
print(repr(data['test']))

#criar o modelo
model = lightFM(loss='wrap')

#modelo trem
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):
    
    #números de usuários e filmes em dados de treinamento
    n_users, n_items = data['train'].shape
    
    #gerar recomendação para cada usuário que inserirmos
    for user_id in user_ids:
        #filmes que eles já gostam
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
        
        #filmes nosso modelo prevê que eles vão gostar
        scores = model.predict(user_id, np.arange(n_items))
        
        #Rank, em seguida, em ordem de mais gostou da lista
        top_items = data['item_labels'][np.argsort(-scores)]
        
        #print out o resultado
        print("Usuário %s" % user_id)
        print("         Known positives ")
            
        for x in known_positives[:3]:
            print("       %s" % x)
            
            
        print("        Recomendados:")    
        for x in top_items[:3]:
            print("       %s"  % x)
            
sample_recommendation(model, data, [3,25,450])            
        
        
        
        
    