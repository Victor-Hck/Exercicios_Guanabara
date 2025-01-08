"""
Desafio 021

Faça um programa em python que abra e reproduza o áudio
De um arquivo MP3.
"""
# Podemos usar qualquer biblioteca e modulos para resolver os problemas
import pygame

# Inicializa o pygame e o mixer de áudio
pygame.mixer.init()

# Carrega o arquivo de áudio
pygame.mixer.music.load("musica/ex021.mp3") # Viva as Classicas <3

# Reproduz o áudio
pygame.mixer.music.play()

# Aguardar o áudio terminar antes de fechar
while pygame.mixer.music.get_busy():  # Verifica se o áudio ainda está tocando
    pygame.time.Clock().tick(10)  # Atraso para evitar sobrecarga no processador


