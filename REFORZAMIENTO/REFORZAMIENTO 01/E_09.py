"""9.Elevar al exponente de 4 un número que su valor estará asignado a una variable y
luego restar este mismo valor multiplicado por dos (usar pow). Mostrar el resultado en
pantalla."""

numero = 10
resultado_potencia = pow(numero, 4)

resultado_final = resultado_potencia - (2 * resultado_potencia)

print("El resultado de la siguiente opreacion es: {}".format(resultado_final))