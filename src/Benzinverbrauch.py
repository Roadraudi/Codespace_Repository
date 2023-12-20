def consum_100(cons, dist):
    erg = cons / dist * 100        #Verbrauch auf 100km
    print("Der Verbrauch liegt bei " +str(erg) + " Liter pro 100km.")

def consum(cons, dist):
    erg2 =  dist / cons
    print("Sie können eine Strecke von " + str(erg2) + " pro Liter zurücklegen.")


print("Berechnung des Beninz-Verbrauchs")
distance = float(input("Gefahrene Strecke in km: "))
consumption = float(input("Benötigtes Benzin in Liter: "))

consum_100(consumption, distance)
consum(consumption, distance)

