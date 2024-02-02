"""Programacion funcional con Python"""

var_1 = 50
var_2 =  120

"""Input: dos variables que pasaran por parametros de la funcion"""
"""a, b: son parametros de la funcion "suma" """


def sumar(a, b):
    return a + b

#def sumar (a, b):
#    suma = a + b
#    return suma

resultado = sumar(var_1 , var_2)

"""Output: lo que retorna a funcion"""
print(resultado)

resultado_2 = sumar(90.7,150.89)
print(resultado_2)
