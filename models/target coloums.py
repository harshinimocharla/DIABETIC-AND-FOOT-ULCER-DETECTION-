import pandas as pd

db_path = "C:/Users/harsh/Medical_Thermogram_Analysis/data/Plantar_Thermogram_Database.xlsx"
df = pd.read_excel(db_path)

print(df.columns)  # See available columns
print(df.head())   # Quick preview
