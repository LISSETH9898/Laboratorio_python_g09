"""12. Realizar una clase que administre una agenda. Se debe almacenar en
un diccionario dentro de una lista para cada contacto el nombre, el
teléfono, email y DNI. Deberá tener los siguientes métodos:

Añadir contacto
Mostrar contactos
Buscar contacto
(Por DNI)"""


class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email, dni):
        contacto = {"Nombre": nombre, "Teléfono": telefono, "Email": email, "DNI": dni}
        self.contactos.append(contacto)
        print("Los contacto de la persona han sido agregado correctamente.")

    def mostrar_contactos(self):
        if self.contactos:
            print("Lista de contactos:")
            for contacto in self.contactos:
                valor = contacto.values()
                print(list(valor))
        else:
            print("La agenda está vacía.")

    def buscar_contacto_por_dni(self, dni):
        for contacto in self.contactos:
            if contacto["DNI"] == dni:
                print("Contacto encontrado con el Dni {} es:".format(dni))
                print(contacto)
                return
        print("No se encontró ningún contacto con ese DNI.")


agenda = Agenda()


agenda.agregar_contacto("Lissseth", "945786325", "camilagallegos116@gmail.com", "72026355")
agenda.agregar_contacto("Miguel", "987654321", "miguel1988@gmail.com", "79568245")


agenda.mostrar_contactos()


agenda.buscar_contacto_por_dni("79568245")



