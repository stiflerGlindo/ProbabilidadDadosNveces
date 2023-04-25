import pandas as pd
datos = pd.read_excel(r'C:\Users\HP 245 RYZEN\Downloads', index_col=0, engine='openpyxl')
print(datos.head())

