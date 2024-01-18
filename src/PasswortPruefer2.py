
def passChecker(passwort):
    passwort_list = list(passwort)
    safe = True

    if len(passwort) < 8:
        print("Das Passwort ist leider zu kurz!")
        safe = False

    if not any(buchstabe.isupper() for buchstabe in passwort_list):
        print("Das Passwort enthält keinen Großbuchstaben!")
        safe = False

    if not any(buchstabe.islower() for buchstabe in passwort_list):
        print("Das Passwort enthält keinen Kleinbuchstaben!")
        safe = False

    if not any(buchstabe.isdigit() for buchstabe in passwort_list):
        print("Das Passwort enthält keine Zahl!")
        safe = False

    if safe == True:
        print("Das Passwort ist sicher!")


passwort = input("Geben sie ihr Passwort ein: ")
passChecker(passwort)