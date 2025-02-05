"""
Desafio 077

Crie um programa que tenha uma tupla com várias palavras
(Não usar acentos). Depois disso, você deve mostrar, para cada palavra quais
são as suas vogais.
"""
tupla = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO", "GRATIS", "ESTUDAR", "PRATICAR", "TRABALHAR", "MERCADO", "PROGRAMADOR", "FUTURO")

for i in tupla:
    contagem_vogais = (letra for letra in i.lower() if letra in 'aeiou')
    vogais_str = ' '.join(contagem_vogais)
    print(f"Na palavra {i} temos {vogais_str}")