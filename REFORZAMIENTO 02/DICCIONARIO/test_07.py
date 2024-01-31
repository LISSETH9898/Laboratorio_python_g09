"""7. Crear un diccionario con 6 departamentos en el país.
➢ Borrar cualquier departamento (uno) usando la palabra reservada del.
➢ Comprobar que no existe este departamento borrado dentro del diccionario."""

diccionario = {"departamento1": "Lima", "departamento2": "Huancayo", "departamento3": "Cajamarca","departamento4":
    "Arequipa","departamento5": "Puno", "departamento6": "Cusco"}

del diccionario["departamento1"]
print("EL diccionario actualizado es: {}".format(diccionario))