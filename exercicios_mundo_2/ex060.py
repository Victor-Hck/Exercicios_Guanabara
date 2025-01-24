"""
Desafio 060

Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120
"""
# Entrada de valores
numero = int(input("Digite um número: "))

fatorial = 1
contador = 1

# Loop para gerar fatorial
while contador <= numero:
    fatorial *= contador
    contador += 1

# Imprimindo fatorial
print(f"O fatorial de {numero} é: {fatorial}")