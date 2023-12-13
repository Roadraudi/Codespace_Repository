from random import *


print("Hallo, du befindest dich im Glücksspiel Zufallszahl. Errate die vom Computer erstellte Zufallszahl die zischen 1 und 10 liegt und erhalte den Jackpot ansonsten erhälst du nichts! ")
is_spielen = input("Willst du eine Runde gegen den Computer spielen?")
is_einsatz = int(input("Wie hoch ist dein Einsatz"))

jackpot = randint(200,300)      # Jackpot variert pro Spiel zwischen 200€ und 300€
print("Heute im Jackpot liegen" + str(jackpot) + "€")

if is_spielen in ["ja", "Ja"]:
    number = input("Wie lautet deine Zahl")
    com_num = randint(1,10)
    if com_num == number:
        print("Super du hast die Zahl erhalten und erhälst den Jackpot von " + str(jackpot) + "€")
    else:
        print("Das war leider nichts.")
        print("Bis zum nächsten mal.")
else:
    print("Bis zum nächsten mal!")
