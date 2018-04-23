#zahlenraten.py

import random
max = 200
zufallszahl = random.randint(1,max)
versuche = 0
gewonnen = False
print("Bitte geben sie ihre gewünschte Zahl zwischen 1 und", max,"ein")

while(gewonnen == False):
    zahl = input("Welche zahl raten sie?")
    zahl = int(zahl)
    versuche += 1
    if (zahl == zufallszahl):
        gewonnen = True
    if (zahl < zufallszahl):
        print("Meine gewählte Zahl ist groesser")
    if (zahl > zufallszahl):
        print("Meine gewählte Zahl ist kleiner")

print("Bravo! sie die Zahl mit", versuche, "Versuche erraten")

