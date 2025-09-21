# 21. Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

# Para a realização desse exercício, é preciso importar a biblioteca de jogos do Python, a pygame
import pygame
pygame.init()
pygame.mixer.music.load('Ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()
