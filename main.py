from os import system
system("cls")

from ejercicio2.funciones import *

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [10, 8, 9]
]

# nro 1
"""fila_columna = "filas"
fila_columna1 = "columnas"
media_fila = calcular_media_filas_columnas(matriz, fila_columna)
print(f"Media geometrica {fila_columna} es: {media_fila}")

media_fila1 = calcular_media_filas_columnas(matriz, fila_columna1)
print(f"Media geometrica {fila_columna1} es: {media_fila1}")
"""
# nro 2
calcular_suma(matriz, "secundaria")
calcular_suma(matriz, "principal")

#nro 3
#devolver_transpuesta(matriz)

#nro 4
"""diagonal = input("Ingrese que diagonal desea sumar (principal, secundaria, ambas): ")
while diagonal != "principal" and diagonal != "secundaria" and diagonal != "ambas":
    print("Inválido!!!.")
    diagonal = input("Ingrese que diagonal desea sumar (principal, secundaria, ambas): ")

calcular_suma(matriz, diagonal)"""
    

