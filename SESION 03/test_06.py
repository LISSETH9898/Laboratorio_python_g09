"""Uso del flujo condicional: if"""

var_1= int(input("Ingrese su primer dato numerico: "))
var_2= int(input("Ingrese su segundo dato numerico: "))


if var_1 > var_2:
    print("El valor de var_1 es amyor que el segundo valor ingresado")
elif var_1 == var_2:
    print("Los valores ingresados son iguales")
else:
    print("El valor de la var_1 no es mayor que la var_2")