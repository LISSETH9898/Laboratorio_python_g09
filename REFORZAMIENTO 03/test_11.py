"""11. Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una
persona. Implementar los métodos necesarios para inicializar los
atributos (constructor), un método para mostrar los datos e indicar si
la persona es mayor de edad o no y otro método que bonificación que
retornará el 20% adicional de su sueldo.
Instanciar por lo menos la clase con 2 diferentes personas."""

class Persona:
    nombre = None
    edad = None
    sueldo = None

    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def mostrar_datos(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))
        print("Sueldo: {}".format(self.sueldo))

    def mostrar_si_es_mayor_de_edad(self):
        if self.edad >= 18:
            print("{} es mayor de edad".format(self.nombre))
        else:
            print("{} es menor de edad".format(self.nombre))

    def bonificacion(self):
        if self.sueldo >= 1025:
            bonificacion = self.sueldo * 0.20
            sueldo_con_bonificacion = self.sueldo + bonificacion
            print("Usted {} tiene un sueldo de {} por lo tanto recibe una bonificacion de: {}".format(self.nombre,self.sueldo,bonificacion))
            print("Sueldo con bonificación: {}".format(sueldo_con_bonificacion))
        else:
            print("Usted {} tiene un sueldo de {} por lo tanto no recibe una bonificacion.".format(self.nombre, self.sueldo))


persona1 = Persona("Lisseth", 25, 3000)
persona2 = Persona("Miguel", 17, 1000)

print("Datos de la primera persona: ")
persona1.mostrar_datos()
persona1.mostrar_si_es_mayor_de_edad()
persona1.bonificacion()
print()

print("Datos de la segunda persona: ")
persona2.mostrar_datos()
persona2.mostrar_si_es_mayor_de_edad()
persona2.bonificacion()

