"""2. Usando el concepto de herencia y encapsulación (para saldo) para crear
elsiguiente programa (3 ptos):
Reglas:
- Agregar un atributo saldo a la clase persona (ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la Persona que llame al método pueda
transferir la cantidad monto al objeto Persona2 por consiguiente deberá
ir actualizando también el saldo o monto que tiene la otra persona en su
cuenta cada vez que use el método transferencia

- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase por lo
menos realizando una transferencia y con dos personas."""
class Persona:
    def __init__(self, nombre=None, edad=None, saldo=None, nacionalidad="Peruana"):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = nacionalidad

    def solicitar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))
        self.saldo = int(input("Ingrese su saldo: "))

    def cumpleaños(self):
        if self.edad is not None:
            self.edad += 1
            print("Feliz cumpleaños {}! Ahora tienes {} años.".format(self.nombre, self.edad))
        else:
            print("No se puede calcular el cumpleaños debido a un error en la edad.")

    def transferencia(self, monto, persona_destino):
        monto = int(monto)
        if monto <= self.saldo:
            self.saldo -= monto
            persona_destino.saldo += monto
            print("Transferencia de {} a {} realizada. Saldo actual: {}".format(monto, persona_destino.nombre, self.saldo))
        else:
            print("Saldo insuficiente. Transferencia no realizada.")

    def mostrar_saldo(self):
        print("Saldo actual de {}: {}".format(self.nombre, self.saldo))


persona1 = Persona()
persona1.solicitar_datos()
persona1.mostrar_saldo()

persona2 = Persona()
persona2.solicitar_datos()
persona2.mostrar_saldo()

persona1.transferencia(300, persona2)
persona1.mostrar_saldo()
persona2.mostrar_saldo()
