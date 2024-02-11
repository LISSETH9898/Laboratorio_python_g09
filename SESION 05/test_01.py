"""Programacion funcional en Python"""

def multiplica(a,b,c=1000):
    resultado = a * b * c
    return resultado

print("EL RESULTADO DE MI FUNCION ES: {}".format(multiplica(40, 30)))
print("EL RESULTADO DE MI FUNCION ES: {}".format(multiplica (40, 2, 30)))