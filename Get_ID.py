#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

#definir un lecteur comme un lecteur simple de carte 
reader = SimpleMFRC522()

try:
    ID, text = reader.read()    #stoker le ID lit par le lecteur dans la variables ID puis l'affichier dans le terminal
    print(ID)

    #stcker le ID dans un fichier txt pour l'envoyer au serveur
    with open('toto.txt', 'w') as f:
        f.write('ID:')
        f.write(str(ID))
    f.close()

finally:
    GPIO.cleanup()

