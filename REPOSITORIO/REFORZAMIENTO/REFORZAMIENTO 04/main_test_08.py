"""8. Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:

- Una función que realizará la carga de un valor entero.
- Una función que mostrará por pantalla la raíz cuadrada de dicho
valor
- Y otra función el valor elevado al cuadrado y al cubo de dicho
número.
- Utilizar el módulo math de python."""

import operaciones_test_08


def main():

    numero = operaciones_test_08.cargar_entero()

    if numero is None:
        return

    operaciones_test_08.mostrar_raiz_cuadrada(numero)

    operaciones_test_08.mostrar_cuadrado_cubo(numero)


if __name__ == "__main__":
    main()
