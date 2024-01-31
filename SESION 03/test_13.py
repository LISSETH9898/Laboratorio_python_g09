"""Usando las propiedades de cadenas o strings"""

"""Concatenacion"""


nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")

nombre_completo = input ("El nombre compelto es: "+nombre+' '+apellido)
print(nombre_completo)

nombre_completo_2 = input ("El nombre compelto  del usurio es: {} {} ".format(nombre,apellido))
print(nombre_completo_2)
