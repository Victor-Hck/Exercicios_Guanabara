"""
Desafio 062

Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
print('='*30)
print(f"{'10 TERMOS DE UMA PA':^30}")
print('='*30)

# Entrada de dados
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1

# Loop para mostrar até onde você deseja mostrar
while cont <= 10:
    print(f"{termo}", end=' > ')
    termo += razao
    cont += 1    

print(f"PAUSA")
teste = int(input("Quantos termos você quer mostrar a mais? "))
# Repete os termos de onde parou mais mostrando mas quantas vezes o usuario deseja ver
while teste:
    adicional = 1
    while adicional <= teste:
        print(f"{termo}", end=" > ")
        termo += razao
        adicional += 1
        cont += 1
    print(f"PAUSA")
    teste = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Fim")