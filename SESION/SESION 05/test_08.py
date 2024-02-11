"""Programacion orientada a objeto en Python"""
"""Clase y metodos"""


class Carro:
    """Atributos"""
    ruedas = 4


    """Constructor"""

    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion =aceleracion
        self.velocidad = 0


    """Metodo: son las funciones de la class"""
    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion


    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0

        self.velocidad = velocidad

"""AÑADIENDO HERENCIA"""
"""creamos nuestra class hija"""

class CarroVolador():

    rueda = 6

    def __init__(self, color, aceleracion, estado_volante = False ):
       super().__init__(color,aceleracion)
            #self.estadoVolando = estado_volante

    def Vuela (self):
        self.estadoVolando = True

    def aterriza (self):
        self.estadoVolando = False

carro_1 = Carro("ROJO",45)
carro_volador =CarroVolador("Blanco",55)

print("el color del carro es :{}".format(carro_volador.color))
print("el estado inicial de mi carro es: {}".format(carro_volador.estadoVolando))