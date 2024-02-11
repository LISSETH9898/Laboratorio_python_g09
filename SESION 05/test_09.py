

class Alumno():

    nacionalidad = "Peruano"

    def __init__(self, nombre, distrito, notainicial, nota2, nota3):
        self.nombre = nombre
        self.distrito = distrito
        self.notainicial = 0
        self.nota2 = nota2
        self.nota3 = nota3

    def aprobar(self):
        promedio = (self.notainicial + self.nota2 + self.nota3) / 3
        self.promedio = promedio
        return self.promedio

    def mostrar(self):
        if self.promedio >= 10 and self.promedio <= 11:
            return "aprobó"
        else:
            return " desaprobó"

alumno_1 = Alumno("Lisseth", "Lima", 0,10, 11)
alumno_1.aprobar()
resultado = alumno_1.mostrar()

print("El alumno se llama: {}".format(alumno_1.nombre))
print("El alumno es de: {}".format(alumno_1.distrito))
print("El alumno : {}".format(resultado))

