"""
Desafio 006

Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
n1 = int(input("Digite um número: "))
dobro = n1 * 2
triplo = n1 * 3
raizQuadrada = n1**(1/2)

print(f"O dobro de {n1} vale {dobro}.\nO triplo de {n1} vale {triplo}.\nA raiz quadrada de {n1} é igual a {raizQuadrada:.2f}.")