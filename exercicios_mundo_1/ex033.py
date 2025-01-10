"""
Desafio 033

Faça um programa que leia três numeros
E mostre qual é o maior e qual é o menor.
"""
a = int(input("Primeiro Valor: "))
b = int(input("Segundo Valor: "))
c = int(input("Terceiro Valor: "))


# 1 forma de fazer, mas foge do escopo do exercicio que é utilizar condicionais.
menor = min(a, b, c)
maior = max(a, b, c)
print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")

# 2 forma de fazer
# if a < b and a < c:
#     print(f"O menor valor digitado foi {a}")
# elif b < a and b < c:
#     print(f"O menor valor digitado foi {b}")
# else:
#     print(f"O menor valor digitado foi {c}")

# if a > b and a > c:
#     print(f"O maior valor digitado foi {a}")
# elif b > a and b > c:
#     print(f"O maior valor digitado foi {b}")
# else:
#     print(f"O maior valor digitado foi {c}")

# 3 forma de fazer
# if a < b and a < c:
#     menor = a
#     print(f"O menor valor digitado foi {a}")
# elif b < a and b < c:
#     menor = b
#     print(f"O menor valor digitado foi {b}")
# else:
#     print(f"O menor valor digitado foi {c}")

# if a > b and a > c:
#     maior = a
#     print(f"O maior valor digitado foi {a}")
# elif b > a and b > c:
#     maior = b
#     print(f"O maior valor digitado foi {b}")
# else:
#     print(f"O maior valor digitado foi {c}")
    