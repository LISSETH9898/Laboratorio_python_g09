
import os
import funciones

def crear_notas_txt():
    if not os.path.exists("notas.txt"):
        with open("notas.txt", "w") as archivo:
            archivo.write("Archivo 'notas.txt' creado.\n")
    else:
        print("El archivo 'notas.txt' ya existe.")

def main():
    crear_notas_txt()

    tamaño = int(input("Ingrese el tamaño de la lista: "))
    lista = funciones.generar_lista(tamaño)
    funciones.escribir_lista_en_archivo(lista)

    raices = funciones.calcular_raices(lista)
    funciones.escribir_raices_en_archivo(raices)

    print("Operaciones completadas. Revise el archivo 'notas.txt'.")

if __name__ == "__main__":
    main()


