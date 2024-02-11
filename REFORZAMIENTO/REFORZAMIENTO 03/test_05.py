"""5. Crear una función que aceptará por parámetro dos valores que serán
ingresados por el usuario, una lista donde los valores serán llenados
por el usuario también y un segundo parámetro que eliminará de la
lista que fue ingresada a la función, finalmente el output de la función
será la lista actualizada sin el valor que se sacará de la lista. Mostrar
también la lista original y el número que fue eliminado."""

valor1 = input("Ingrese el primer valor: ")
valor2 = input("Ingrese el segundo valor: ")
lista = input("Ingrese una lista de valores separados por espacios: ").split()
valor_a_eliminar = input("Ingrese el valor que desea eliminar de la lista: ")

def eliminar_valor(lista, valor_a_eliminar):
    print("Lista original:", lista)

    print("Valor a eliminar:", valor_a_eliminar)

    if valor_a_eliminar in lista:
        lista.remove(valor_a_eliminar)
        print("La lista ha sido actualizada: {}".format(lista))
    else:
        print("El valor a eliminar no está presente en la lista.")

    return lista

lista_actualizada = eliminar_valor(lista, valor_a_eliminar)