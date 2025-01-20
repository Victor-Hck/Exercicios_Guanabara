"""
Desafio 055

Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
# Entrada de dados
maior_peso = 0
menor_peso = float('inf') 

# Verifica e adiciona maior e menor peso 
for i in range(1, 6):
    peso = float(input(f"Peso da {i} pessoa: "))
    if peso > maior_peso:
        maior_peso = peso
        
    if peso < menor_peso:
        menor_peso = peso

# Imprime resultado
print(f"O maior peso lido foi:{maior_peso}\nO menor peso lido foi:{menor_peso}")