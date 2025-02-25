import sys

import App.logic as log

import os
default_limit=1000

sys.setrecursionlimit(default_limit*10)

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    catalog=log.new_logic()
    return catalog

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    frame=log.dataframe()
    size=log.load_data(control,frame)
    
    ult=log.greater_year(control)
    prim=log.lesser_year(control)
    
    first=log.primeros(control)
    last=log.ultimos(control)
    
    print("Número de registros: ", size)
    print("Último año de registro: ", ult)
    print("Primer año de registro reportado: ", prim)
    print("Primeros 5 registros cargados: ")
    print("...")
    print(first)
    print("...")
    print("Últimos 5 registros cargados: ")
    print("...")
    print(last)
    
    return control


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    
    anno=input("Inserte año de interés: ")
    datos=log.req_1(control,anno)
    print("El último registro de ese año es: ",datos[0])
    print("Un total de: ", datos[2], " registros pasaron el filtro por año.")
    print("La acción tomó: ", datos[1], "ms")


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    
    anno_i=input("Inserte año de inicio: ")
    anno_f=input("Inserte año final: ")
    nombre=input("inserte nombre de departamento/estado: ")
    datos=log.req_3(control,nombre,anno_i,anno_f)
    
    print("Listado de registros: ", datos[0])
    print("...")
    print("Un total de: ", datos[3], " registros pasaron el filtro por año.")
    print("...")
    print("Total de registros con origen SURVEY: ",datos[1])
    print("Total de registros con origen CENSUS: ",datos[2])
    print("...")
    print("La acción tomo: ", datos[4],"ms")


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    anno_i=input("Inserte año de inicio: ")
    anno_f=input("Inserte año final: ")
    product=input("inserte nombre de departamento/estado: ")
    datos=log.req_4(control,product,anno_i,anno_f)
    
    print("Listado de registros: ", datos[0])
    print("...")
    print("Un total de: ", datos[3], " registros pasaron el filtro por año.")
    print("...")
    print("Total de registros con origen SURVEY: ",datos[1])
    print("Total de registros con origen CENSUS: ",datos[2])
    print("...")
    print("La acción tomo: ", datos[4],"ms")


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
