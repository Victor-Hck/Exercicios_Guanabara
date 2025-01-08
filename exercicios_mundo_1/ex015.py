"""
Desafio 015

Escreva um programa que pergunte a quantidade de Km
Percorrido por um carro alugado e a quantidade de dias
Pelos quais ele foi alugado. Calcule o preço a pagar,
Sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
"""
aluguel = int(input("Quantos dias alugados?: "))
km_rodado = float(input("Quantos Km rodados?: "))
preco_aluguel = (aluguel * 60) + (km_rodado * 0.15)

print(f"O total a pagar é de R${preco_aluguel}")