import random

schwierig = False

def winner(eingabe, ki):
    if eingabe == ki:
        print("Ein Unentschieden!")
        schwierig = False

    elif eingabe in ["Schere"] and ki in ["Papier"]:
        print("Super du hast gewonnen!")
        schwierig = True
    elif eingabe in ["Papier"] and ki in ["Stein"]:
        print("Super du hast gewonnen!")
        schwierig = True
    elif eingabe in ["Stein"] and ki in ["Schere"]:
        print("Super du hast gewonnen!")
        schwierig = True
    elif eingabe in ["Schere"] and ki in ["Stein"]:
        print("Schade du hast verloren!")
        schwierig = False
    elif eingabe in ["Stein"] and ki in ["Papier"]:
        print("Schade du hast verloren!")
        schwierig = False
    elif eingabe in ["Papier"] and ki in ["Schere"]:
        print("Schade du hast verloren!")
        schwierig = False

def com(eingabe):
    random_num = random.randint(1, 3)
    if schwierig == True:                               #Der Computer schaut nach der vorherigen Eingabe und entscheidet dann seinen Zug. Dabei wählt er entweder das was den Spieler in der vorherigen Runde geschlagen hätte oder das andere das man normal nicht noch einmal das gleiche wählt.
        if eingabe in ["Schere"]:
            return random.choice['Papier', 'Stein']
        elif eingabe in ["Papier"]:
            return random.choice['Stein', 'Schere']
        elif eingabe in ["Stein"]:
            return random.choice['Papier', 'Schere']
    else:
        if random_num == 1:
            return "Stein"
        elif random_num == 2:
            return "Schere"
        elif random_num == 3:
            return "Papier"


def spielen():
    player_action = input("Wie lautet deine Entscheidung (Schere, Stein, Papier)?")
    winner(player_action,com(player_action))
    again = input("Willst du nochmal spielen?")
    if again in ["Ja", "ja", "j"]:
        spielen()
    else:
        print("Tschüss, bis zum nächsten mal!")

play = input("Lass uns eine Runde Schere-Stein-Papier spielen oder?")
if play in ["Ja", "ja", "j"]:
    spielen()