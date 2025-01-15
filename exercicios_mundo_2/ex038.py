"""
Desafio 038

Escreva um programa que leia dois números inteiros
E compare-os, mostrando na tela uma mensagem:
- 0 primeiro valor é maior
- 0 segundo valor é maior
- Não existe valor maior, os dois são iguais
"""
# paleta de cores ASI
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'vermelho':'\033[31m',
        'ciano':'\033[36m',
        'verde':'\033[32m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30'}

# Entrada de dados
number_one = int(input("Digite o primeiro número: "))
number_two = int(input("Digite o segundo número: "))

# Mostrando resultado dos valores
if number_one > number_two:
    print(f"{cores['verde'] + 'O primeiro valor é maior' + cores['limpa']}")
elif number_two > number_one:
    print(f"{cores['verde'] + 'O segundo valor é maior' + cores['limpa']}")
else:
    print(f"{cores['vermelho'] + 'Os dois valores são IGUAIS' + cores['limpa']}")
