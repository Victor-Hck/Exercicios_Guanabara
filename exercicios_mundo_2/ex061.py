"""
Desafio 061

Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA
Mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
# Tabela
print('='*30)
print(f"{'10 TERMOS DE UMA PA':^30}")
print('='*30)

# Entrada de dados
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
cont = 1

# Loop para exibir numeros primos
while cont <= 10:
    print(f"{termo}", end='» ')
    termo += razao
    cont += 1
print(f"Fim")
