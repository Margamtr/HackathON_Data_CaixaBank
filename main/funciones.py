
import pandas as pd
import requests
import numpy as np
print("hola mundo")

def llamar_api(url):
    llamada= requests.get(url)
    print(f'Respuesta de la llamada:{llamada.status_code}')
    if llamada.status_code !=200:
        print(f'Fallo llamada. Error:{llamada.reason}')
    else:
        return llamada.json()
    

def eda_basico (df):
    """
    Análisis exploratorio básico.
    Arg= dataframe
    Return: estructura, duplicados, valores nulos, información (series)
    """
    print(f'Muestra de datos:')
    print(df.sample(2))
    df.shape
    print(f'Columnas: {df.shape[1]}\nFilas: {df.shape[0]}')
    print(f'Valores duplicados:{df.duplicated().sum()}')
    print(f'Valores nulos encontrados:')
    print(df.isnull().sum())
    print('Información general:')
    print(df.info())


def limpieza_dollar(df,columna):
    df[columna]=df[columna].str.replace("$","")
    df[columna]=pd.to_numeric(df[columna], errors='coerce').fillna(9999).astype(np.int64)
    return df

def limpieza_dollar_to_float(df,columna):
    df[columna]=df[columna].str.replace("$","")
    df[columna]=df[columna.astype(float)]
    return df

def final_query(df, columna, query):
    df_query=pd.DataFrame(df[columna])
    df_query.to_csv(query,index=False)
    js_query=df_query.to_json(orient="columns", index=None)
    return js_query

def final_query(df, query):
    df_query=df.toPandas()
    df_query.to_csv(query,index=False)
    js_query=df_query.to_json(orient="records")
    return js_query