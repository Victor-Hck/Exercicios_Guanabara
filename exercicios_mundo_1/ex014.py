"""
Desafio 014

Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
"""
celsius = float(input("Informe a temperatura em °C: "))
fahrenheit = (celsius *  1.8) + 32

print(f"A temperatura de {celsius}°C corresponde a {fahrenheit}°F")