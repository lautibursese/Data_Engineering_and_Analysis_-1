import pandas as pd
from geopy.geocoders import Nominatim

class Preprocesamiento:
    '''
    Esta clase toma como argumento un DataFrame de Pandas
    '''
    def __init__(self, data:pd.DataFrame):
        self.data = data

    '''
    Busca por columna si hay valores nulos y los cambio por 'sin dato' o cero dependiendo el tipo de dato que contenga la columna
    '''
    def llenar_nulos(self):
        for i in self.data.columns:
            if self.data[i].dtype == 'object':
                self.data[i] = self.data[i].fillna('sin dato')

            elif self.data[i].dtype == 'float64':
                self.data[i] = self.data[i].fillna(0)
    
    '''
    Si hay datos nulos, toma la fecha de la columna anterior.
    '''
    def reemplazar_fechas_nulas(self, col_origen:str, col_destino:str):
        self.data[col_destino] = self.data[col_destino].fillna(self.data[col_origen].map(lambda x: x))
    
    '''
    Cambio las columnas con fechas a tipo de dato Fecha.
    '''
    def cambio_tipo_fecha(self, columna:str):
        self.data[columna] = pd.to_datetime(self.data[columna])
    
    '''
    Si la diferencia entre la fecha posterior a la anterior es negativa, entonces se intercambian.
    '''
    def intercambio_fechas(self, anterior:str, posterior:str):
        self.data.loc[(self.data[posterior]-self.data[anterior])/pd.Timedelta(days=1)<0, posterior] = self.data[anterior]

    
    '''
    DataFrame con la data limpia a un nuevo csv guardado en la carpeta 'clean_data'
    '''
    def clean_to_csv(self, csv):
<<<<<<< HEAD
        self.data.to_csv(f"../proyectoolist/clean_datasets/{csv}", index=False)
=======
        self.data.to_csv(f"../Proyecto_Final_OLIST/clean_datasets/{csv}", index=False)
>>>>>>> cb6f1f594834fad87333d2951b372292aeb952ca


    #kervin
    def reemplazo_str(self, columna:str):
        self.data[columna] = self.data[columna].str.replace("_", " ")
    
    def reemplazo_str_regex(self, columna:str):
        self.data[columna] = self.data[columna].str.replace("_", " ", regex=True)

    def drop_columna(self, columna:str):
        self.data.drop(columna, inplace=True, axis=1)

    #lautaro

    def unificar_criterio(self, columna:str, valor_viejo:str, valor_nuevo:str):
        self.data[columna] = self.data[columna].replace({valor_viejo}, valor_nuevo)

    def completar_nulos(self, columna:str, valor:str):
        self.data[columna].fillna(valor, inplace=True)

