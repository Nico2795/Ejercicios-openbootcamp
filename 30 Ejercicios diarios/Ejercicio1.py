import pandas as pd

data = pd.read_excel(r'C:/Users/nico2/OneDrive - UNIVERSIDAD ANDRES BELLO/Documents/correo.xlsx')
df = pd.DataFrame(data, columns=['correo'])
print(df)
