"""
Desafio 018

Faça um programa que leia um ângulo qualquer e mostre
Na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import radians, sin, cos, tan

angulo = int(input("Digite o ângulo que você deseja: "))
radianos = radians(angulo)
seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print(f"O ângulo de {angulo:.1f} tem o SENO de {seno:.2f}\nO ângulo de {angulo:.1f} tem o COSSENO de {cosseno:.2f}\nO ângulo de {angulo:.1f} tem a TANGENTE de {tangente:.2f}")
