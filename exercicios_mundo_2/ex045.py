"""
Desafio 045

Crie um programa que faça o computador jogar Jokenpô com você.
"""
# Importando bibliotecas
from time import sleep
from random import randint

# Entrada de dados
itens = ["Pedra","Papel","Tesoura"]
computador = randint(0, 2)
print("""Suas opões:
[0] PEDRA
[1] PAPEL
[2] TESOURA
""")
jogador = int(input("Qual é a sua jogada?: "))

# Dando valor a escolha do jogador

print(f"JO")
sleep(1)
print(f"KEN")
sleep(1)
print(f"PO!!!")
print('-=-'*11)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print('-=-'*11)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print(f"EMPATE")
    elif jogador == 1:
        print(f"JOGADOR VENCE")
    elif jogador == 2:
        print(f"COMPUTADOR VENCE")
    else:
        print(f"JOGADA INVÁLIDA!")
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print(f"COMPUTADOR VENCE")
    elif jogador == 1:
        print(f"EMPATE")
    elif jogador == 2:
        print(f"JOGADOR VENCE")
    else:
        print(f"JOGADA INVÁLIDA!")
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print(f"JOGADOR VENCE")
    elif jogador == 1:
        print(f"COMPUTADOR VENCE")
    elif jogador == 2:
        print(f"EMPATE")
    else:
        print(f"JOGADA INVÁLIDA!")