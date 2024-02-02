"""Reglas:
- Crear un diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Mostrar en pantalla sólo los values del diccionario
- Agregar un key adicional con el nombre de “profesion” y un valor para este key
nuevo.
- Eliminar el key dni y mostrar el nuevo diccionario."""




nom = input("Ingrese su nombre: ")
ape = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
dni = input("Ingrese su Dni: ")

diccionario = {"nombre": nom, "apellido":ape, "edad": edad, "dni":dni}

print("Los valores del diccionario son los siguientes: {}".format(list(diccionario.values())))

diccionario["profesion"]= input("Ingrese su profesion: ")
print("Los valores actualizado son: {}".format(list(diccionario.values())))

del diccionario["dni"]
print("Los valores actualizado son:{}".format(list(diccionario.values())))