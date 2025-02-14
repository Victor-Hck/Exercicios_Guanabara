"""
Desafio 085

Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
Em uma lista única que mantanha separados os valores pares e ímpares. No final, mostre os valores
Pares e ímpares em ordem crescente.
"""
treino = [[], []]
valor = 0

for i in range(1, 8):
    valor = int(input(f"Digite o {i} valor: "))

    if valor % 2 == 0:
        treino[0].append(valor)
    else:
        treino[1].append(valor)

treino[0].sort()
treino[1].sort()
print("-=" * 30)
print(f" Os valores pares digitados forem: {treino[0]}")
print(f" Os valores impares digitados forem: {treino[1]}")


