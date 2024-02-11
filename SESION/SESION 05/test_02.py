"""Programacion funcional en Python"""

def encontrar_mayor_y_cubo(num1, num2, num3, num4):
    numeros = [num1, num2, num3, num4]
    mayor = max(numeros)
    cubo_del_mayor = mayor ** 3
    return mayor, cubo_del_mayor

def datos():

    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 =int(input("Ingrese el tercer número: "))
    num4 = int(input("Ingrese el cuarto número: "))


    mayor, cubo_del_mayor = encontrar_mayor_y_cubo(num1, num2, num3, num4)


    print("El número más grande es:", mayor)
    print("El cubo del número más grande es:", cubo_del_mayor)

if __name__ == "__main__":
    datos()

