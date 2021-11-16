# -*- coding: utf-8 -*-
"""
@author: Rafaela e Eric
"""
'''
Questão 01

Faça um programa que leia a entrada do usuário e retorne a posição(s) e a vezes que a palavra aparecer na tupla.
'''

Tupla = ("Melhor", "Professor", "Brito", "Melhor", "Matéria", "Python")

palavra = input("Entre com uma palavra: ")


if Tupla.count(palavra) == 1:
    print(f"A palavra aparece na Tupla 1 vez e está na posição {Tupla.index(palavra, 0)}")
elif Tupla.count(palavra) > 1:
    i = 0
    pos_palavra = []
    
    while i <= Tupla.count(palavra):
        pos_palavra.append(Tupla.index(palavra, i))
        i = Tupla.index(palavra, i)+1
        
    print(f"A palavra aparece na Tupla {Tupla.count(palavra)} vezes e está nas posições {pos_palavra}")
    
else:
    print(f"A palavra não foi encontrada na Tupla, as palavras da Tupla são: {Tupla}")