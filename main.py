import pandas as pd
from helpers.crearTablasHTML import crearTabla
import matplotlib.pyplot as plt
import numpy as np

tabla = pd.read_csv("./data/Siembras.csv")


# FILTRO1: Encontrar todos los datos de santa fe de Antioquia donde se
# tengan siembras de + de 250 arboles
print('Filtro 1')
print("\n")
filtro1 = tabla.query("Ciudad == 'Santa Fe de Antioquia' and Arboles > 250")
print(filtro1)
crearTabla(filtro1, "arbolesSantaFeDeAntioquia")
print("\n")

# Creamos un gráfico de barras de la edad contra el nombre
fig, ax = plt.subplots()
# Define las ubicaciones de las barras y su ancho
bar_locations = np.arange(filtro1.shape[0])
bar_width = 0.5
# Dibuja las barras para cada variable, ajustando la ubicación para que no se superpongan
ax.bar(bar_locations, filtro1['Arboles'], width=bar_width, label='Arboles')
# Define las etiquetas del eje x usando las etiquetas de las filas del DataFrame
ax.set_xticks(bar_locations)
ax.set_xticklabels(filtro1.index)

ax.set_xlabel('Santa Fe de Antioquia')
ax.set_ylabel('Arboles')
ax.set_title('Arboles - Santa Fe de Antioquia')
ax.legend()
plt.show()


# FILTRO2: Filtrar todos los datos de Caucasia e interpretar sus estadísticas
print('Filtro 2')
print("\n")
filtro2 = tabla.query("Ciudad == 'Caucasia'")
estadisticasFiltro2 = filtro2.describe()
print(filtro2)
print("\n")
print(estadisticasFiltro2)
crearTabla(estadisticasFiltro2, "estadisticasCaucasia")
print("\n")


# FILTRO 3: Filtrar todos los datos de las veredas Rio Arriba y La Salazar de Belmira
print('Filtro 3')
print("\n")
filtro3 = tabla.query(
    "Ciudad == 'Belmira' and Vereda == 'La Salazar' or Vereda == 'Rio Arriba'")
print(filtro3)
crearTabla(filtro3, "datosRioArribaLaSalazar")
print("\n")


# FILTRO 4: Encontrar los datos de las veredas Quitasol de Bello mostrando
# además las medias de cada ítem del dataframe
print('Filtro 4')
print("\n")
filtro4 = tabla.query("Ciudad == 'Bello' and Vereda == 'Quitasol'")
mean = filtro4.mean(numeric_only=True)
print(filtro4)
print("\n")
print(mean)
crearTabla(filtro4, "mediasQuitasol")
print("\n")


# FILTRO 5: Encontrar todos los datos de caramanta donde se tengan siembras
# de + de 100 arboles
print('Filtro 5')
print("\n")
filtro5 = tabla.query("Ciudad == 'Caramanta' and Arboles > 100")
print(filtro5)
crearTabla(filtro5, "datosCaramantaArboles")
print("\n")


# FILTRO 6: Encontrar los datos de la vereda mallarino del municipio de
# Yarumal
print('Filtro 6')
print("\n")
filtro6 = tabla.query("Ciudad == 'Yarumal' and Vereda == 'Mallarino'")
print(filtro6)
crearTabla(filtro6, "datosMallarino")
print("\n")
