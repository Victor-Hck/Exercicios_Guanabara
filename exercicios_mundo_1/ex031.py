"""
Desafio 031

Desenvolva um programa que pergunte a distância
de uma viagem em Km.
Calcule o preça da passagem, cobrando R$0,50 por Km 
Para viagens de até 200km e R$0,45 para viagens mais longas.
"""
viajem = float(input("Qual a distancia da sua vigaem: "))
passagem = viajem * 0.50

if viajem > 200:
    passagem = viajem * 0.45
    print(f"Você está preste a começar uma viagem de {viajem:.1f}Km.\n E o preço da sua passagem será de R${passagem:.2f}")
else: 
    print(f"Você está preste a começar uma viagem de {viajem:.1f}Km.\n E o preço da sua passagem será de R${passagem:.2f}")
