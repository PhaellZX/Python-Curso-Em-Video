# DESAFIO 21 #
#   Faça um programa em Python que abra e reproduza
#   o áudio de um arquivo MP3.

# Esse código funcionou :)
import playsound
input('PLAY ♫ (Pressione o enter)')
print('Musica Rodando... ♫♪')
playsound.playsound('musica.mp3')
print('acabou...')

# Esse não, não está carregando a dll libmpg123-0 :\
#import pygame
#pygame.init()
#pygame.mixer.music.load('musica.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()