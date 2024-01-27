"""Diccionario en Python"""
"""del: eliminar un key y valor del diccionario"""

var_1 = {"nombre": "Margarita", "edad":27, "promedio":15}

""""para eliminar  valores de nuestro diccionario usamos a del delante de variables"""

del var_1 ["edad"]

print("mi actualizada es:{}".format(var_1))