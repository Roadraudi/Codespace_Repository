import matplotlib.pyplot as plt

# Daten für den Plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Erstelle den Linienplot
plt.plot(x, y)

# Beschriftungen für Achsen und Titel
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Einfacher Linienplot')

# Zeige den Plot
plt.show()
