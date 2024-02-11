"""3. Quita 2 elementos de tu nueva lista ítems por valor, no por índice."""

"Lista anterior "

lista = ["Circuito electronico", "Sistemas basados en conocimiento", "Seguridad de la informacion", "Realidad Virtual", "Proyecto de redes", "Auditoria de sistemas"]

"Agregando 4 objetos"

lista.append("Excel")
lista.append("Tesis I")
lista.append("Proyecto de sistemas")
lista.append("Sistemas operativos")

print("La lista actualizada seria la siguiente: {}".format(lista))


"eliminando 2 lista de mi lista actualizada"

lista.remove("Seguridad de la informacion")
lista.remove("Sistemas basados en conocimiento")

print("la lista actualizada es: {}".format(lista))