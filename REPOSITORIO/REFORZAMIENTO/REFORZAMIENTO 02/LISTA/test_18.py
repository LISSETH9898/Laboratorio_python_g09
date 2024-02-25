"""18. Crear una lista con los 15 primeros números impares, luego agregar 3 números flotantes
repetidos (los cuales son impares dentro del rango indicado y que no sea el último
impar).
- Empezando desde 1 y no 0.
- Agregar un cadena en la posición 3 de la lista.
- Eliminar este valor string de la cadena usando del."""


lista = list(range(1,30,2))
print(lista)

lista.append(3.33)
lista.append(3.33)
lista.append(3.33)
print("mi lista actualizada es :{}".format(lista))


lista.insert(3,"hola")
print("mi lista actualizada es :{}".format(lista))


del lista[3]
print("la ultima actualizacion de mi lista es:{}".format(lista))