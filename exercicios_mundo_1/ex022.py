"""
Desafio 022

Crie um programa que leia o nome completo de uma pessoa e mostre:
-> O nome com todas as letras maiúsculas. 
-> O nome com todas todas minúsculas. 
-> Quantas letras ao todo (Sem considerar espaços).
-> Quantas letras tem o primeiro nome.
"""
name = str(input("Digite o seu nome completo: "))
primeiro_nome = name.split()

print(f"Seu nome em maiúscuas é {name.upper()}")
print(f"Seu nome em minúsculas é {name.lower()}")
print(f"Seu nome tem ao todo {len(name.replace(" ", ""))} letras")
print(f"Seu primeiro nome é {primeiro_nome[0]} e ele tem {len(primeiro_nome[0])} letras")

