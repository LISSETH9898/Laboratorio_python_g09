"""8. Ingresar el nombre de tu carrera dentro de los valores que tienes en tu diccionario ya creado.
➢ Mostrar en consola los valores de su variable final (ya sea diccionario o lista)."""

diccionario = {"departamento1": "Lima", "departamento2": "Huancayo", "departamento3": "Cajamarca","departamento4":
    "Arequipa","departamento5": "Puno", "departamento6": "Cusco"}

carrera = input("Ingresa el nombre de tu carrera: ")
diccionario["carrera"] = carrera

print(diccionario)