"""19. Crea una lista vacía (con 10 posiciones), pedir al usuario c/u sus valores y que
finalmente se devuelva la suma y la media de los números ingresados de la lista."""


lista_vacia = [0] * 10

for i in range(10):
    valor = int(input("Ingrese el valor para la posición {}: ".format(i+1)))
    lista_vacia[i] = valor


suma = sum(lista_vacia)
media = suma / len(lista_vacia)

print("Lista ingresada: {}".format(lista_vacia))
print("Suma de los números: {}".format(suma))
print("Media de los números: {}".format(media))
