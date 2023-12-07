def primenumber(number):
    for x in range(2, int(number*0.5)+1):
        if number % x == 0:
            return False
        return True

zahl = input("Wie lautet deine zu Überprufende Zahl?")

if primenumber(zahl):
    print( "{zahl} ist eine Primzahl.")
else:
    print(f"{zahl} ist keine Primzahl.")