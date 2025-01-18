"""
Desafio 048

Faça um programa que calcule a soma entre todos os números ímpares que são
Multiplos de três e que se encontram no intervalo de 1 até 500.
"""
# Inicializa a variavel para armazenar a soma
soma = 0
soma2 = 0

# Itera pelo intervalo de 1 até 500
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        soma += 1
        soma2 += i

print(f"A soma de todos os {soma} valores splicitados é {soma2}")