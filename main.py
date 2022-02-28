
from spieler import Spieler
from parasitens import Parasiten
import os

os.system("cls")

print()
print('Die Stadt ist voll von Parasiten der BÖSEN HEXE DES OSTENS')
print('Du bist auf Straße 1 und musst')
print('zur Straße 30 gehen um dich zu retten.')
print()
print('Die BÖSE HEXE DES OSTENS und ihre PARASITEN bewegen sich 1, 2 oder 3 Straßen rückwärts oder vorwärts')
print('Du bewegst dich 1, 2 oder 3 Straßen immer vorwärts')
print()


nummer = ''

while nummer not in ('1', '2', '3', '4'):
    nummer = input(" Nummer Spieler (1/4): ")


spielern = []

for i in range(1, int(nummer)+1):
    name = input(" Name " + str(i) + "° Spieler: ").capitalize()
    spieler = Spieler(name)
    spielern.append(spieler)

herde = []

for i in range(10):
    z = Parasiten()
    herde.append(z)

while len(spielern) >0:

    os.system("cls")

    print("   NAME     -      STRAßE    -     ENERGIE")
    print("-------------------------------------------")

    for spieler in spielern:
        nom, cal, ene = spieler.platz()

        print("   {:8}     -     {:2}      -       {:2}".format(nom, cal, ene))
    print()


    strasses = []

    for parasiten in herde:
        if not parasiten.nicht_sichtbar():
            strasses.append(parasiten.strasse)
    strasses.sort()
    print('Die HEXE DES OSTEN und ihre PARASITEN HERDE befinden sich auf Straßen: ')
    for elemento in strasses:
        print(elemento, end=" ")
    print()
    print()


    gewinner = []
    for spieler in spielern:
        if spieler.strasse >= 30:
            gewinner.append(spieler)

    if len(gewinner) > 0:
        for spieler in spielern:
            print(" {}, Du/Ihr hast/habt es geschafft, den Parasiten zu entkommen.".format(spieler.name))
        print(" Du/Ihr hast/habt das Spiel gewonnen.")
        print()
        break


    for spieler in list(spielern):
        if spieler.energie <=0:
            print(" {}, Du hast deine ganze Energie verloren. Die BÖSE HEXE DES OSTENS hat Dich gesehen und du kannst dich nicht bewegen....OHH ...OHH...die BÖSE HEXE kommt zu dir".format(spieler.name))
            spielern.remove(spieler)

    
    for spieler in list(spielern):
        for parasiten in herde:
            if parasiten.strasse == spieler.strasse:
                if spieler in spielern:
                    print(" {}, Ein Parasit der BÖSEN HEXE DES OSTENS hat Dich gesehen. Er frisst deine Seele und dein Gehirn...HA...HA..HA....HUNGER..., du hast verloren".format(spieler.name))
                    spielern.remove(spieler)



    print()

    for spieler in spielern:
        geschwindigkeit = ''
        while geschwindigkeit not in ("1", "2", "3"):
            geschwindigkeit = input(" Wie viele Straßen du {} bewegen möchtest (1/2/3): ".format(spieler.name))
        spieler.bewegen(geschwindigkeit)


    for z in list(herde):
        z.bewegen()
        if z.nicht_sichtbar():
            herde.remove(z)


else:
    print("DIE BÖSE HEXE DES OSTENS und ihre PARASITEN haben Euch aufgefressen, es gibt keine Gewinner.... HA....HA....HA..")
    print()