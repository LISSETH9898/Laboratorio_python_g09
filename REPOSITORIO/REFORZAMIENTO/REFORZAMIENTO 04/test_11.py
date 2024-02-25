"""11. Crear una función que creará el archivo calificaciones.txt que contiene
las calificaciones de un curso.
Escribir un programa que contenga las siguientes funciones:
- Una función que guarde el nombre, 2 notas y el promedio (el
promedio lo calculará la función antes de escribirlo en el fichero)
- Y una función que leerá el fichero anterior y dirá si el alumno X,
aprobó o no, tener en cuenta que si tiene un promedio mayor a día
tendrá un mensaje de “Alumno X, aprobado” de lo contrario “Alumno
X, desaprobado”"""


def guardar_calificaciones(nombre_archivo):

    with open(nombre_archivo, "w") as file:

        while True:
            nombre = input("Ingrese el nombre del alumno (o 'fin' para terminar): ")
            if nombre.lower() == "fin":
                break

            nota1 = float(input("Ingrese la primera nota del alumno {}: ".format(nombre)))
            nota2 = float(input("Ingrese la segunda nota del alumno {}: ".format(nombre)))
            promedio = (nota1 + nota2) / 2


            file.write("{},{},{},{}\n".format(nombre, nota1, nota2, promedio))

    print("Se han guardado las calificaciones en el archivo", nombre_archivo)


def verificar_aprobacion(nombre_archivo, alumno):

    with open(nombre_archivo, "r") as file:
        for linea in file:
            datos = linea.strip().split(",")
            nombre = datos[0]
            promedio = float(datos[3])


            if nombre == alumno and promedio >= 6:
                print("Alumno {}, aprobado".format(alumno))
                return
        print("Alumno {}, desaprobado".format(alumno))



guardar_calificaciones("calificaciones.txt")


verificar_aprobacion("calificaciones.txt", "Juan")
