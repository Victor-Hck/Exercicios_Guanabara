"""
Desafio 051

Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa programassão.
"""
# Criando tabela
print('='*30)
print(f"{'10 TERMOS DE UMA PA':^30}")
print('='*30)

# Entrada de dados
termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo + (10 - 1) * razao

# Verificando termo, razão e incluindo decimo termo
for i in range(termo, decimo + razao, razao):
    print(f"{i}", end='→ ')
print(f"ACABOU")