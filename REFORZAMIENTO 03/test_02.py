"""2. Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la
función una vez y mostrar el resultado por consola). Los números
serán ingresados y solicitados al usuario."""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 >= num2:
    print("El primer número debe ser menor que el segundo número.")
def cuadrados(num1, num2):
    for i in range(num1 , num2+1):
        print(i ** 2)


print("Los cuadrados de los números entre {} y {} son:  ".format(num1,num2))
resultado = cuadrados(num1, num2)

