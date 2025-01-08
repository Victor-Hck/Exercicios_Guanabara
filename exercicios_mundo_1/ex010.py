"""
Desafio 010

Crie um programa que leia quanto dinheiro uma pessoa
Tem na carteira e mostra quantos dólares ela pode comprar.
Considere US$ 1,00 = 3,27
"""
real = float(input("Quanto dinheiro vocé tem na carteira? R$"))
dolar = real / 3.27



print(f"Com R${real} você pode comprar US${dolar:.2f}")





