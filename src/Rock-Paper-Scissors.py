import random


def winner(eingabe, ki):
    if eingabe == ki:
        print("Ein Unentschieden!")

    elif eingabe in ["Schere"] and ki in ["Papier"]:
        print("Super du hast gewonnen!")
    elif eingabe in ["Papier"] and ki in ["Stein"]:
        print("Super du hast gewonnen!")
    elif eingabe in ["Stein"] and ki in ["Schere"]:
        print("Super du hast gewonnen!")
    elif eingabe in ["Schere"] and ki in ["Stein"]:
        print("Schade du hast verloren!")
    elif eingabe in ["Stein"] and ki in ["Papier"]:
        print("Schade du hast verloren!")
    elif eingabe in ["Papier"] and ki in ["Schere"]:
        print("Schade du hast verloren!")

def com(random_num):

    if random_num == 1:
        return "Stein"
    elif random_num == 2:
        return "Schere"
    elif random_num == 3:
        return "Papier"

def spielen():
    random_integer = random.randint(1, 3)
    player_action = input("Wie lautet deine Entscheidung (Schere, Stein, Papier)?")
    winner(player_action,com(random_integer))
    again = input("Willst du nochmal spielen?")
    if again in ["Ja", "ja", "j"]:
        spielen()
    else:
        print("Tschüss, bis zum nächsten mal!")

play = input("Lass uns eine Runde Schere-Stein-Papier spielen oder")
if play in ["Ja", "ja", "j"]:
    spielen()