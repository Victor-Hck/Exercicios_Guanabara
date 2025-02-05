"""
Desafio 075

Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
Em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
cont = 0
rep = 0
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))
num4 = int(input("Digite o último número: "))

tupla = (num1, num2, num3, num4)

par = sum(1 for num in tupla if num % 2 == 0)

for num in tupla:
    if tupla.count(num) > 1:
        rep = num
        cont = tupla.count(num)


print(f"Você digitou os valores {tupla}")
print(f"O valor {rep} pareceu {cont}")
print(f"O valor 3 apareceu na {tupla.index(3)} posição")
print(f"Os valores pares digitados foram {par}")