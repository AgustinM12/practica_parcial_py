import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('edades.csv')

# * convertir la columna age a datetime
df["age"] = pd.to_datetime(df["age"], dayfirst=True)

# *calcular año actual
df['edad'] = pd.Timestamp.now().year - (df['age']).dt.year

mayores_25 = df[df['edad'] > 25] 

mayores_25_ordenados = mayores_25.sort_values(by='edad')

lista_edades = {}

for edad in mayores_25_ordenados['edad']:
    if edad in lista_edades:
        lista_edades[edad] += 1
    else:   
        lista_edades[edad] = 1

diccionario = {'edad': lista_edades.keys(), 'cantidad': lista_edades.values()}

df_edades_ordenadas = pd.DataFrame(diccionario)

print(df_edades_ordenadas)

plt.plot(df_edades_ordenadas['edad'], df_edades_ordenadas['cantidad'], "r.-")
plt.xlabel('Edad')
plt.ylabel('Cantidad')
plt.title('Cantidad de personas mayores a 25 años')
plt.grid(True)
plt.show()