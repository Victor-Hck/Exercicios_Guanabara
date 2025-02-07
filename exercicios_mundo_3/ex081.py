"""
Desafio 081

Crie um programa que vai ler vários numeros e colocar em uma lista.
Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
valores = list()

while True:
    new_valor = int(input("Digite um valor: "))
    
    valores.append(new_valor)
    resp = input("Deseja continuar [S/N]").upper()
    if resp == "N":
        break
valores.sort(reverse=True)
print(f"Foram digitados {len(valores)} números")
print(f"{valores}")
if 5 in valores:
    print("O valor 5 está na lista")
else:
    print("O valor 5 não está na lista")