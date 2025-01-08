"""
Desafio 020

O mesmo professor do desafio anterior quer sortear a ordem de apresentação
De trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
from random import shuffle

primeiro = str(input("Primeiro aluno: "))
segundo = str(input("Segundo aluno: "))
terceiro = str(input("Terceiro aluno: "))
quarto = str(input("Quarto aluno: "))
lista = [primeiro, segundo, terceiro, quarto]

shuffle(lista)

print(f"A ordem de apresentação será: {lista}")
