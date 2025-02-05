"""
Desafio 074

Crie um programa que vai gerar cinco números aleatórios e colocar um uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
valor que estáo na tupla.
"""
import random

minha_tupla = tuple(random.sample(range(10), 5))

print(f"Os valores sorteados foram: ", *minha_tupla)
print(f"O maior valor sorteado foi: {max(minha_tupla)}")
print(f"O menor valor sorteado foi: {min(minha_tupla)}")