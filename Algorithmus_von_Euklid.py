print("Zur bestimmung des größten gemeinsamen Teilers brauche ich zwei Eingabe Werte")
zahl_a = input("Wie lautet deine erste Zahl?")
zahl_b = input("Wie lautet deine zweite Zahl?")

rest = zahl_a % zahl_b

while True:
    if rest != 0:
        zahl_a = zahl_b
        zahl_b = rest
        rest = zahl_a % zahl_b
    else:
        break

print(zahl_b)