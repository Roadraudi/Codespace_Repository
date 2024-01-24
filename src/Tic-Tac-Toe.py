spielbrett = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def show_spielbrett():
    for zeile in spielbrett:
        print("|".join(zeile))
        print("_____")

def play():
    player1 = True
    eingabe = [
        [], []
    ]
    if player1 == True:
        print("Spieler 1 ist an der Reihe")
        print("Setze dein X!", end=' ')
        eingabe = input("Spalte|Zeile")
        player1 = False
    else:
        print("Spieler 2 ist an der Reihe")
        eingabe = input("Setze dein 0!(Spalte|Zeile)")
        player1 = True

show_spielbrett()
play()