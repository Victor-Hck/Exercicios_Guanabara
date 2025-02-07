"""
Desafio 078

Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
valores = list()
for cont in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {cont}: ")))
    maior = max(valores)
    menor = min(valores)
print(f"Você digitou os valores {valores}")
print(f"O maior valor digitado foi {maior} na posição {valores.index(maior)}...")
print(f"O menor valor digitado foi {menor} na posição {valores.index(menor)}...")

