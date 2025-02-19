"""
Desafio 069

Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
"""
# Variaveis
homens = 0
mulheres = 0
soma_idade = 0

# Loop para descobrir valor do enunciado
while True:
    print("Cadastre uma pessoa")
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    
    if idade >= 18:
        soma_idade += 1
        
    if sexo == "M":
        homens += 1
        
    if idade < 20 and sexo == "F":
        mulheres += 1
    
    resposta = ' '
    while resposta not in "SN":
        resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resposta == "N":
        break

# Imprimindo resultado
print(f"====== FIM DO PROGRAMA ======")
print(f"Total de pessoas com mais de 18 anos: {soma_idade}\nAo todo temos {homens} homens cadastrados\nE temos {mulheres} mulher com menos de 20 anos")