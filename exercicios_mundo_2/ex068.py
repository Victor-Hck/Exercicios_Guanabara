"""
Desafio 068

Faça um programa que que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total de
vitorias consecutivas que ele conquistou no final do jogo.
"""
# Importando biblioteca
from random import randint

# Criando tabela
print('-='*15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print('-='*15)

# Variavel
vitorias = 0

# Loop para somar quantas vezes você ganhou
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(1,10)
    par_ou_impar = input("Par ou Ímpar? [P/I] ").strip().upper()
    
    soma = jogador + computador
    resultado = "PAR" if soma % 2 == 0 else "ÍMPAR"
    print('-'*15)
    print(f"Você jogou {jogador} e o computador {computador}. Total de {soma} deu {resultado}")
    print('-'*15)
    if (par_ou_impar == "P" and resultado == "PAR") or (par_ou_impar == "I" and resultado == "ÍMPAR"):
        print(f"Você ganhou")
        vitorias += 1
    else:
        print(f"VOCÊ PERDEU")
        break

# Imprimindo resultado
print(f"GAME OVER! Você venceu {vitorias} vezes.")

