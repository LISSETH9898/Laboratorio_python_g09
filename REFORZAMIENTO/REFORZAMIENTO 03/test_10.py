"""10. Crear una clase llamada Alumno que tenga como atributos el nombre,
edad y la nota final del alumno. Crear los métodos para inicializar sus
atributos, otro para imprimirlos y un método para mostrar un mensaje
con el resultado de la nota y si ha aprobado (mayor o igual a 11) o no el
alumno.Instanciar la clase por lo menos 3 veces (3 alumnos)"""


class Alumno:
    nombre = None
    edad = None
    nota_final = None

    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def imprimir_atributo(self):
        print("Nombre:".format(self.nombre))
        print("Edad:".format(self.edad))
        print("Nota Final:".format(self.nota_final))

    def mostrar_resultado(self):
        if self.nota_final >= 11:
            print("{} ha aprobado con una nota de {}.".format(self.nombre,self.nota_final))
        else:
            print("{} ha reprobado con una nota de {}.".format(self.nombre,self.nota_final))


alumno1 = Alumno("Lisseth", 25, 15)
alumno2 = Alumno("Miguel", 22, 13)
alumno3 = Alumno("Fanny", 21, 8)


print("Información del alumno 1:")
alumno1.imprimir_atributo()
alumno1.mostrar_resultado()
print()

print("Información del alumno 2:")
alumno2.imprimir_atributo()
alumno2.mostrar_resultado()
print()

print("Información del alumno 3:")
alumno3.imprimir_atributo()
alumno3.mostrar_resultado()
