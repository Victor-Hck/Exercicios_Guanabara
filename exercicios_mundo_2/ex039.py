"""
Desafio 039

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
# Importando biblioteca datetime
from datetime import date

# Puxando data do computador
ano = date.today().year

# Entrada de dados
nascimento = int(input("Ano de nascimento: "))
idade_atual = ano - nascimento

# Saida de dados
print(f"Quem nasceu em {nascimento} tem {idade_atual} anos em {ano}")

# Descobrindo alistamento do usuario
if idade_atual < 18:
    anos_faltante = 18 - idade_atual
    ano_alistamento = anos_faltante + ano
    print(f"Ainda faltam {anos_faltante} anos para o alistamento")
    print(f"Seu alistamento será em {ano_alistamento}")
elif idade_atual > 18:
    anos_passando = idade_atual - 18
    ano_alistamento = ano - anos_passando
    print(f"Você já deveria ter se alistado há {anos_passando} anos")
    print(f"Seu alistamento foi em {ano_alistamento}")
else:
    print(f"Você tem que se alistar IMEDIATAMENTE!")