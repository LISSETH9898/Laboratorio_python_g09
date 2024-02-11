"""14. Crear un módulo y un archivo principal (donde llamará las funciones del
módulo) el módulo tendrá una función para ingresar nombres y
apellidos, una función para pedir el tipo de seguro que tiene y otra
función para indicar si es mayor de edad o no (pedir la edad desde
consola)"""

class Seguro:
    def __init__(self, nombre=None, edad=None):
        self.nombre = nombre
        self.edad = edad

    def ingresar_nombre_apellido(self):
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")

    def pedir_tipo_seguro(self):
        tipo_seguro = input("Ingrese el tipo de seguro que tiene: ")
        return tipo_seguro

    def es_mayor_de_edad(self):
        edad = int(input("Ingrese su edad: "))
        if edad >= 18:
            print("Es mayor de edad.")
        else:
            print("No es mayor de edad.")

persona_1 = Seguro()
persona_1.ingresar_nombre_apellido()
persona_1.edad = int(input("Ingrese su edad: "))
seguro = persona_1.pedir_tipo_seguro()

print("Usted {} tiene {} años y tiene un seguro de vida de tipo {}".format(persona_1.nombre, persona_1.edad, seguro))
