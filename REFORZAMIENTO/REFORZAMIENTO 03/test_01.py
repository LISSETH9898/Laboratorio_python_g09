
""""Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los
números cuya sumatoria de dígitos es menor que 10. Utilizar una o
más funciones, según sea conveniente."""


num1 = int(input("Ingrese el primer número positivo: "))
num2 = int(input("Ingrese el segundo número positivo: "))

if num1 <= 0 or num2 <= 0:
    print("Tiene que ingresar un numero positivo.")
else:
    def suma_digitos(numero):
        return sum(int(digito) for digito in str(numero))

    suma_num1 = suma_digitos(num1)
    suma_num2 = suma_digitos(num2)

    print("La suma de dígitos del primer número es: {}".format(suma_num1))
    print("La suma de dígitos del segundo número es: {}".format(suma_num2))

    if suma_num1 > suma_num2:
        print("El número {} es mayor en sumatoria de dígitos.".format(num1))
    elif suma_num2 > suma_num1:
        print("El número {} es mayor en sumatoria de dígitos.".format(num2))
    else:
        print("Ambos números tienen la misma sumatoria de dígitos.")

    print("Los números cuya sumatoria de dígitos es menor que 10 son los siguientes:")
    if suma_num1 < 10:
        print("Primer número {} ".format(num1))
    if suma_num2 < 10:
        print("Segundo número {} ".format(num2))
