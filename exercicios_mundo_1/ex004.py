"""
Desafio 004

Faça um programa que leia algo pelo teclado e mostre
na tela o seu tipo primitivo e todos as informações
possiveis sobre ele
"""
msg = input("Digite algo: ")

print(f"O tipo primitivo desse valor é: {type(msg)}")
print(f"Só tem espaços ? {msg.isspace()}")
print(f"É um número? {msg.isnumeric()}")
print(f"É alfabético? {msg.isalpha()}")
print(f"É alfanumérico? {msg.isalnum()}")
print(f"Está em maiúsculas? {msg.isupper()}")
print(f"Está em minúsculas? {msg.islower()}")
print(f"Está capitalizada? {msg.istitle()}")
