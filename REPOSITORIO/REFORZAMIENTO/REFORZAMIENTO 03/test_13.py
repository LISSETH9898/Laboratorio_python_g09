"""13. Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase
Persona y agregue un atributo sueldo y muestre si debe pagar
impuestos (10% de su sueldo-encapsulamiento) (sueldo superior a
4000)
Instanciar la clase Empleado, mostrar el sueldo del empleado y cuánto
debe pagar de impuesto."""

class Persona:
    def __init__(self, nombre=None, edad=None):
        self.nombre = nombre
        self.edad = edad

    def ingresar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))

class Empleado(Persona):
    def __init__(self, nombre=None, edad=None, sueldo=None):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def ingresar_datos(self):
        super().ingresar_datos()
        self.sueldo = float(input("Ingrese su sueldo: "))

    def mostrar_impuesto(self):
        if self.sueldo > 4000:
            impuesto = self.sueldo * 0.10
            print("El impuesto es de: $ {} ".format(impuesto))
        else:
            print("Usted no paga impuesto")


empleado_1 = Empleado()
empleado_1.ingresar_datos()

print("El sueldo del empleado {} es: {}".format(empleado_1.nombre, empleado_1.sueldo))

empleado_1.mostrar_impuesto()
