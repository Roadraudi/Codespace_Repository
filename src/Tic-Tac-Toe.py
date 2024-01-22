spielbrett = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def show_spielbrett():
    for zeile in spielbrett:
        print("|".join(zeile))
        print("_____")

show_spielbrett()