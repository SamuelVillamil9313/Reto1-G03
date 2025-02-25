import time

import csv

import pandas as pd

import os

from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as al
from DataStructures.Queue import queue as qu
from DataStructures.Stack import stack as st

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

csv.field_size_limit(2147483647)

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    
    catalog = {'source': None,
               'commodity': None,
               'statical_category': None,
               'unit_measurement': None,
               'state_name': None,
               'location': None,
               'year_collection': None,
               'freq_collection': None,
               'reference_period': None,
               'load_time': None,
               'value': None}

    catalog['source'] = al.new_list()
    catalog['commodity'] = al.new_list()
    catalog['statical_category'] = al.new_list()
    catalog['unit_measurement'] = al.new_list()
    catalog['state_name'] = al.new_list()
    catalog["location"] = al.new_list()
    catalog["year_collection"] = al.new_list()
    catalog["freq_collection"] = al.new_list()
    catalog["reference_period"] = al.new_list()
    catalog["load_time"] = al.new_list()
    catalog["value"] = al.new_list()
    return catalog

def dataframe():
    """
    Crea un dataframe a partir de los datos del archivo escogido para
    facilitar el acceso a los mismos, y poder cargarlos fácilmente a la 
    las listas.
    """
    
    frame=pd.read_csv(data_dir+"agricultural-20.csv")
    return frame

# Funciones para la carga de datos

def carga(dataframe,catalog,columna:str):
    for i in dataframe[columna]:
        al.add_last(catalog[columna],i)
    

def load_data(catalog, dataframe):
    """
    Carga los datos del DataFrame en el catálogo.
    """
    carga(dataframe, catalog, 'source')
    
    source_size = catalog["source"]["size"]
    
    carga(dataframe, catalog, 'commodity')
    carga(dataframe, catalog, 'statical_category')
    carga(dataframe, catalog, 'unit_measurement')
    carga(dataframe, catalog, 'state_name')
    carga(dataframe, catalog, 'location')
    carga(dataframe, catalog, 'year_collection')
    carga(dataframe, catalog, 'freq_collection')
    carga(dataframe, catalog, 'reference_period')
    carga(dataframe, catalog, 'load_time')
    carga(dataframe, catalog, 'value')
    
    return source_size

def lesser_year(catalog):
    año=catalog["year_collection"]["elements"][0]
    for i in catalog["year_collection"]["elements"]:
        if año > i:
            año=i
    return año

def greater_year(catalog):
    año=catalog["year_collection"]["elements"][0]
    for i in catalog["year_collection"]["elements"]:
        if año < i:
            año=i
    return año

def primeros(catalog):
    final=[]
    transitoria=[]
    info = {'source': None,
               'unit_measurement': None,
               'state_name': None,
               'year_collection': None,
                "freq_collection":None,
               'load_time': None,
               'value': None,}
    for indice in range(0,5):
        for llave in catalog:
            transitoria.append(catalog[llave]["elements"][indice])
        info["source"]=transitoria[0]
        info["unit_measurement"]=transitoria[3]
        info["state_name"]=transitoria[4]
        info["year_collection"]=transitoria[6]
        info["load_time"]=transitoria[9]
        info["value"]=transitoria[10]
        final.append(info)
        transitoria=[]
    return final

def ultimos(catalog):
    final=[]
    transitoria=[]
    info = {'source': None,
               'unit_measurement': None,
               'state_name': None,
               'year_collection': None,
               'load_time': None,
               'value': None,}
    for indice in range(-6,-1):
        for llave in catalog:
            transitoria.append(catalog[llave]["elements"][indice])
        info["source"]=transitoria[0]
        info["unit_measurement"]=transitoria[3]
        info["state_name"]=transitoria[4]
        info["year_collection"]=transitoria[6]
        info["load_time"]=transitoria[9]
        info["value"]=transitoria[10]
        final.append(info)
        transitoria=[]
    return final
# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog,anno):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    
    start_time=get_time()
    
    lista_fechas=[]
    info = {'source': None,
            'commodity': None,
               'unit_measurement': None,
               'state_name': None,
               'year_collection': None,
               'load_time': None,
               'value': None,}
    
    for i in range(catalog["year_collection"]["size"]):
        if catalog["year_collection"]["elements"][i] == int(anno):
            lista_fechas.append(catalog["load_time"]["elements"][i])
    
    pasaron=len(lista_fechas)
    ultima=max(lista_fechas)
    
    for k in range(catalog["load_time"]["size"]):
        if (str(ultima) == catalog["load_time"]["elements"][k]) and (int(anno)==catalog["year_collection"]["elements"][k]):
            info["source"]=catalog["source"]["elements"][k]
            info["commodity"]=catalog["commodity"]["elements"][k]
            info["unit_measurement"]=catalog["unit_measurement"]["elements"][k]
            info["state_name"]=catalog["state_name"]["elements"][k]
            info["year_collection"]=catalog["year_collection"]["elements"][k]
            info["load_time"]=catalog["load_time"]["elements"][k]
            info["value"]=catalog["value"]["elements"][k]
    
    end_time=get_time()
    
    req_1_time=delta_time(start_time,end_time)
    
    return(info,req_1_time,pasaron)
    
    
            
        
    


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
