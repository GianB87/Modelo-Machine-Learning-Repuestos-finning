import os
import numpy as np
import pandas as pd
# Convierte archivos excel a csv
def exportar_csv(dataframe, folder, name,index=False):
    file_dir = os.path.join(os.getcwd(),'..')
    export_path = os.path.join(file_dir,folder)
    name_path = os.path.join(export_path,name + '.csv')
    dataframe.to_csv(name_path,index=index)
def exportar_excel(dataframe, folder, name,index=False):
    file_dir = os.path.join(os.getcwd(),'..')
    export_path = os.path.join(file_dir,folder)
    name_path = os.path.join(export_path,name + '.xlsx')
    dataframe.to_excel(name_path,index=index)

def addOSMadreIndex(df, dropOrden=False, index = True,ordenName = 'Orden', osMadreName = 'OSMadre',osFilter=[]):
    # Convierte a numerico
    df[ordenName] = pd.to_numeric(df[ordenName], errors='coerce')
    # con el errors=coerce, los textos se convierten en nan, el dropna funciona como filtro de textos
    df = df.dropna(subset=[ordenName]).reset_index(drop=True)
    # convierte decimales a enteros
    df[ordenName] = df[ordenName].astype('int64')
    
    # cambia el numero final de la os
    df[osMadreName] = ((df[ordenName] / 100).apply(np.floor)* 100).astype('int64')

    # Filtros adicionales
    if osFilter:
        df = df[df[osMadreName].isin(osFilter)]
    if index:
        df = df.set_index(osMadreName)

    if dropOrden:
        df = df.drop(columns=[ordenName])
    
    return df