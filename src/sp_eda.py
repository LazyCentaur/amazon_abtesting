# Pandas tratamiento de datos
import pandas as pd

def eda_preliminar (df):
    
    """
    Realiza un análisis exploratorio preliminar sobre un DF dado.
    
    Este análisis incluye:
    - Muestra aleatoria de 5 filas del DF.
    - Información general del DF (tipos de datos, nulos, etc.)
    - Porcentaje de valores nulos por columna.
    - Conteo de filas duplicadas
    - Distribución de valores para columnas categóricas
    
    Parameters:
    df (pd.DataFrame): DataFrame a analizar
    
    Returns:
    None
    """
    
    display(df.sample(5))
    print('------------')
    print('DIMANSIONES')
    print(f'Nº de filas: {df.shape[0]}\nNº de columnas: {df.shape[1]}')
    
    print('------------')
    print('INFO')
    display(df.info())
    
    print('------------')
    print('PORCENTAJE NULOS')
    display(df.isnull().mean() * 100)
    
    print('------------')
    print('DUPLICADOS')
    display(df.duplicated().sum())
    
    print('------------')
    print('FRECUENCIA CATEGORICAS')
    for col in df.select_dtypes(include= 'string').columns:
        print(col.upper())
        print(df[col].value_counts())
        print('------------')
        
    print('------------')
    print('ESTADISTICOS NUMERICAS')
    display(df.describe().T)
