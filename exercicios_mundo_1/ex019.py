"""
Desafio 019

Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
from random import choice

primeiro = input("Primeiro aluno: ")
segundo = input("Segundo aluno: ")
terceiro = input("Terceiro aluno: ")
quarto = input("Quarto aluno: ")
lista = [primeiro, segundo, terceiro, quarto]
escolhido = choice(lista)

print(f"O aluno escolhido foi: {escolhido}")
