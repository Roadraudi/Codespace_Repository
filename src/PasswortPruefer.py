import random
import string

passwort = input("Wie lautet dein zu Überprüfendes Passwort?")

def passwortPruefer(passwort):
    safe = True
    passwort_list = list(passwort)
    all_characters = string.ascii_letters + string.digits + string.punctuation
    this_list = []
    for i in range(len(passwort_list)-1):
        character = passwort_list[i]
        if character != passwort_list[i+1]:
            this_list.append(character)
            this_list.append(passwort_list[i+1])
        else:
            for j in range(len(this_list)-1):
                character = random.choice(all_characters)
                if character != this_list[j]:
                    this_list.append(character)
                    break
                else:
                    j +=1
            safe = False
    if safe == False:
        print("Passwort ist nicht sicher")
        print("Ein mögliches Passwort könnte lauten:")
        unique_list(this_list)
    else:
        print("Das Passwort ist sicher!")
    return this_list

def unique_list(liste):
    neue_liste = []
    for element in liste:
        if element not in neue_liste:
            neue_liste.append(element)
    print(neue_liste)

passwortPruefer(passwort)



