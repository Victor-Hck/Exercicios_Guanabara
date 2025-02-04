"""
Desafio 073

Crie uma tupla preenchida com os 20 primeiros colocados da tabela do 
Campeonato Brasileiro de futebol, na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.
"""
tabela_brasileirao = ("Palmeiras", "Flamengo", "Corinthians", "Atlético-MG", "Grêmio", "Athletico-PR", "Internacional", "Fluminense", "Botafogo", "São Paulo", "Cuiabá", "Fortaleza", "Cruzeiro", "Vasco", "Bahia", "Goiás", "Santos", "Coritiba", "América-MG", "Avaí")
print(f"")
print(f"Os 5 primeiros são {tabela_brasileirao[0:5]}")
print(f"Os 4 últimos são {tabela_brasileirao[-4:]}")
print(f"Times em ordem alfabética: {sorted(tabela_brasileirao)}")
print(f"O Atlético-MG está na {tabela_brasileirao.index('Atlético-MG')+1} posição")