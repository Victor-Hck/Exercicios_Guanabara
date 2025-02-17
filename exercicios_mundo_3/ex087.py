"""
Desafio 087

Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
valor_total = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        valor_total += matriz[l][2] 
print("-=" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()
print("-=" * 30)
print(f"A soma dos valores pares é {pares}")
print(f"A soma dos valores da terceira coluna é {valor_total}")
print(f"O maior valor da segunda linha é {max(matriz[1])}")
