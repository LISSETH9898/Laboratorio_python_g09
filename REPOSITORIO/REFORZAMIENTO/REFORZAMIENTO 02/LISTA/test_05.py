"""5. Obtén la cantidad total ítems que tienes en tu lista creada y mostrar el resultado en
consola. (Pista: len(lista))"""


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


"invirtiendo "

lista.reverse()
print("la lista invertida es la siguiente:{}".format(lista))


"total de items que tiene una lista"

print(len(lista))