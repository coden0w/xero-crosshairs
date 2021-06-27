import os

files = os.listdir('crosshairs/')

for f in files:
    file = f.split('.')
    print(f'Fichero: {file[0]}')