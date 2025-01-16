"""
Desafio 042

Refaça o desafio 035 dos triângulos, acrescentando o recurso de
Mostrar que tipo de triângulo será formado:

- Equilátero: Todos os lados iguais
- Isósceles: Dois lados iguais
- Escaleno: Todos os lados diferentes
"""
# Importando biblioteca
from datetime import date
from time import sleep

# paleta de cores ASI
cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'vermelho':'\033[31m',
        'ciano':'\033[36m',
        'verde':'\033[32m',
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;30'}

# Criando tabela superior
print(cores['verde'] + '-=-'*10)
print(f"Analisador de Triângulos")
print('-=-'*10 + cores['limpa'])

# Entrada de dados
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmente: "))

# Utilizando sleep
print(f"{cores['ciano']}Processando...{cores['limpa']}")
sleep(2)
# Calculando tipo de Triângulo
if a == b == c:
    print(f"Os segmentos acima PODEM FORMAR um triângulo Eqilátero")
elif a == b or a == c or b == c:
    print(f"Os segmentos acima PODEM FORMAR um triângulo Isósceles")
else:
    print(f"Os segmentos acima PODEM FORMAR um triângulo Escaleno")

# Verificando triângulo resposta aula
# if a < b + c and b < a + c and c < a + b:
#     print(f"Os segmentos acima PODEM FORMAR um triângulo ", end='')
#     if a == b == 3:
#         print('EQUILÁTERO!')
#     if a != b != c != a:
#         print('ESCALENO')
#     else:
#         print(f"ISÓSCELES")
