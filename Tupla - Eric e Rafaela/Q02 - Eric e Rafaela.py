# -*- coding: utf-8 -*-
"""
@author: Rafaela e Eric
"""
'''
Questão 02

Faça um programa que peça um intervalo para o usuário e imprima o intervalo da Tupla correspondente.
'''

Tupla = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', '...')

i, j = input('Entre com o intervalo: ').split(" ")
i = int(i)
j = int(j)

if j < len(Tupla):
    print(Tupla[i:j])
    
else:
    print(f"Não há itens suficientes na tupla, digite um intervalo até {len(Tupla)}")
