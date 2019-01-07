# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 16:15:24 2019

@author: 748418
"""

pedra = 0
papel = 1
tesoura = 2

player1 = input("Digite seu nome, player 1: ")
player2 = input("Digite seu nome, player 2: ")

try:

    while True:
        print("Jogada 1")
        print("escolha uma opção: ")
        print("Pedra")
        print("Papel")
        print("Tesoura")
    
    def compare(player1, player2):
        if player1 == player2:
            return("empate")
        elif player1 == 0:
            if player2 == 1:
                return("Player 2 ganhou!")
            else:
                return("Player 1 ganhou!")
        elif player1 == 1:
            if player2 == 2:
                return("Player 2 ganhou!")
            else:
                return("Player 1 ganhou!")
        elif player1 == 2:
            if player2 == 0:
                return("Player 1 ganhou!")
            else:
                return("Player 2 ganhou!")
        else:
              return ("opção errada, fim de jogo.")
                          sys.exit()
              
              print(compare(player1, player2))
except KeyboardInterrupt:
                          break
                
                
                
                
                
                