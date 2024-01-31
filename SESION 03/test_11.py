"""USO DEL FLUJO CONDICIONAL: if"""
"""if ternaria"""

"""Requisitos:
-Ingrsar por teclado el sueldo de un empleado
-Si el sueldo es mayor a 3000, imprmir"Su sueldo no tiene bonificacion
-Caso contrario: "Su sueldo tiene bonificacion"""

sueldo = int(input("Ingres el sueldo del empleador: "))

final = "Su tiene no tiene bonificacion " if sueldo > 3000 else "Su tiene  tiene bonificacionb este año "
print(final)