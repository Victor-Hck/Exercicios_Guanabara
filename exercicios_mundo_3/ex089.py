"""
Desafio 089

Crie um programa que leia nome e duas notas de vários alunos
E guarde tudo em uma lista composta. No final, mostre um boletim
Contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
lista = list()
cont = 0
while True:
    nome = input("Nome: ")
    nota = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    resp = input("Quer continuar? [S/N]").upper()
    cont += 1
    media = (nota + nota2) / 2
    lista.append([nome, [nota, nota2], media])
    if resp == 'N':
        break
print('-=' * 13)
print(f"{'No.':<5} {'NOME':<10} {'MÉDIA':<5}")
print('-' * 25)
for i, a in enumerate(lista):
    print(f"{i:<5}{a[0]:<10}{a[2]:>6}")
    # print(f"{cont:<5} {nome:<10} {media:<5}")
print('-' * 25)
while True:
    notas_alunos = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if notas_alunos <= len(lista) - 1:
        print(f"Notas de {lista[notas_alunos][0]} são {lista[notas_alunos][1]}")
    if notas_alunos == 999:
        break