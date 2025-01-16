"""
Desafio 044

Elabore um programa que calcule o valor a ser pago por um produto,
Considerando o seu preço normal e condição de pagamento:

- Á vista dinheiro/cheque: 10% de desconto
- Á vista no cartão: 5% de desconto
- Em até 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros
"""

# Entrada de dados
print(f"{'='*10} LOJAS VICTOR {'='*10}")
produto = float(input(f"Digite o valor do produto: "))

# Menu de Opções
print('='*10)
print(f"Escolha uma das opcões abaixo")
print('='*10)
print("""[1] Á vista dinheiro/cheque
[2] Á vista no cartão
[3] 2x no cartão
[4] 3x no cartão""")
pagamento = int(input("Escolha a forma de pagamento: "))

# Calculando valor de desconto
dinheiro_cheque = produto - (produto * 10/100) 
avista_cartao = produto - (produto * 5/100) 
juros = (produto * 1.20)

# Informando condição de pagamento
if pagamento == 1:
    print(f"Sua compra de R${produto} vai custar R${dinheiro_cheque} no final")
elif pagamento == 2:
    print(f"Sua compra de R${produto} vai custar R${avista_cartao} no final")
elif pagamento == 3:
    total = produto / 2    
    print(f"Sua compra será parcelada de 2x de R${total}")
    print(f"Sua compra de R${produto} vai custar R${produto} no final.")
elif pagamento == 4:
    parcelas = int(input("Quantas parcelas?: "))
    print(f"Sua compra será pacelada em {parcelas}x de R${juros / parcelas} com JUROS")
    print(f"Sua compra de R${produto} vai custar R${juros} no final.")
else:
    print(f"Informação invalida! tente novamente")