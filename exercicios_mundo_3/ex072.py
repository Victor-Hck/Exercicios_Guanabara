"""
Desafio 072

Crie um programa que tenha uma tupla totalmente preenchida
Com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.
"""
numeros_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze","doze", "treze", "quatorze", "quinze", "dezesseis","dezessete", "dezoito", "dezenove", "vinte")
while True:
    number = int(input("Digite um número entre 0 e 20: "))
    if 0 <= number <= 20:
        break
    print("Tente novamente. ", end='')
print(f"Você digitou o número {numeros_extenso[number]}")