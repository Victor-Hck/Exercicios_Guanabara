"""
Desafio 060

Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120
"""
numero = int(input("Digite um número: "))

fatorial = 1
contador = 1

while contador <= numero:
    fatorial *= contador
    contador += 1

print(f"O fatorial de {numero} é: {fatorial}")