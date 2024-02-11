"""USANDO LAS PROPIEDADES DE CADENAS A STRINGS"""

"""METODOS DE STRING"""

cadena = "Python para la prediccion de fraudes"

cadena_sin_espacios = cadena.split()
print("Cadena separados por espacion en blanco dentro del string:{}".format(cadena_sin_espacios))

for palabra in cadena_sin_espacios:
    print(palabra)