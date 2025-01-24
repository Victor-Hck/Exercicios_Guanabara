"""
Desafio 064

Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
Parar quando o usuário digitar o valor 999, que é a condição de parada. No final mostre
Quantos números digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
# Entrada de valores
number = int(input("Digite um número [999 para parar]: "))
contador = 0
soma = 0

# Loop para somar os valores tirando a flag
while number != 999:
    soma += number
    contador += 1
    number = int(input("Digite um número [999 para parar]: "))

# Imprime resultado do loop
print(f"Você digitou {contador} números e a soma entre eles foi {soma}.")