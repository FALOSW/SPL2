#Grundlagen-Python.py
import random 
#Kommentare erfolgen mit hashtag

#Ausgabe von Daten
print("Hallo Welt")

#Variable definieren (kann ohne typ erfolgen)
heimat = "Erde"

#Mehrere Variablen werden mit , getrennt
print(heimat, "an World: ", "Hallo!")

#Eingabe
wer = input("Und wer bist du?")

#und gibt den text wieder aus
if (wer == "Ich"):
    print("Hallo Du!")
else:
    print("Hallo", wer)

lieblingszahl = input("Was ist ihre Lieblingszahl? ")
print("Super, ich mag die zahl", lieblingszahl)
print("Aber die coolere Zahl", int (lieblingszahl)+10,"mag ich noch mehr!")

runden = input("Wie viele Runden sollen wir spielen?")
runden = int(runden)

for runde in range(1,runden+1):
    sieger = ""
    zufallszahl = random.randint(1,6)
    if (zufallszahl == 1 or zufallszahl == 3 or zufallszahl == 5):
        sieger = "Ich"
    else:
        sieger = "Computer"
    print("Runde", runde, "von", runden, ": Sieger: ", sieger, ": gewuerfelt wurde:", zufallszahl)
print("Game Over")