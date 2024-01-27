"""listas en Python"""

"""Listas (del): elimina un valor indicandao el inico del valor en la lista"""

paises =[]

paises.append("Peru")
paises.append("Brasil")
paises.append("Canada")
paises.append("España")
paises.append("Chile")


print("los valores de mi lista de paises son: {}".format(paises))

del paises[2]

print("mi lista actualizada tiene los siguientes valores: {}".format(paises))