"""
Desafio 049

Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário
Escolher, só que agora utilizando um laço for.
"""
# Entrada de dados
valor = int(input("Deseja ver a tabuada de qual número?: "))

# Mostra tabuada de 1 a 10 de acordo com o valor do usuario
for i in range(1, 11):
    print(f"{valor} {'X':>2} {i:>2} = {valor * i:>2}")
