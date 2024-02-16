""""1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad, saldo y de nacionalidad peruana (use el manejo de errores para el
tipo de dato) y un método para solicitar su nombre y edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo instanciar la clase 2 veces, mostrar por
pantalla dicha edad actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla este valor)"""

from datetime import datetime

class Persona:
    def __init__(self, nombre=None, edad=None, saldo=None, nacionalidad="Peruana"):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = nacionalidad

    def convertir_edad_a_entero(self):
        try:
            self.edad = int(self.edad)
        except ValueError:
            print("La edad debe ser un número entero.")
            return

    def solicitar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = input("Ingrese su edad: ")
        self.convertir_edad_a_entero()

    def cumpleaños(self):
        if self.edad is not None:
            self.edad += 1
            print("Feliz cumpleaños {}! Ahora tienes {} años.".format(self.nombre, self.edad))
        else:
            print("No se puede calcular el cumpleaños debido a un error en la edad.")

def obtener_fecha():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


persona1 = Persona()
persona1.solicitar_datos()
persona1.cumpleaños()

persona2 = Persona()
persona2.solicitar_datos()
persona2.cumpleaños()

print("Fecha de registro: {}".format(obtener_fecha()))

