"""1. Crear una lista de 6 objetos y mostrar en pantalla (ítems de cursos que lleves o hayas
llevado en la universidad)"""

lista = ["Circuito electronico", "Sistemas basados en conocimiento", "Seguridad de la informacion", "Realidad Virtual", "Proyecto de redes", "Auditoria de sistemas"]
print("Los cursos universitario que he llevado son los siguientes:")
for item, l in enumerate(lista,1):
    print(item , l)