lis_1 = []
lis_2 = []

lis_1.append("Lisseth")
lis_1.append(25)
lis_1.append("Ing.sistemas")

lis_2.append("Camila")
lis_2.append(24)
lis_2.append("Ing.industrial")
print("Mi lista1 actual es: {}".format(lis_1))
print("Mi lista2 actual es: {}".format(lis_2))
suma_lista = lis_1 + lis_2

print("La suma de mi lista es: {}".format(suma_lista))

suma_lista.reverse()
print("el reverse de la suma_lista es: {}".format(suma_lista))

del lis_1[1]
del lis_2[1]

print("mi lista actualizada es: {}".format(lis_1))
print("mi lista actualizada es: {}".format(lis_2))

