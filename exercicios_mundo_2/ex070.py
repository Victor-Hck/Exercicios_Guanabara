"""
Desafio 070

Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.
"""
# Variaveis
tot_compra = 0
maiorpreco = 0
menor_preco = None
menor_produto = ''

# Tabela
print('-'*20)
print(f"{'LOJA SUPER BARATÃO':^20}")
print('-'*20)

# Loop para percorrer enunciado
while True:
    produto = input("Nome do produto: ").strip()
    preco = float(input("Preço: "))
    tot_compra += preco
    
    if preco > 1000:
        maiorpreco += 1
        
    if menor_preco is None or preco < menor_preco:
        menor_preco = preco
        menor_produto = produto
        
    resp = input("Quer continuar [s/n] ").strip().upper()
    if resp == "N":
        break

# Imprimindo Resultado
print(f"---------- Fim do programa ----------")
print(f"O total da compra foi R${tot_compra:.2f}\nTemos {maiorpreco} produtos custando mais de R$1000.00\nO produto mais barato foi {menor_produto} que custa R${menor_preco:.2f}")