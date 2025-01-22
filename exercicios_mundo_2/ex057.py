"""
Desafio 057

Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
# Entrada de dados
sexo = str(input("Informe seu sexo [F/M]: ")).strip().upper()[0]

# Loop para o usuario digitar o que se espera
while sexo not in 'MfFf':
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso")
