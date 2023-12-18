print("Bercehnung des Body Mass Index:")
print()
height = float(input("Wie groß bist du? (Größe in Meter) "))            #Casting vom Input
weight = float(input("Wie viel wiegst du? (Gewicht in Kilogramm)"))      #Casting vom Input

index = weight / (height * height)
index = round(index, 2)

if index < 18.5:
    print("Laut deinem BMI Index hast du Untergewicht.")
elif index <= 24.9:
    print("Laut deinem BMI Index befindest du dch im Normalbereich")
else:
    print("Laut deinem BMI Index hast du Übergewicht.")

