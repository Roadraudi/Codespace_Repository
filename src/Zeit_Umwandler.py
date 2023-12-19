print("Das ist der Zeitumwandler")
print()
seconds = int(input("Anzahl von Sekunden: "))

days = seconds / (60*60*24)         #Anzahl an Tagen
sec = seconds % (60*60*24)          #Rest Sekunden

hours = seconds / (60*60)           #Anzahl an Stunden
sec = seconds % (60*60)             #Rest Sekunden

minutes = seconds / 60              #Anazhl an Minuten
sec = seconds % 60                  #Rest Sekunden

print(str(seconds) + " Sekunden sind " + str(days) +" Tage "+ str(hours) + " Stunden " + str(minutes) +" Minuten " + str(sec) + " Sekunden.")