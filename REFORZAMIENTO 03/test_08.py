"""8. Crear una clase que contenga dos métodos, uno que pida ingresar un
nombre y apellido, un método para pedir su edad y otro método que lo
imprima ambos resultados, pero estarán contenidos en un diccionario.
Comprobar ambos métodos instanciado la clase respectivamente.
Considerar en el constructor los valores necesarios."""

class Datos:
    def __init__(self):
        self.nombre = None
        self.apellido = None
        self.edad = None
        self.diccionario = None

    def ingresar_dato(self):
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")

    def ingresar_edad(self):
        self.edad = int(input("Ingrese su edad: "))

    def imprimir(self):
        self.diccionario = {"nombre": self.nombre, "apellido": self.apellido, "edad": self.edad}
        print("Mi diccionario tiene los siguientes datos: {}".format(self.diccionario))

persona = Datos()
persona.ingresar_dato()
persona.ingresar_edad()
persona.imprimir()
