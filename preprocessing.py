import pandas as pd

class Preprocessing:
    '''
    This class take as value a Pandas Dataframe.
    '''
    def __init__(self, data:pd.DataFrame):
        self.data = data

    '''
    Look for null values and fill them with 'sin dato' or 0 depending the data type they contain in every column.
    '''
    def fill_nulls(self):
        for i in self.data.columns:
            if self.data[i].dtype == 'object':
                self.data[i] = self.data[i].fillna('sin dato')

            elif self.data[i].dtype == 'float64':
                self.data[i] = self.data[i].fillna(0)
    
    '''
    If there are null values, it gets the previous column data.
    '''
    def replace_null_dates(self, col_origin:str, col_destination:str):
        self.data[col_destination] = self.data[col_destination].fillna(self.data[col_origin].map(lambda x: x))
    
    '''
    Change the date columns with date format type
    '''
    def change_type_date(self, column:str):
        self.data[column] = pd.to_datetime(self.data[column])
    
    '''
    If the difference between the later date and the previous date is negative, then they swap.
    '''
    def swap_dates(self, previous:str, later:str):
        self.data.loc[(self.data[later]-self.data[previous])/pd.Timedelta(days=1)<0, later] = self.data[previous]

    
    '''
    Clean Dataframe to a new .csv file in the folder 'clean_datasets'
    '''
    def clean_to_csv(self, csv):
        self.data.to_csv(f"C:/Users/Predator/Desktop/Lauti/Programación/GitHub/2. Data Analytics/#2/clean_datasets/{csv}", index=False)

    def replace_str(self, column:str):
        self.data[column] = self.data[column].str.replace("_", " ")
    
    def replace_str_regex(self, column:str):
        self.data[column] = self.data[column].str.replace("_", " ", regex=True)

    def drop_column(self, column:str):
        self.data.drop(column, inplace=True, axis=1)

    def criteria_unification(self, column:str, valor_viejo:str, valor_nuevo:str):
        self.data[column] = self.data[column].replace({valor_viejo}, valor_nuevo)

    def fill_some_values(self, column:str, valor:str):
        self.data[column].fillna(valor, inplace=True)

