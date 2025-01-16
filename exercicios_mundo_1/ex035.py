"""
Desafio 035

Desenvolva um programa que leia o comprimento de três 
Retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
print('-=-'*10)
print(f"Analisador de Triângulos")
print('-=-'*10)

a = float(input("Primeiro Valor: "))
b = float(input("Segundo Valor: "))
c = float(input("Terceiro Valor: "))

if (a < b + c) and (b < a + c) and (c < a + b):
    print(f"Os segmentos acima PODEM FORMAR triângulo!")
else:
    print(f"Os segmentos acima NÃO PODEM FORMAR triângulo!")   