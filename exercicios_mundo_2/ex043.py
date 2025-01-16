"""
Desafio 043

Desenvolva uma lógica que leia o peso e altura de uma pessoa
Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo.

- Abaixo de 18,5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acime de 40: Obesidade mórbida
"""
# Entrada de dados
altura = float(input("Qual sua altura?: "))
peso = float(input("Qual seu peso?: "))

# Calculando IMC
imc = peso / (altura ** 2)

# Imprimindo IMC 
print(f"IMC:{imc:.1f}")

# Calculando status
if imc < 18.5:
    print(f"Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print(f"Peso ideal")
elif imc > 25 and imc <= 30:
    print(f"Sobrepeso")
elif imc > 30 and imc <= 40:
    print(f"Obesidade") 
else:
    print(f"Obesidade mórbida")