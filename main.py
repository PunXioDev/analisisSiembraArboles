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

# Creamos un gráfico de barras de la edad contra el nombre
fig, ax = plt.subplots()
# Define las ubicaciones de las barras y su ancho
bar_locations = np.arange(estadisticasFiltro2.shape[0])
bar_width = 0.5
# Dibuja las barras para cada variable, ajustando la ubicación para que no se superpongan
ax.bar(bar_locations, estadisticasFiltro2['Ticket'], width=bar_width, label='Ticket')

ax.bar(bar_locations, estadisticasFiltro2['Arboles'], width=bar_width, label='Arboles')

ax.bar(bar_locations, estadisticasFiltro2['Hectareas'], width=bar_width, label='Hectareas')



# Define las etiquetas del eje x usando las etiquetas de las filas del DataFrame
ax.set_xticks(bar_locations)
ax.set_xticklabels(estadisticasFiltro2.index)

ax.set_xlabel('Caucasia')

ax.set_title('Caucasia estadisticas')
ax.legend()
plt.show()



# FILTRO 3: Filtrar todos los datos de las veredas Rio Arriba y La Salazar de Belmira
print('Filtro 3')
print("\n")
filtro3 = tabla.query(
    "Ciudad == 'Belmira' and Vereda == 'La Salazar' or Vereda == 'Rio Arriba'")
print(filtro3)
crearTabla(filtro3, "datosRioArribaLaSalazar")
print("\n")

# Creamos un gráfico de barras de la edad contra el nombre
fig, ax = plt.subplots()
# Define las ubicaciones de las barras y su ancho
bar_locations = np.arange(filtro3.shape[0])
bar_width = 0.5
# Dibuja las barras para cada variable, ajustando la ubicación para que no se superpongan

ax.bar(bar_locations, filtro3['Ciudad'], width=bar_width, label='Ciudad')

ax.bar(bar_locations, filtro3['Vereda'], width=bar_width, label='Vereda')
# Define las etiquetas del eje x usando las etiquetas de las filas del DataFrame
ax.set_xticks(bar_locations)
ax.set_xticklabels(filtro3.index)

ax.set_xlabel('Belmira')
ax.set_ylabel('Veredas')
ax.set_title('estadisticas Belmira')
ax.legend()
plt.show()



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

# Creamos un gráfico de barras de la edad contra el nombre
fig, ax = plt.subplots()
# Define las ubicaciones de las barras y su ancho
bar_locations = np.arange(mean.shape[0])
bar_width = 0.5
# Dibuja las barras para cada variable, ajustando la ubicación para que no se superpongan
ax.bar(bar_locations, mean['Ticket'], width=bar_width, label='Ticket')
ax.bar(bar_locations, mean['Arboles'], width=bar_width, label='Arboles')
ax.bar(bar_locations, mean['Hectareas'], width=bar_width, label='Hectareas')

# Define las etiquetas del eje x usando las etiquetas de las filas del DataFrame
ax.set_xticks(bar_locations)
ax.set_xticklabels(mean.index)



ax.set_title('Medias guevas')
ax.legend()
plt.show()


# FILTRO 5: Encontrar todos los datos de caramanta donde se tengan siembras
# de + de 100 arboles
print('Filtro 5')
print("\n")
filtro5 = tabla.query("Ciudad == 'Caramanta' and Arboles > 100")
print(filtro5)
crearTabla(filtro5, "datosCaramantaArboles")
print("\n")

# Creamos un gráfico de barras de la edad contra el nombre
fig, ax = plt.subplots()
# Define las ubicaciones de las barras y su ancho
bar_locations = np.arange(filtro5.shape[0])
bar_width = 0.5
# Dibuja las barras para cada variable, ajustando la ubicación para que no se superpongan
ax.bar(bar_locations, filtro5['Arboles'], width=bar_width, label='Arboles')
# Define las etiquetas del eje x usando las etiquetas de las filas del DataFrame
ax.set_xticks(bar_locations)
ax.set_xticklabels(filtro5.index)


ax.set_title('Caramanta mas de 100 ')
ax.legend()
plt.show()


# FILTRO 6: Encontrar los datos de la vereda mallarino del municipio de
# Yarumal
print('Filtro 6')
print("\n")
filtro6 = tabla.query("Ciudad == 'Yarumal' and Vereda == 'Mallarino'")
print(filtro6)
crearTabla(filtro6, "datosMallarino")
print("\n")


# Creamos un gráfico de barras de la edad contra el nombre
fig, ax = plt.subplots()
# Define las ubicaciones de las barras y su ancho
bar_locations = np.arange(filtro6.shape[0])
bar_width = 0.5
# Dibuja las barras para cada variable, ajustando la ubicación para que no se superpongan
ax.bar(bar_locations, filtro6['Ticket'], width=bar_width, label='Ticket')
ax.bar(bar_locations, filtro6['Nombre comun'], width=bar_width, label='Nombre comun')
ax.bar(bar_locations, filtro6['Fecha'], width=bar_width, label='Fecha')
ax.bar(bar_locations, filtro6['evento'], width=bar_width, label='evento')
ax.bar(bar_locations, filtro6['Ciudad'], width=bar_width, label='Ciudad')
ax.bar(bar_locations, filtro6['Vereda'], width=bar_width, label='Vereda')
ax.bar(bar_locations, filtro6['Arboles'], width=bar_width, label='Arboles')
ax.bar(bar_locations, filtro6['Hectareas'], width=bar_width, label='Hectareas')

# Define las etiquetas del eje x usando las etiquetas de las filas del DataFrame
ax.set_xticks(bar_locations)
ax.set_xticklabels(filtro6.index)



ax.set_title('Yarumal - Mallarino')
ax.legend()
plt.show()