"""
Desafio 032

Faça um programa que leia um ano
Qualquer e mostre se ele é BISSEXTO.
"""
from datetime import date
ano = int(input("Que ano quer analisar? Coloque o 0 para analisar o ano atual: "))

if ano == 0:
    ano = date.today().year # Pega o ano atual da sua maquina
if (ano % 4 == 0 and ano % 100) or ano % 400 == 0:
    print(f"Ano {ano} e BISSEXTO")
else:
    print(f"Ano {ano} não é BISSEXTO")
    



