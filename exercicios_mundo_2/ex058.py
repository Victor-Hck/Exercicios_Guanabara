"""
Desafio 058

Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um
Número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
Palpites foram necessários para vencer.
"""
# Gera números aleatorios
from random import randint # Gera números aleatorios

# Jogador escolhe numero aleatorio
computador = randint(0, 10)
contador = 1 # Começa com 1 por que o jogador já fez um palpite
print("""Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?""")

# Primeiro palpite do jogador
palpite = int(input("Qual seu palpite? "))

# Loop até o jogador acertar
while palpite != computador:
    if palpite > computador:
        print(f"Menos... Tente mais uma vez.")
    else:
        print(f"Mais... Tente mais uma vez")
    
    # Novo palpite e incrementa o contador
    palpite = int(input("Qual seu palpite? "))
    contador += 1

# Mensagem final, usando o contador corretamente  
print(f"Acertou com {contador} tentativas. Parabéns!")