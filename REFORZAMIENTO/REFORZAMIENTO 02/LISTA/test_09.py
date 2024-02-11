"""9. Sumar las dos listas creadas anteriormente y mostrar el resultado en terminal."""

"Lista 1"

lista = ["Circuito electronico", "Sistemas basados en conocimiento", "Seguridad de la informacion", "Realidad Virtual", "Proyecto de redes", "Auditoria de sistemas"]

lista.append("Excel")
lista.append("Tesis I")
lista.append("Proyecto de sistemas")
lista.append("Sistemas operativos")


"lista 2"
lista_vacia = []

lista_vacia.append(85.58)
lista_vacia.append(25.69)
lista_vacia.append(23.45)

lista_vacia.append(85)
lista_vacia.append(42)
lista_vacia.append(12)

lista_vacia.append("Perú")
lista_vacia.append("Colombia")
lista_vacia.append("Canada")


print("la lista actualizada es: {}".format(lista_vacia + lista))