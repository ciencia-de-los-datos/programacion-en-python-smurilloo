"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.
.\tests.py '01'


"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    import csv
    archivo_csv = 'data.csv'
    suma_segunda_columna = 0

    with open(archivo_csv, mode='r', newline='') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')  # Establece el delimitador como '\t' para el CSV con tabulaciones
    
        # Lee cada fila del archivo CSV
        for fila in lector_csv:
            if len(fila) > 1:
                try:
                    valor_segunda_columna = int(fila[1])
                    suma_segunda_columna += valor_segunda_columna
                except ValueError:
                    pass  # Ignora las filas que no contienen números en la segunda columna

    return suma_segunda_columna

    

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como una lista de tuplas (letra, cantidad), ordenadas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14)
    ]
    """
    import csv
    archivo_csv = 'data.csv'
    contador_letras = {}

    with open(archivo_csv, mode='r', newline='') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
    
        for fila in lector_csv:
            if fila and len(fila) >= 1:
                primera_columna = fila[0]
                if primera_columna.isalpha():
                    primera_letra = primera_columna[0].upper()  # Tomar la primera letra y convertirla a mayúscula
                    contador_letras[primera_letra] = contador_letras.get(primera_letra, 0) + 1

    # Crear una lista de tuplas con el formato deseado
    lista_letras_cantidad = [(letra, cantidad) for letra, cantidad in contador_letras.items()]

    # Ordenar la lista alfabéticamente
    lista_letras_cantidad.sort()

    return lista_letras_cantidad




def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    import csv
    archivo_csv = 'data.csv'
    suma_por_letra = {}

    with open(archivo_csv, mode='r', newline='') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
    
        for fila in lector_csv:
            if fila and len(fila) >= 1:
                primera_columna = fila[0]
                segunda_columna = fila[1]
                if primera_columna.isalpha():
                    primera_letra = primera_columna[0].upper()  # Tomar la primera letra y convertirla a mayúscula
                    valor_segunda_columna = int(segunda_columna) if segunda_columna.isdigit() else 0
                    suma_por_letra[primera_letra] = suma_por_letra.get(primera_letra, 0) + valor_segunda_columna

    # Crear una lista de tuplas con el formato deseado
    lista_letras_suma = [(letra, suma) for letra, suma in suma_por_letra.items()]

    # Ordenar la lista alfabéticamente
    lista_letras_suma.sort()

    return lista_letras_suma


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    import csv
    archivo_csv = 'data.csv'
    registros_por_mes = {}

    with open(archivo_csv, mode='r', newline='') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
    
        for fila in lector_csv:
            if fila and len(fila) >= 1:
                tercera_columna = fila[2]  # La tercera columna contiene la fecha
                # Extraer el mes de la fecha (asumiendo que siempre está en formato 'YYYY-MM-DD')
                mes = tercera_columna.split('-')[1]
                if mes in registros_por_mes:
                    registros_por_mes[mes] += 1
                else:
                    registros_por_mes[mes] = 1

    # Crear una lista de tuplas con el formato deseado
    lista_meses_cantidad = [(mes, cantidad) for mes, cantidad in registros_por_mes.items()]

    # Ordenar la lista alfabéticamente por mes (año no se tiene en cuenta)
    lista_meses_cantidad.sort()

    return lista_meses_cantidad




def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    import csv
    archivo_csv = 'data.csv'
    max_min_por_letra = {}

    with open(archivo_csv, mode='r', newline='') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
    
        for fila in lector_csv:
            if fila and len(fila) >= 1:
                primera_columna = fila[0]
                segunda_columna = int(fila[1]) if fila[1].isdigit() else 0
                
                if primera_columna in max_min_por_letra:
                    max_valor, min_valor = max_min_por_letra[primera_columna]
                    max_valor = max(max_valor, segunda_columna)
                    min_valor = min(min_valor, segunda_columna)
                    max_min_por_letra[primera_columna] = (max_valor, min_valor)
                else:
                    max_min_por_letra[primera_columna] = (segunda_columna, segunda_columna)

    # Crear una lista de tuplas con el formato deseado
    lista_max_min_letra = [(letra, max_valor, min_valor) for letra, (max_valor, min_valor) in max_min_por_letra.items()]
    lista_max_min_letra.sort()
    return lista_max_min_letra



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import csv
    archivo_csv = 'data.csv'
    min_max_por_clave = {}

    with open(archivo_csv, mode='r', newline='') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')
    
        for fila in lector_csv:
            if fila and len(fila) >= 1:
                quinta_columna = fila[4]  # La quinta columna contiene el diccionario
                # Dividir el diccionario en pares clave:valor
                pares = quinta_columna.split(',')
                for par in pares:
                    clave, valor = par.split(':')
                    clave = clave.strip()  # Eliminar espacios en blanco alrededor de la clave
                    valor = int(valor) if valor.isdigit() else 0
                    if clave in min_max_por_clave:
                        min_valor, max_valor = min_max_por_clave[clave]
                        min_valor = min(min_valor, valor)
                        max_valor = max(max_valor, valor)
                        min_max_por_clave[clave] = (min_valor, max_valor)
                    else:
                        min_max_por_clave[clave] = (valor, valor)

    # Crear una lista de tuplas con el formato deseado
    lista_min_max_clave = [(clave, min_valor, max_valor) for clave, (min_valor, max_valor) in min_max_por_clave.items()]
    lista_min_max_clave.sort()

    return lista_min_max_clave



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    
    import csv
    archivo_csv = 'data.csv'
    asociaciones = {}

    with open('data.csv', mode='r', newline='') as archivo:
        # Utilizar un lector CSV con delimitador '\t'
        lector_csv = csv.reader(archivo, delimiter='\t')

        for fila in lector_csv:
            if len(fila) >= 1:
                valor_columna_2 = int(fila[1]) if fila[1].isdigit() else None
                letra_columna_1 = fila[0]

                if valor_columna_2 is not None:
                    # Verificar si el valor ya existe en el diccionario
                    if valor_columna_2 in asociaciones:
                        asociaciones[valor_columna_2].append(letra_columna_1)
                    else:
                        asociaciones[valor_columna_2] = [letra_columna_1]

    # Crear una lista de tuplas con el formato deseado
    lista_asociaciones = [(valor, letras) for valor, letras in asociaciones.items()]
    lista_asociaciones.sort()
    return lista_asociaciones


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    import csv
    asociaciones = {}

    # Leer el archivo CSV y procesar las filas
    with open('data.csv', mode='r', newline='') as archivo:
        # Utilizar un lector CSV con delimitador '\t'
        lector_csv = csv.reader(archivo, delimiter='\t')

        for fila in lector_csv:
            if len(fila) >= 1:
                valor_columna_2 = int(fila[1]) if fila[1].isdigit() else None
                letra_columna_1 = fila[0]

                if valor_columna_2 is not None:
                    # Verificar si el valor ya existe en el diccionario
                    if valor_columna_2 in asociaciones:
                        if letra_columna_1 not in asociaciones[valor_columna_2]:
                            asociaciones[valor_columna_2].append(letra_columna_1)
                    else:
                        asociaciones[valor_columna_2] = [letra_columna_1]

    # Crear una lista de tuplas con el formato deseado
    lista_asociaciones = [(valor, sorted(list(set(asociaciones.get(valor, [])))) if valor in asociaciones else []) for valor in range(10)]

    return lista_asociaciones


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import csv
    conteo_claves = {}

    # Leer el archivo CSV y procesar las filas
    with open('data.csv', mode='r', newline='') as archivo:
        # Utilizar un lector CSV con delimitador '\t'
        lector_csv = csv.reader(archivo, delimiter='\t')

        for fila in lector_csv:
            if len(fila) >= 1:
                quinta_columna = fila[4]
                # Dividir el diccionario en pares clave:valor
                pares = quinta_columna.split(',')
                for par in pares:
                    clave, _ = par.split(':')
                    clave = clave.strip()  # Eliminar espacios en blanco alrededor de la clave
                    if clave in conteo_claves:
                        conteo_claves[clave] += 1
                    else:
                        conteo_claves[clave] = 1

    # Ordenar el diccionario por claves alfabéticamente
    conteo_claves_ordenado = {k: v for k, v in sorted(conteo_claves.items())}

    return conteo_claves_ordenado



def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    import csv
    archivo_csv = 'data.csv'
    cantidad_elementos_por_letra = []

    with open(archivo_csv, mode='r', newline='') as archivo:
        lector_csv = csv.reader(archivo, delimiter='\t')

        for fila in lector_csv:
            if len(fila) >= 1:
                letra_columna_1 = fila[0]
                columna_4 = fila[3] if len(fila) > 3 else ''
                columna_5 = fila[4] if len(fila) > 4 else ''

                cantidad_columna_4 = len(columna_4.split(','))
                cantidad_columna_5 = len(columna_5.split(','))

                cantidad_elementos_por_letra.append((letra_columna_1, cantidad_columna_4, cantidad_columna_5))

    return cantidad_elementos_por_letra



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    import csv
    suma_por_letra = {}

    # Leer el archivo CSV y procesar las filas
    with open('data.csv', mode='r', newline='') as archivo:
        # Utilizar un lector CSV con delimitador '\t'
        lector_csv = csv.reader(archivo, delimiter='\t')

        for fila in lector_csv:
            if len(fila) >= 1:
                segunda_columna = int(fila[1]) if fila[1].isdigit() else 0
                cuarta_columna = fila[3]

                # Dividir la cuarta columna en letras
                letras = cuarta_columna.split(',')
                for letra in letras:
                    letra = letra.strip()  # Eliminar espacios en blanco
                    if letra in suma_por_letra:
                        suma_por_letra[letra] += segunda_columna
                    else:
                        suma_por_letra[letra] = segunda_columna

    # Ordenar el diccionario por claves alfabéticamente
    resultado_final = {letra: suma_por_letra[letra] for letra in sorted(suma_por_letra)}

    return resultado_final


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import csv
    suma_por_letra = {}

    # Leer el archivo CSV y procesar las filas
    with open('data.csv', mode='r', newline='') as archivo:
        # Utilizar un lector CSV con delimitador '\t'
        lector_csv = csv.reader(archivo, delimiter='\t')

        for fila in lector_csv:
            if len(fila) >= 1:
                letra_columna1 = fila[0].strip()  # Obtener el valor de la columna 1 y quitar espacios en blanco
                quinta_columna = fila[4]

                # Dividir la quinta columna en pares clave:valor
                pares = quinta_columna.split(',')
                for par in pares:
                    clave, valor_str = par.split(':')
                    clave = clave.strip()  # Eliminar espacios en blanco alrededor de la clave
                    valor = int(valor_str) if valor_str.isdigit() else 0
                    if letra_columna1 in suma_por_letra:
                        suma_por_letra[letra_columna1] += valor
                    else:
                        suma_por_letra[letra_columna1] = valor

    # Ordenar el diccionario por claves alfabéticamente
    resultado_final = {letra: suma_por_letra[letra] for letra in sorted(suma_por_letra)}

    return resultado_final



