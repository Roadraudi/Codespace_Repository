import matplotlib.pyplot as plt
import numpy as np

# Daten für den Plot
x = np.linspace(0, 10, 100)  # 100 gleichmäßig verteilte Punkte zwischen 0 und 10
y = np.sin(x)  # Sinus-Funktion von x

# Erstelle den Linienplot mit spezifischen Farben und Linienstilen
plt.plot(x, y, color='blue', linestyle='--', linewidth=2, label='Sinus')

# Füge eine Legende hinzu
plt.legend()

# Fülle den Bereich unter der Sinus-Kurve
plt.fill_between(x, y, color='lightblue', alpha=0.3)

# Beschriftungen für Achsen und Titel mit LaTeX-Formatierung
plt.xlabel(r'$x$')
plt.ylabel(r'$\sin(x)$')
plt.title('Sinus-Funktion')

# Ändere die Größe der Achsen
plt.xlim(0, 10)
plt.ylim(-1.2, 1.2)

# Zeichne vertikale und horizontale Linien durch bestimmte Punkte
plt.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
plt.axvline(x=np.pi, color='red', linestyle='--', linewidth=1)

# Zeige den Plot an
plt.show()
