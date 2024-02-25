
"""9. Crear una función que pida al usuario un número entero entre 1 y 20 y
guarde en un fichero (que no existe) con el nombre tabla.txt la tabla
de multiplicar de ese número, done n es el número introducido."""
def generar_tabla_multiplicar():

    while True:
        try:
            numero = int(input("Ingrese un número entero entre 1 y 20: "))
            if 1 <= numero <= 20:
                break
            else:
                print("Por favor, ingrese un número válido entre 1 y 20.")
        except ValueError:
            print("Error: Por favor, ingrese un número entero.")


    tabla = [f"{numero} x {i} = {numero*i}" for i in range(1, 11)]


    with open("tabla.txt", "w") as file:
        file.write("\n".join(tabla))

    print(f"La tabla de multiplicar del número {numero} se ha guardado en tabla.txt")


generar_tabla_multiplicar()
