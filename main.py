import pandas as pd

tabla = pd.read_csv("./data/Siembras.csv")

# FILTRO1: Encontrar todos los datos de santa fe de Antioquia donde se
# tengan siembras de + de 250 arboles
print('Filtro 1')
print("\n")
filtro1 = tabla.query("Ciudad == 'Santa Fe de Antioquia' and Arboles > 250")
print(filtro1)
print("\n")


# FILTRO2: Filtrar todos los datos de Caucasia e interpretar sus estadísticas
print('Filtro 2')
print("\n")
filtro2 = tabla.query("Ciudad == 'Caucasia'")
estadisticasFiltro2 = filtro2.describe()
print(filtro2)
print("\n")
print(estadisticasFiltro2)
print("\n")


# FILTRO 3: Filtrar todos los datos de las veredas Rio Arriba y La Salazar de Belmira
print('Filtro 3')
print("\n")
filtro3 = tabla.query(
    "Ciudad == 'Belmira' and Vereda == 'La Salazar' or Vereda == 'Rio Arriba'")
print(filtro3)
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
print("\n")


# FILTRO 5: Encontrar todos los datos de caramanta donde se tengan siembras
# de + de 100 arboles
print('Filtro 5')
print("\n")
filtro5 = tabla.query("Arboles > 100")
print(filtro5)
print("\n")


# FILTRO 6: Encontrar los datos de la vereda mallarino del municipio de
# Yarumal
print('Filtro 6')
print("\n")
filtro6 = tabla.query("Ciudad == 'Yarumal' and Vereda == 'Mallarino'")
print(filtro6)
print("\n")
