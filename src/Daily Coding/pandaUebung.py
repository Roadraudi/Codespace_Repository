import pandas as pd

data = {
    "Name": ["Nico", "Dennis", "Lisa"],
    "Alter": [18, 20, 19],
    "Studiengang": ["Informatik", "BWL", "Mechatronik"]
}

df = pd.DataFrame(data)

# Anzeigen des gesamten Datenrahmens
print("Gesamter Datenrahmen:")
print(df)
print()

# Abrufen von Informationen über den Datenrahmen
print("Info über den Datenrahmen:")
print(df.info())
print()

# Abrufen von statistischen Informationen
print("Statistische Informationen:")
print(df.describe())
print()

# Abrufen einer bestimmten Spalte
print("Nur die 'Name'-Spalte:")
print(df['Name'])
print()

# Hinzufügen einer neuen Spalte
df['Geschlecht'] = ['männlich', 'männlich', 'weiblich']
print("Datenrahmen mit neuer 'Geschlecht'-Spalte:")
print(df)
print()

# Filtern von Daten basierend auf einer Bedingung
print("Nur Zeilen mit Alter über 18:")
print(df[df['Alter'] > 18])
