"""
Requesitos:
-Dentro de una empresa se va a solicitar pedir nombre y apellido de empleado.
-Distrito de residencia
-Sueldo y calculo del bono final año, que sera el triple del sueldo mensual, menos el 10 porciento
-Todos estos datos van a ingresar a una lista
-Por asignacion multiple de variables asignar los valores de esta lista
-Mostrar por la terminal el mensaje de "Nombre' 'apellido' recibira 'bono' soles los valores

"""

var1 = input("Ingrese el nombre del empleado: ")
var2 = input("Ingrese el apellido del empleado: ")
var3 = input("Ingrese el distrito de residencia del empleado: ")
var4 = int(input("Ingrese el sueldo mensual del empleado: "))


bono = (var4 * 3 ) * 0.9


milista = [var1, var2,var3,var4,bono]


nombre, apellido, residencia, sueldo, bono = milista

print ("{} {} recibira {} soles de bono fin de año".format(nombre,apellido,bono))