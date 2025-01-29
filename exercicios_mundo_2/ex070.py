"""
Desafio 070

Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.
"""
tot_compra = 0

while True:
    produto = input("Nome do produto: ")
    preco = int(input("Preço: "))
    tot_compra += preco
    resp = input("Quer continuar [s/n] ").upper()
    if resp == "N":
        break
print(f"Fim do programa")
print(f"O total da compra foi {tot_compra}")