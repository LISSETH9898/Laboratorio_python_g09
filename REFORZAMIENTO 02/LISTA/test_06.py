"""6. Devuelve la cantidad de veces que se repite un curso (agregarla previamente a la lista)
dentro de la lista."""

lista = ["Circuito electronico", "Sistemas basados en conocimiento", "Seguridad de la informacion", "Realidad Virtual", "Proyecto de redes", "Auditoria de sistemas", "Tesis I"]

lista.append("Tesis I")

print("El curso Tesis I se repite: {} veces".format(lista.count("Tesis I")))


