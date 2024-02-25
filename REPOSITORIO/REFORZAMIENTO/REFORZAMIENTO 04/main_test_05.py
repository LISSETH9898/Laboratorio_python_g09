from validar_test_05 import validar_nombre_usuario

def main():
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    resultado_validacion = validar_nombre_usuario(nombre_usuario)
    if resultado_validacion == True:
        print("El nombre de usuario es válido.")
    else:
        print(resultado_validacion)

if __name__ == "__main__":
    main()