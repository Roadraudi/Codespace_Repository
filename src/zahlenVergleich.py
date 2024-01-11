def biggestNumber(num1, num2, num3):
    if num1 < num2:
        num1 = num2
    if num1 < num3:
        num1 = num3
    return num1

def smallestNumber(num1, num2, num3):
    if num1 > num2:
        num1 = num2
    if num1 > num3:
        num1 = num3
    return num1

zahl1 = int(input("Geb bitte deine erste Zahl ein: "))
zahl2 = int(input("Geb bitte deine zweite Zahl ein: "))
zahl3 = int(input("Geb bitte deine dritte Zahl ein: "))
eingabe = input("Willst du nach der größten oder kleinsten Zahl suchen?")
if eingabe in ["Größte", "größte", "groß", "Groß"]:
    print(biggestNumber(zahl1, zahl2, zahl3))
elif eingabe in ["Kleinste", "kleinste", "klein", "Klein"]:
    print(smallestNumber(zahl1, zahl2, zahl3))
else:
    print("Deine Eingabe war nicht korrekt!")

