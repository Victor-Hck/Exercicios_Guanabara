"""
Desafio 036

Escreva um programa para aprovar o empréstimo bancário
Para a compra de uma casa. O programa vai perguntar o
Valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
Do salário ou então o empréstimo será negado.
"""
# Entrada de dados
casa = float(input("Valor da casa: "))
salario = float(input("Salario do comprador: "))
anos = int(input("Quantos anos de financiamento?: "))

# Cálculo da prestação
prestacao = casa / (anos * 12) # Converte anos para meses

# Cálculo excedido
limite = salario * 0.3

# Exibição do resultado
print(f"Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}")

# Condição do emprestimo
if prestacao > limite:
    print("Empréstimo NEGADO")
else:
    print("Empréstimo porde ser CONCEDIDO")