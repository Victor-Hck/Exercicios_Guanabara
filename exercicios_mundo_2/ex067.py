"""
Desafio 067

Faça um programa que mostre a tabuada de vários números, um de cada vez
Para cada valor digitado pelo usuário. O programa será interrompido quando
O número solicitado for negativo.
"""
# Loop para mostrar tabuada
while True:
    numero = int(input("Quer ver a tabuada de qual valor?: "))
    if numero < 0:
        break
    print('-'*30)
    contador = 1
    while contador <= 10:
        multiplicacao = numero * contador
        print(f"{numero} X {contador} = {multiplicacao}")
        contador += 1
    print('-'*30)
# Imprime mensagem de encerramento
print(f"Programa encerrado. Até a próxima!")