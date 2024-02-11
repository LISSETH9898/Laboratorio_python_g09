"""Programacion orientada a objeto en Python"""

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

    """Instanciones de la class"""
carro_1 = Carro("negro",50)
print("el color del primer carro es:  {}".format(carro_1.color))
print("la aceleracion de mi primer carro es: {}".format(carro_1.aceleracion))
print("La cantidad de ruedas que tiene mi primer carro es: {}".format(carro_1.ruedas))



carro_2 = Carro("Azul",70)
print("el color del segundo carro es:  {}".format(carro_2.color))
print("la aceleracion de mi segundo carro es: {}".format(carro_2.aceleracion))
print("La cantidad de ruedas que tiene mi segundo carro es: {}".format(carro_2.ruedas))
