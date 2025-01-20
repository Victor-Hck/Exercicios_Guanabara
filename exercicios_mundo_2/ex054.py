"""
Desafio 054

Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores.
"""
# Importando biblioteca
from datetime import datetime

# Entrada de usuario
ano = datetime.now().year
maior = 0
menor = 0

# Verifica quantas pessoas são maiores de idades ou menores
for i in range(1, 8):
    nascimento = int(input(f"Em que ano a {i}o nasceu?: "))
    idade = ano - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1    

# Tratando narrativa da resposta
if menor == 0:
    print(f"Todos os 7 são maiores de idade")
elif menor > 1:
    print(f"No total {maior} pessoas são maiores de idade e {menor} são menores de idade")
else:    
    print(f"No total {maior} pessoas são maiores de idade e {menor} é menor de idade")