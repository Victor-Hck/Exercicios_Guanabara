"""
Desafio 071

Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50,R$20,R$10 e R$1.
"""
# Tabela
print('='*20)
print(f"{'BANCO CEV':^20}")
print('='*20)
# Loop para destribuir cedulas
while True:
    valor = int(input("Que valor você quer sacar? R$ "))
    cedulas = [50, 20, 10, 1]
    for cedulas in cedulas:
        qtd_cedulas = valor // cedulas
        if qtd_cedulas > 0:
            print(f"Total de {qtd_cedulas} cédulas de R${cedulas}")
            valor -= qtd_cedulas * cedulas
    break
# Imprimindo resultado
print(f"Volte sempre ao BANCO CEV! Tenha um bom dia!")