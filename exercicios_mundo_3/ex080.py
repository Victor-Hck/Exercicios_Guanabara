"""
Desafio 080

Crie um programa onde o usuário possa digitar cinco valores numéricos
E cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())

No final, mostre a lista ordenada na tela.
"""
valores = list()

for i in range(5):
    new_valor = int(input("Digite um número: "))
    
    if not valores:
        valores.append(new_valor)
        print(f"Adicionado na posição 0, pois a lista estava vazia.")
    elif new_valor < valores[0]:
        valores.insert(0, new_valor)
        print(f"Adicionado na posição 0, pois a lista estava vazia.")
    elif new_valor > valores[-1]:
        valores.insert(new_valor)
        print(f"Adicionado na posição 0, pois é o menor valor até agora.")
    else:
        pos = 0
        while pos < len(valores) and valores[pos] < new_valor:
            pos += 1
        valores.insert(pos, new_valor)
        print(f"Adicionado na posição {pos}, pois está entre os valores existentes.")


print(f"Lista ordenada: {valores}")