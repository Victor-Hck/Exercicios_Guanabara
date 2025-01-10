"""
Desafio 027

Faça um programa que leia o nome completo de uma pessoa
Mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
"""
print('-'*20)
nome = str(input("Digite seu nome completo: ")).strip().split()

print(f"Seu Primeiro Nome: {nome[0]}\nSeu Ultimo Nome: {nome[-1]}")
print('-'*20)





