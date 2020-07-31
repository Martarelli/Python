import os
import random
import pygame

pygame.mixer.init()

path = "C:\\Users\\Martarelli\\Google Drive\\Documentos\\CURSOS\\PYTHON - IGNORANCIA\\Martarelli\\teste pygame"
files = os.listdir(path)
d = random.choice(files)
pygame.mixer.music.load(d)
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)


print("Reproduzindo:",d)
j = input('Digite algo para parar... ')







