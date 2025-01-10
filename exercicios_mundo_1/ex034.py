"""
Desafio 034

Escreva um programa que pergunte o salário
De um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1.250, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.
"""
salario = float(input("Digite o seu salário: "))

if salario <= 1250:
    novo_valor = salario + (salario * 15 / 100)
else:
    novo_valor = salario + (salario * 10 / 100)

print(f"Quem ganhava R${salario} passa a ganhar R${novo_valor} agora.")
    

    
