"""
Desafio 059

Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep
primeiro_valor = int(input("Primeiro valor: "))
segundo_valor = int(input("Segundo valor: "))
print("""[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa""")
escolha = int(input("Qual é a sua escolha?: "))

while escolha != 5:
    if escolha == 1:
        soma = primeiro_valor + segundo_valor
        print(f"A soma entre {primeiro_valor} + {segundo_valor} é {soma}")
    elif escolha == 2:
        multiplicador = primeiro_valor * segundo_valor
        print(f"O resultado de {primeiro_valor} X {segundo_valor} é {multiplicador}")
    elif escolha == 3:
        maior = max(primeiro_valor, segundo_valor)
        print(f"Entre {primeiro_valor} e {segundo_valor} o maior valor é {maior}")
    elif escolha == 4:
        print(f"Informe os numeros novamente: ")
        primeiro_valor = int(input("Primeiro valor: "))
        segundo_valor = int(input("Segundo valor: "))
    elif escolha > 5:
        print(f"Finalizando...")
        print('-=-'*10)
        sleep(2)
    else:
        print(f"Opção invalida. Tente novamente")
    print('-=-'*10)
    print("""[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa""")
    escolha = int(input("Qual é a sua escolha?: "))

print(f"Finalizando...")
print('-=-'*10)
sleep(2)
print(f"Fim do programa! Volte sempre!")