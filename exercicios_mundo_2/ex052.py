"""
Desafio 052

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
primo = int(input("Digite um número: "))
tot = 0

# laço para somar quantas vezes primo foi divisivel
for i in range(1, primo + 1):
    if primo % i == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(i, end='')

# Mostra quantas vezes numero foi divisivel
print(f"\033[m O número {primo} foi divisivel {tot} vezes")

# Mostra se vai ser primo ou não
if tot == 2:
    print(f"E por isso ele É PRIMO")
else:
    print(f"E por isso ele NÃO É PRIMO")