import pandas as pd

def minus (df):
    """
    Reemplaza las columnas categóricas a minúsculas
    Args:
        df (DataFrame): DataFrame a modificar
    """
    for col in df.select_dtypes(include='string').columns:
        df[col] = df[col].str.lower()  
        
def comas (df):
    """
    Reemplaza ',' por '.' y si puede convierte a float
    Args:
        df (DataFrame): DataFrame a modificar
    """
    for col in df.select_dtypes(include='string').columns:
        df[col] = df[col].str.replace(',', '.')
        try:
            df[col] = df[col].astype('float64')
        except:
            pass
    
def espacios (df):
    """
    Reemplaza ' ' por '_' en las columnas categóricas
    Args:
        df (DataFrame): DataFrame a modificar
    """
    for col in df.select_dtypes(include='string').columns:
        df[col] = df[col].str.replace(' ', '_')     