import pandas as pd
import numpy as np
import matplotlib.pyplot as ptl


from io import StringIO
import json
#import DataFrame

datos = pd.read_csv(r"/Users/Reyes/Desktop/Trainings/Python/GAP/datascience-project/ChicagoIllinois-RestaurantInspections.csv")

datos.drop_duplicates(subset = ('dba_name', 'address', 'zip' , 'inspection_date'), keep = "first", inplace = True)
datos.head()

# convert DATA FILTER IN JSON

myJSON = datos.to_json('temp.json', orient='records', lines=True)
print("MYJSON ",myJSON)
