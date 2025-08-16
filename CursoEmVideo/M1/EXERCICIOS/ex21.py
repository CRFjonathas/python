import pygame  # Importa o módulo pygame, usado para jogos e multimídia
pygame.mixer.init()  # Inicializa o mixer de áudio do pygame
pygame.init()  # Inicializa todos os módulos do pygame
pygame.mixer.music.load('C:/Users/jonat/OneDrive/Documentos/Jonathas/python/CursoEmVideo/M1/EXERCICIOS/ex21.mp3')  # Carrega o arquivo de música MP3
pygame.mixer.music.play()  # Inicia a reprodução da música
print('CAOS...')  # Exibe uma mensagem no console
pygame.event.wait()  # Mantém o programa aberto até que um evento aconteça (ex: fechar a janela)