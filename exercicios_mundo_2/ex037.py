"""
Desafio 037

Escreva um programa que leia um número inteiro qualquer
E peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
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
number = int(input("Digite um numero: "))

# Tabela de escolha
print(f"{cores['vermelho'] + 'Escolha uma das bases para conversão:' + cores['limpa']}")
print(f"{cores['verde'] + '[1]' + cores['limpa']} converter para {cores['azul'] + 'BÍNARIO' + cores['limpa']}\n{cores['verde'] + '[2]' + cores['limpa']} converter para {cores['azul'] + 'OCTAL' + cores['limpa']}\n{cores['verde'] + '[3]' + cores['limpa']} converter para {cores['azul']+ 'HEXADECIMAL' + cores['limpa']}")

# Escolhendo opção
option = int(input("Sua opção: "))

# Convertendo para escolha do usuario
if option == 1:
    print(f"{number} convertido para BÍNARIO é igual a: {bin(number)[2:]}")
elif option == 2:
    print(f"{number} convertido para OCTAL é igual a: {oct(number)[2:]}")
elif option == 3:
    print(f"{number} convertido para HEXADECIMAL é igual a: {hex(number)[2:]}")
else:
    print(f"Nenhuma das opções são validas tente novamente")
