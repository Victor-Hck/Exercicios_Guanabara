"""
Desafio 029

Escreva um programa que leia a velocida de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado.

A multa vai custar R$7,00 por cada Km acima do limite.
"""

velocidade = float(input("Qual a velocidade atual do carro: "))
limite = 80
multa_por_km = 7

if velocidade > limite:
    excesso = velocidade - limite
    multa = excesso * multa_por_km
    print(f"MULTADO! Você excedeu o limite permitido que é de {limite}km/h.")
    print(f"Você deve pagar uma multa de R${multa:.2f}!")
    print(f"Tenha um bom dia! Dirija com segurança!")
else:
    print(f"Tenha um bom dia! Dirija com segurança!")
