"""
Desafio 056

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""
# Entrada de dados
media = 0
idade_velho = 0
nome_velho = ""
menor_de_20 = 0
soma_idade = 0

# Verificando simulado
for i in range(1, 5):
    print(f"-----{i}o PESSOA-----")
    nome = str(input("Nome: ")).replace(" ","").upper()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).replace(" ","").upper()
    soma_idade += idade
    if sexo == "M" and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome
    
    if sexo == "F" and idade < 20:
        menor_de_20 += 1

# Calculando a média após o loop
media = soma_idade / 4
# Imprimindo resultado
print(f"A média de idade do grupo é de {media} anos\nO homem mais velho é {nome_velho} com {idade_velho} anos")

# Tratando narrativa
if menor_de_20 > 1:
    print(f"Temos {menor_de_20} mulheres com menos de 20 anos")
elif menor_de_20 == 0:
    print(f"Não temos nenhuma mulher com menos de 20 anos")
else:
    print(f"Temos {menor_de_20} mulher com menos de 20 anos")