"""
Desafio 066

Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
Que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles ( desconsiderando o flag).
"""
# Entrada de dados
contador = 0
numero = 0
soma = 0

# Itera até digitar numero 999
while True:
    numero = int(input(f"Digite o {soma} valor (999 para parar): "))
    if numero == 999:
        break
    soma += 1
    contador += numero

# Imprimindo resultado
print(f"A soma dos {soma} valores foi {contador}!")