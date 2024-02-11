"""Usando las propiedades de cadenas o strings"""

usuario = input("ingres su nombre: ")
apellido = input("ingres su apellido: ")

nombre_completo = usuario + "" + apellido
print(nombre_completo)


print("mi nombre  a mayusculas es: {}".format(nombre_completo.upper()))

final = "el tamaño del nombre es mayor al apellido" if len(usuario) > len(apellido) else "el tamaño del nombre no es mayor al apellido"
print(final)