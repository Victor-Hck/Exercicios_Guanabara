"""
Desafio 016

Crie um programa que leia um número real qualquer
Pelo teclado e mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
"""
from math import trunc

valor = float(input("Digite um valor: "))

print(f"O valor digitado foi {valor} e a sua porção inteira é {trunc(valor)}")