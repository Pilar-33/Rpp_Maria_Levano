
def validar_matriz_cuadrada(matriz: list):
    filas = len(matriz)
    for fila in matriz:
        if len(fila) != filas:
            return False
    return True

#1. Generar una función que calcule la media geométrica de filas o columnas de una matriz
#cuadrada.

def calcular_media_geometrica(matriz: list) -> float:
    """
    Calcula le media geométrica de la matriz.
    Recibe la matriz en la cual se va operar.
    Devuelve un número tipo float.
    """
    n = len(matriz)
    producto = 1
    for numero in matriz:
        producto *= numero
    rpta = producto ** (1 / n)
    return rpta

def calcular_media_filas_columnas(matriz: list, tipo: str) -> list:
    """
    Calcula la media geométrica de las filas o columnas de la matriz.
    Recibe la matriz en la cual se va operar y el tipo si es sobre
    las filas o columnas.
    Devuelve una lista con las medias geométricas de las filas o
    columnas."""
    
    medias_filas = []
    medias_columnas = []
    
    if tipo == "filas":
        for fila in matriz:
            media_fila = calcular_media_geometrica(fila)
            medias_filas += [media_fila]
        return medias_filas
    if tipo == "columnas":
        for i in range(len(matriz[0])):
            columna = []
            for j in range(len(matriz)):
                columna +=[matriz[j][i]]
            media_columna = calcular_media_geometrica(columna)
            medias_columnas += [media_columna]
        return medias_columnas
    

#Generar una función que calcule la suma de las diagonales principal y secundaria de una
#matriz

def calcular_suma(matriz: list, diagonal: str) -> None:
    """
    Calcula la suma de la diagonal principal o secundaria de 
    la matriz.
    Recibe la matriz y la diagonal con la que se va operar.
    Devuelve el resultado de la suma.
    """
    if not validar_matriz_cuadrada(matriz):
        return "La matriz no es cuadrada."
    
    suma_diagonal_principal = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                suma_diagonal_principal += matriz[i][j]


    suma_diagonal_secundaria = 0
    n = len(matriz)
    for j in range(n):
        suma_diagonal_secundaria += matriz[j][n - 1 - j]

    if diagonal == "principal":
        print(f"La suma de la diagonal {diagonal} es: {suma_diagonal_principal}")
    elif diagonal == "secundaria":
        print(f"La suma de la diagonal {diagonal} es: {suma_diagonal_secundaria}")
    elif diagonal == "ambas":
        print(f"La suma de la diagonal principal es: {suma_diagonal_principal}")
        print(f"La suma de la diagonal secundaria es: {suma_diagonal_secundaria}")
    
        
def devolver_transpuesta(matriz: list) -> None:
    """
    Realiza la tranzpuesta de una matriz.
    Recibe la matriz la cual va transponer.
    Devuelve la matriz transpuesta.
    """
    if not validar_matriz_cuadrada(matriz):
        return "La matriz no es cuadrada."
    
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            print(matriz[j][i], end = " ")
        print("")

                    
