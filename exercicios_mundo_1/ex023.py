"""
Desafio 023

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex:
Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
Obs: fazer como string é matematicamente.
"""
# Enunciado type string

number = str(input("Digite um número: ")).zfill(4)
number_div = number.split()

print(f"Unidade: {number_div[0][3]}\nDezena: {number_div[0][2]}\nCentena: {number_div[0][1]}\nMilhar: {number_div[0][0]}")

# Enunciado type int

#number = int(input("Digite um número: "))
#u = number // 1 % 10
#d = number // 10 % 10
#c = number // 100 % 10
#m = number // 1000 % 10

#print(f"Analisando o número {number}\nUnidade: {u}\nDezena: {d}\nCentena: {c}\nMilher: {m}")


