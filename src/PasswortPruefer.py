import random
import string

passwort = input("Wie lautet dein zu Überprüfendes Passwort?")

def passwortPruefer(passwort):
    safe = True
    passwort_list = list(passwort)
    all_characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(len(passwort_list)-1):
        character = passwort_list[i]
        if character != passwort_list[i+1]:
            unique_list = [character]
        else:
            for j in range(len(unique_list)-1):
                character = random.choice(all_characters)
                if character != unique_list[j]:
                    unique_list[character]
                    break
                else:
                    j +=1
            safe = False
    if safe == False:
        print("Passwort ist nicht sicher")
    else:
        print("Passwort ist sicher")


passwortPruefer(passwort)