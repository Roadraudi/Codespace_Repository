import random
import string


def passwortGenerator(length, use_numbers, use_special_character):
    characters = string.ascii_letters       #in characters werden alle Groß- und Kleinbuchstaben des alphabets gespeichert

    if use_numbers == True:
        characters = characters + string.digits     #in characters werden zusätzlich noch die Nummern von 0-9 gespeichert
    if use_special_character == True:
        characters = characters + string.punctuation    #in characters werden jetzt auch noch die SOnderzeichen hinzugefügt

    for i in range(length):
        print(random.choice(characters), end='')        #so lange wie die for-Schleife läuft wird ein zufälliger Buchstabe, Zahl oder Sonderzeichen aus characters gewählt und dann geprintet.

def passwortShuffeln(passwort):
    passwort_list = list(passwort)      #passwort in eine Liste legen
    random.shuffle(passwort_list)       #liste zufällig ändern
    passwort = ''.join(passwort_list)   #liste wieder in einen string verwandeln
    return passwort



action = input("Möchtest du ein neues Passwort erstellen oder eine Zeichenfolge eingeben und daraus ein Passwort erstellen?(1 oder 2)")
if action in ["1"]:
    length = int(input("Wie lange soll das Passwort werden?"))
    action_num = input("Möchtest du auch Nummern im Passwort haben?")
    if action_num in ["ja", "Ja"]:
        use_numbers = True
    else:
        use_numbers = False
    action_spec_char = input("Möchtest du auch Sonderzeichen im Passwort haben?")
    if action_spec_char in ["ja", "Ja"]:
        use_special_character = True
    else:
        use_special_character = False
    print("Dein neues Passwort lautet: ")
    passwortGenerator(length, use_numbers, use_special_character)
else:
    passwort = input("Wie lautet dein zu erstellendes Passwort?")
    print(passwortShuffeln(passwort))
