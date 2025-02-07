"""
Crie um programa onde o usuário possa digitar vários valores numéricos e
Cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
valores = list()

while True:
    new_valor = int(input("Digite um valor: "))
    
    if new_valor in valores:
        print("Valor duplicado! não vou adicionar...")
    else:
        valores.append(new_valor)
        print("Valor adicionado com sucesso...")
        
    resp = input("Deseja continuar [S/N]: ").upper()
    if resp == "N":
        break
valores.sort()
print(f"Você digitou os valores {valores}")