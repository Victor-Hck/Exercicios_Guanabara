"""
Desafio 028

Escreva um programa que faça o computador "pensar"
Em um número inteiro entre 0 e 5 e peça para o usuario
tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint # Gera números aleatorios
from time import sleep # Faz o computador esperar por alguns segundos

computador = randint(0, 5) # Faz computador pensar
print('-=-'*20)
print(f"Vou pensar em um número entre 0 a 5. Tente adivinhar")
print('-=-'*20)
jogador = int(input("Em que número eu pensei? ")) # Jogador tenta adivinhar

print(f"PROCESSANDO..")
sleep(3) # Computador vai esperar 3 segundos para rodar o if/else abaixo.

if jogador == computador:
    print(f"PARABÉNS! Você conseguiu me vencer!")
else:
    print(f"GANHEI! Eu pensei no número {computador} e não no {jogador}!")




