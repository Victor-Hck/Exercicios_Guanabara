"""
Desafio 053

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
ex: palíndromo são palavras que são a mesma coisa se ler de traz pra frente.
"""
# Forma que eu desenvolvi o codigo
# frase = str(input("Digite uma frase: ")).replace(" ","").lower()
# fatiamento = frase[::-1]

# print(f"O inverso de {frase} é {fatiamento}")

# if fatiamento == frase:
#     print(f"A frase digitada é um PALÍNDROMO")
# else:
#     print(f"A frase digitada não é um PALÍNDROMO!")

# Forma da aula
# Entrada de dados
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

# Percorrendo letras
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
# imprime resultado
print(f"O inverso de {junto} é {inverso}")
# Verifica se e um palíndromo ou não
if inverso == junto:
    print(f"A frase digitada é um PALÍNDROMO")
else:
    print(f"A frase digitada não é um PALÍNDROMO!")
