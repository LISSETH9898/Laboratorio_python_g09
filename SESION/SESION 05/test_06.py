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

carro_1 = Carro("Azul",70)

print("la velocidad inicial de mi carro 1 es: {}".format(carro_1.velocidad))

carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
print("la velocidad actual de mi carro 1 es: {}".format(carro_1.velocidad))

carro_1.frena()
carro_1.frena()
print("la velocidad actual de mi carro 1 es: {}".format(carro_1.velocidad))