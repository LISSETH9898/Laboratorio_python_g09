"""Uso de: for"""

ingenierias = ["Software", "Sistemas", "Industrial", "Quimica", "Mecanica"]

print("El tamaño de la lista es: {}".format(len(ingenierias)))
i = 0


for ingenieria in ingenierias:
    print(ingenieria)
    i = i + 1
    print("Valor de i:  {}".format(i))