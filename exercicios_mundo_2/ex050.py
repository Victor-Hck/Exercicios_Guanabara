"""
Desafio 050

Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares
Se o valor digitado for ímpar, desconsidere-o.
"""

# Inicializa a variável para armazenar a soma dos números pares
soma_pares = 0
conta_pares = 0
# laço para descobrir soma dos valores pares
for i in range(1, 7):
    num = int(input(f"Digite o {i} primeiro valor: "))
    if num % 2 == 0:
        conta_pares += 1
        soma_pares += num

# Trata narrativa dos valores pares
if conta_pares == 1:
    print(f"Você informou {conta_pares} número par é o valor é {soma_pares}")
elif conta_pares == 0:
    print(f"Você informou {conta_pares} números PARES e a soma foi {soma_pares}")
else:
    print(f"Você informou {conta_pares} números pares é a soma foi {soma_pares}")