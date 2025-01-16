"""
Desafio 041

A confederação nacional de natação precisa de um programa que leia o ano de nascimento
De um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: Sênior
- Acima: Master
"""
# Importando biblioteca
from datetime import date
from time import sleep

# ano do sistema
sistem_year = date.today().year

# Entrada de dados
ano_nascimento = int(input("Em que ano você nasceu?: "))

# Calculando idade
idade = sistem_year - ano_nascimento

# Utilizando sleep
print(f"\033[31mProcessando...\033[m")
sleep(5)

# Imprimindo idade
print(f"O atleta tem {idade} anos.")

# Descobrindo categoria do aluno
if ano_nascimento <= 9:
    print(f"Classificação: MIRIM")
elif ano_nascimento <= 14:
    print(f"Classificação: INFANTIL")
elif ano_nascimento <= 19:
    print(f"Classificação: JUNIOR")
elif ano_nascimento <= 25:
    print(f"Classificação: SÊNIOR")
else:
    print(f"Classificação: MASTER")