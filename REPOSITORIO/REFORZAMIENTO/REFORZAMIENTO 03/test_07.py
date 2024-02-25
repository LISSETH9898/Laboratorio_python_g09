"""7. Crear una clase en python que contenga un método que revierta una
cadena de palabras.
Input: "Hola Pythonista, seguimos adelante"
Output: "adelante seguimos Pythonista Hola"
Llamarlo mínimo 2 veces y mostrar el resultado por consola."""

class Reversor:
    def __init__(self):
        self.cadena = None
        self.revertida = None

    def dato(self):
        self.cadena = "Hola Pythonista, seguimos adelante"

    def revertir_cadena(self):
        palabras = self.cadena.split()
        palabras.reverse()
        self.revertida = ' '.join(palabras)

rev = Reversor()
rev.dato()
rev.revertir_cadena()

resultado_revertido = rev.revertida
print("Resultado: {}".format(resultado_revertido))

resultado_revertido = rev.revertida
print("Resultado: {}".format(resultado_revertido))