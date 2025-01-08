"""
Desafio 011

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
De tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2
"""
largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
litros_de_tinta = area / 2


print(f"Sua parede tem a dimensão de {largura}X{altura} e sua área é de {area}m².\nPara pintar essa parede, você precisará de {litros_de_tinta}")