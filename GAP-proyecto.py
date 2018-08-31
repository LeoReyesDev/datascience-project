import pandas
import numpy as np

datos = pandas.read_csv(r"C:\Users\esteb\Desktop\Proyecto GAP\ChicagoIllinois-Restaurants.csv")
nulos = datos.isnull()
cantidadDeNulos = datos.isnull().sum()