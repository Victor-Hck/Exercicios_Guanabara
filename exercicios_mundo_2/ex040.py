"""
Desafio 040

Cria um programa que leia duas notas de um aluno e culcule sua média
Mostrando uma mensagem no final, de acordo com a média atingida

- Média abaixo de 5.0:
REPROVADO

- Média entre 5.0 e 6.9:
RECUPERAÇÃO

- mÉDIA 7.0 OU SUPERIOR:
APROVADO
"""

# Entrada de dados
one_note = float(input("Primeira nota: "))
two_note = float(input("Segunda nota: "))

# calculando média
media = (one_note + two_note) / 2

# Imprimindo media
print(f"Tirando {one_note} e {two_note}, a média do aluno é {media:.1f}")

# Mostra dependencia do aluno
if 7 > media >= 5:
    print(f"O aluno está de RECUPERAÇÃO")
elif media < 5:
    print(f"O aluno está REPROVADO")
elif media >= 7:
    print(f"O aluno foi provado")
