"""
Desafio 082

Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores
Pares e os impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
valores = list()
a = list()
b = list()

while True:
    new_valor = int(input("Digite um valor: "))
    valores.append(new_valor)
    if new_valor % 2 == 0:
        a.append(new_valor)
    elif new_valor % 2 == 1:
        b.append(new_valor)
    resp = input("Deseja continuar [S/N]: ").upper()
    if resp == "N":
        break

print(f"A lista completa é {valores}")
print(f"A lista de pares é {a}")
print(f"A lista de ímpares é {b}")

