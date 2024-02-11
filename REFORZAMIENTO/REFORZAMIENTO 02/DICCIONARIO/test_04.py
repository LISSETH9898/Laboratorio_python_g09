"""4. Elimina el key edad tipo de tu diccionario, incluyendo su valor.

del var[‘key’]"""

diccionario = {"nombre":"Lisseth", "edad": 25, "salario":1500, "edad_empleador" : 40}
diccionario["dni"] = 72026389


del diccionario["edad"]
print("mi diccionario actualizado es: {}".format(diccionario))