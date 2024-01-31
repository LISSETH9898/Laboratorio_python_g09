"""2. Convierte tu diccionario a una lista y mostrar el tipo de datos final convertido en consola."""
"diccioanrio original"

diccionario = {"nombre":"Lisseth", "edad": 25, "salario":1500, "edad_empleador" : 40}


var_2 = list(diccionario.items())
print("mi diccioanrio convertido es el siguiente: {}".format(diccionario))

print("Tipo de datos después de la conversión: {}".format(type(diccionario)))

