"""4. Pedir al usuario que ingrese una oración con un mínimo de 3 palabras
la cual será usada por parámetro para una función que se creará e
indicará cuantas palabras existen dentro de la oración ingresada."""

oracion = input("Ingrese una oración con un mínimo de tres palabras: ")

def oraciones(oracion):
    if len(oracion.split()) < 3:
        print("La oración debe tener un mínimo de tres palabras.")
        return None
    else:
        return oracion

def contar_palabras(oracion):
    palabras = oracion.split()
    return len(palabras)

resultado_oracion = oraciones(oracion)

if resultado_oracion:
    cantidad_palabras = contar_palabras(resultado_oracion)
    print("La oración: ( {} ) tiene {} palabras.".format(resultado_oracion, cantidad_palabras))
