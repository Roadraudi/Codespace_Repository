print("Hallo, du befindest dich jetzt in der Einkaufsliste.")

thislist = []

is_einkaufen = input("Willst du etwas auf die Liste schreiben")

if is_einkaufen in ["Ja", "ja"]:
    einkaufen = True
else:
    einkaufen = False
    print("Kein Problem, bis zum nächsten mal!")

while einkaufen == True:
    artikel = input("Was benötigst du?")
    thislist.append(artikel)
    amount = int(input("Wie viel davon?"))      # integer casting lässt aber nur zahlen wert zu keine Menge z.B. in Gramm
    thislist.append(amount)
    buy = input("Brauchen wir noch was?")
    if buy in ["Ja", "ja"]:
        einkaufen = True
    else:
        einkaufen = False
        print("Deine Einkaufsliste lauetet: ")
        print(thislist)


