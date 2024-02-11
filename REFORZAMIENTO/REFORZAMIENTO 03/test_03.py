"""3. Crear una función que sume los dígitos del número ingresado y
muestre por consola la suma de estos dígitos."""

numero = int(input("Ingrese un número: "))
def sumar_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma

suma_digitos = sumar_digitos(numero)
print("La suma del numero {} es: {} ".format(numero,suma_digitos))

