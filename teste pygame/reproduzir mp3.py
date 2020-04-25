import os
import random
from pygame import mixer

mixer.init()

path = "C:\\Users\\Martarelli\\Google Drive\\Documentos\\CURSOS\\PYTHON - IGNORANCIA\\Martarelli\\teste pygame"
files = os.listdir(path)
d = random.choice(files)
mixer.music.load(d)
mixer.music.play()
mixer.music.set_volume(1)


print("Reproduzindo:",d)
j = input('Digite algo para parar... ')







