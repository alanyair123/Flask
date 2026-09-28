def ingresarElementosLista(cantidad):
    """
    Crea una lista dinámica solicitando datos al usuario mediante consola.
    
    Autor: Alan Vera
    Fecha: 2026-09-03
    Modificaciones:
        2026-09-03 | Versión inicial

    Parámetros:
        cantidad (int): Número de elementos que se van a registrar.

    Retorna:
        list: Lista con los elementos ingresados por el usuario.
    """
    listaNueva = []
    print(f"Ingresando {cantidad} elementos a la lista")
    for i in range(cantidad):
        elemento = input(f"Ingrese el elemento {i+1}: ")
        listaNueva.append(elemento)
    return listaNueva


def ingresarElementosDiccionario(cantidad):
    """
    Crea un diccionario solicitando parejas de clave-valor al usuario.
    
    Autor: Alan Vera
    Fecha: 2026-09-03
    Modificaciones:
        2026-09-03 | Versión inicial

    Parámetros:
        cantidad (int): Número de pares clave-valor a ingresar.

    Retorna:
        dict: Diccionario con los datos estructurados.
    """
    diccionarioNuevo = {}
    print(f"\n Ingresando {cantidad} elementos al diccionario")
    for i in range(cantidad):
        clave = input(f"Ingrese la clave {i+1}: ")
        valor = input(f"Ingrese el valor para '{clave}': ")
        diccionarioNuevo[clave] = valor
    return diccionarioNuevo


def imprimirEstructuras(lista, diccionario):
    """
    Muestra en pantalla el contenido de la lista y el diccionario de forma limpia.
    
    Autor: Alan Vera
    Fecha: 2026-09-03
    Modificaciones:
        2026-09-03 | Versión inicial

    Parámetros:5
    
        lista (list): Lista de elementos a imprimir.
        diccionario (dict): Diccionario a imprimir.

    Retorna:
        None
    """
    print("\nElementos de la Lista")
    for elemento in lista:
        print(f"- {elemento}")
        
    print("\nElementos del Diccionario")
    for clave, valor in diccionario.items():
        print(f"- {clave}: {valor}")

miLista = ingresarElementosLista(3)
miDiccionario = ingresarElementosDiccionario(2)

imprimirEstructuras(miLista, miDiccionario)

print("\nVista cruda de las estructuras:")
print(miLista)
print(miDiccionario)
