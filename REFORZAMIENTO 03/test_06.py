"""6. Escribir una clase en Python que contenga un método que convierta un
número entero en su cubo y contenga otro método que obtenga el
cuadrado de ese resultado. El valor inicial de resultado deberá estar
creado en el constructor. Considerar un método en la cual le pedirá al
usuario ingresar un valor numérico."""

class Calculadora:
    def __init__(self):
        self.numero = None
        self.cubo = None
        self.cuadrado = None

    def datos(self):
        self.numero = int(input("Ingrese un numero: "))

    def cubo_numero(self):
        self.cubo = self.numero ** 3

    def cuadrado_del_cubo(self):
        self.cuadrado = self.cubo ** 2

calc = Calculadora()

calc.datos()
calc.cubo_numero()
calc.cuadrado_del_cubo()

resultado_cubo = calc.cubo
resultado_cuadrado = calc.cuadrado
numero_ingresado = calc.numero

print("El cubo de {} es: {}".format(numero_ingresado, resultado_cubo))
print("El cuadrado de {} es: {}".format(resultado_cubo, resultado_cuadrado))
