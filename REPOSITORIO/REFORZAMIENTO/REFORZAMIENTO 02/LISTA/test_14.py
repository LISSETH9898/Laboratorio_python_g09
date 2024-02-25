"""14. Elimina un elemento por dos índices existentes y ya no por el valor."""

lista = ["Ana", "Cecilia", "Pedro", 45, 56, 89]

print("lista original: {}".format(lista))

del lista[0]
print("La lista actualizada 01 es :{}".format(lista))

del lista[3]
print("La lista actualizada 02 es:{}".format(lista))


