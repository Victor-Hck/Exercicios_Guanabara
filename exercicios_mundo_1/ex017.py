"""
Desafio 017

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
De um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""
from math import hypot

cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))
hi = hypot(cateto_oposto, cateto_adjacente)

print(f"A hipotenusa vai medir {hypot(hi):.2f}")