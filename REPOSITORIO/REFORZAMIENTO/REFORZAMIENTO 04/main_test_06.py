"""6. Creando un archivo principal donde llamará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones.
- La primera función cargará una un número entero que pedirá al
usuario que ingrese por consola un valor.
- La segunda función solamente sumará dos valores.
- Desde el archivo principal importar al módulo y sumar dos valores
usando las funciones anteriormente creadas en el módulo"""

import operaciones_test_06

def datos():
    numero = operaciones_test_06.cargar_entero()

    if numero is None:
        return

    otro_numero = int(input("Ingrese otro número entero: "))

    resultado = operaciones_test_06.sumar(numero, otro_numero)
    print("La suma de los dos números es: {}".format(resultado))

if __name__ == "__main__":
    datos()
