"""
Desafio 065

Crie um programa que leia vários números inteiros pelo teclado. No final da execução
Mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
# Entrada de dados
number = int(input("Digite um número: "))
continuar = str(input("Quer continuar? [S/N]: ")).upper()
contador = 1
soma = number
maior = number
menor = number

# Loop para descobrir valores
while continuar != 'N':
    number = int(input("Digite um número: "))
    continuar = str(input("Quer continuar? [S/N]: ")).upper()
    soma += number
    contador += 1
    if number > maior:
        maior = number
    if number < menor:
        menor = number

# Calculando media
media = soma / contador

# Imprimi resultado
print(f"Você digitou {contador} números e a média foi de {media:.2f}\nO maior valor foi {maior} e o menor foi {menor}")