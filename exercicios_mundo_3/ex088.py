"""
Desafio 088

Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
Gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep
print('-' * 30)
print(f"{'JOGA NA MEGA SENA':^30}")
print('-' * 30)
lista = []
jogos = list()
pergunta = int(input("Quantos jogos você quer que eu sorteie?: "))
tot = 1

while tot <= pergunta:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f"SORTEANDO {pergunta} JOGOS ", '-=' * 3)
for i, l in enumerate(jogos):
    print(f"jogo {i+1}: {l}")
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=')
