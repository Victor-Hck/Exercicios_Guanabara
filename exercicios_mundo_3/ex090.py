"""
Desafio 090

Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
aluno = dict()
aluno['nome'] = input("Nome: ")
aluno["média"] = float(input(f"Média de {aluno["nome"]}: "))

if aluno["média"] >= 7:
    aluno["situação"] = "Aprovado"
elif 5 <= aluno["média"] < 7:
    aluno["situação"] = "Recuperação"
else:
    aluno["situação"] = "Reprovado"

for k, v in aluno.items():
    print(f"{k} é igual a {v}")