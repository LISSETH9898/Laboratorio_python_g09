"""9. Crear una clase llamada círculo que contenga radio en su constructory
que contenga un método área que devuelva el área de un círculo.
Aplicar excepciones en caso no se ingrese un dato tipo numérico.
Crear adicionalmente un método que devuelva el perímetro del círculo.
Instanciar la clase respectivamente para dos diferentes radios.
Habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola."""

import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio**2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    @classmethod
    def ingresar_radio(cls):
        radio = float(input("Ingrese el radio del círculo: "))
        return cls(radio)

circulo1 = Circulo.ingresar_radio()
circulo2 = Circulo.ingresar_radio()

print("Área del círculo 1: {}".format(circulo1.area()))
print("Perímetro del círculo 1: {}".format(circulo1.perimetro()))
print("Área del círculo 2: {}".format(circulo2.area()))
print("Perímetro del círculo 2: {}".format(circulo2.perimetro()))
