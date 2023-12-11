print("Hallo, du befindest dich jetzt in der Einkaufsliste.")

thislist = []

is_einkaufen = input("Willst du etwas auf die Liste schreiben")

if is_einkaufen in ["Ja", "ja"]:
    einkaufen = True
else:
    einkaufen = False

while einkaufen == True:
    artikel = input("Was benötigst du?")
    thislist.append(artikel)
    buy = input("Brauchen wir noch was?")
    if buy in ["Ja", "ja"]:
        einkaufen = True
    else:
        einkaufen = False
        print("Deine Einkaufsliste lauetet: ")
        print(thislist)

