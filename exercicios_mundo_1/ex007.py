"""
Desafio 007

Desenvolva um programa que leia as duas notas de um aluno,
Calcule e mostre a sua média.
"""
n1 = float(input("Primeira nota do aluno: "))
n2 = float(input("Segunda nota do aluno: "))
media = (n1 + n2) / 2

print(f"A media entre {n1} e {n2} é igual a {media:.2f}")