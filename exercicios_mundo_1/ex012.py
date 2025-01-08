"""
Desafio 012

Faça um algoritmo que leia o preço de um produto e mostre
Seu novo preço, com 5% de desconto.
"""
preco = float(input("Qual o preço do produto?: "))
desconto = preco - (preco * 0.05) 

print(type(desconto))
print(f"O produto que custava R${preco}, na promoção com desconto de 5% vai custar R${desconto}")