"""
Desafio 008

Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.
"""
metros = (float(input("Uma distância em metros: ")))
decametros = metros / 10
hectometros = metros / 100
quilometro = metros / 1000
decimetros = metros * 10
centimetros = metros * 100 
milimetros = metros * 1000

print(f"A medida de {metros}m corresponde a\n{quilometro}km\n{hectometros}hm\n{decametros}dam\n{decimetros}dm\n{centimetros}cm\n{milimetros}mm")