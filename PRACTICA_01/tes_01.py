"""1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (3 ptos)
Reglas:
- Pedir por consola nombre y edad de un usuario.
- Edad tiene que ser tipo entero, para esto apoyarse de la conversión de datos
- Identificar los tipos de datos ingresados y mostrarlos en pantalla.
- Pedir los nombres y edades para dos trabajadores y finalmente
agregarlos a una lista. Mostrar la suma de las edades de los
trabajadores localizándolos por la posición en la lista."""



nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))


print("Tipo de dato de {} es: {}".format(nombre, (type(nombre))))
print("Tipo de dato de {} es: {}".format(edad, (type(edad))))


trabajador1_nombre = input("Ingrese el nombre del primer trabajador: ")
trabajador1_edad = int(input("Ingrese la edad del primer trabajador: "))

trabajador2_nombre = input("Ingrese el nombre del segundo trabajador: ")
trabajador2_edad = int(input("Ingrese la edad del segundo trabajador: "))


lista = [trabajador1_nombre, trabajador1_edad, trabajador2_nombre, trabajador2_edad]


suma = lista[1] + lista[3]
print("La edad del trabajador_1 es: {}".format(lista[1]))
print("La edad del trabajador_2 es: {}".format(lista[3]))
print("La suma de las edades de los trabajadores es: {}".format(suma))