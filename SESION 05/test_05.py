"""Programacion orientada a objeto en Python"""
"""Atributo"""


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

carro_1 = Carro("blanco",60)

print("el color de mi primer carro es: {}".format(carro_1.color))

carro_2 = Carro("rojo", 80)
carro_2.marchas =3000
print("el numero de marcha de mi segundo carro es:{}".format(carro_2.marchas))
#importante no es posible llmar un atributo de datos que se le ha asignado a otra instancia de la clase
#print(carro_1.marchas)