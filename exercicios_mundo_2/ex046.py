"""
Desafio 046

Faça um programa que mostre na tela uma contagem regrssiva para o estouro de fogos de artifício,
Indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
# Importando Biblioteca time
from time import sleep

# Contando de 10 a 0
for c in range(10, -1, -1):
    print(c)
    sleep(1) # Utilizando sleep

# Imprimindo resultado
print(f"\033[31mFOGOS DE ARTIFICIO\033[m")