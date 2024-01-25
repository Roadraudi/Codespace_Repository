import pandas as pd

data = {
    "Name": ["Nico", "Dennis", "Lisa"],
    "Alter": [18, 20, 19],
    "Studiengang": ["Informatik", "BWL", "Mechatronik"]
}

df = pd.DataFrame(data)


print(df)
