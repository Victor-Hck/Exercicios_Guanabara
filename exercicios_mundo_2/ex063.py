"""
Desafio 063

Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros 
Elementos de uma sequência de Fibonacci
Ex: 0 » 1 » 1 » 2 » 3 »5 » 8
"""
# Tabela
print('-'*30)
print(f"Sequência de Fibonacci")
print('-'*30)

# Entrada de Dados
limite = int(input("Quantos termos você quer mostrar? "))
a = 0
b = 1
contador = 0

# Loop para mostrar sequencia de fibonacci
while contador < limite:
    print(f"{a}", end=' ')
    c = a + b
    a = b
    b = c
    contador += 1

# Imprimindo resultado
print(f"FIM")