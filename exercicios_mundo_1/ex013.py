"""
Desafio 013

Faça um algoritmo que leia o salário de um funcionário e mostre seu
Novo salário, com 15% de aumento.
"""
salario = float(input("Qual é o salário do Funcionário? R$: "))
aumento_salario =  (salario * 1.15)

print(f"Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${aumento_salario:.2f}")