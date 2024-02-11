"""17. Crear una lista con los 10 primeros números al cuadrado y mostrar el resultado en
terminal."""

lista = list(range(1,11))

for l in lista:
    potencia = l ** 2
    print("{} ** 2 == {}".format(l, potencia))