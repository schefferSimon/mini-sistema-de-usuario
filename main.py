from services.auth_service import AuthService

def menu():
    print("\n=== MINI SISTEMA DE USUARIOS ===")
    print("1. Registrar usuario")
    print("2. Iniciar sesion")
    print("3. Salir")


def main():
    autenticacion = AuthService()

    while True:
        menu()
        opcion = input("\n seleccione una opcion: ")

        if opcion == "1" :
            nombre = input("Nuevo usuario: ")
            contraseña = input("Contraseña: ")
            ok, msg = autenticacion.reguistrar(nombre, contraseña)
            print(msg)

        elif opcion == "2":
            nombre = input("Usuario: ")
            contraseña = input("Contraseña: ")
            ok, msg = autenticacion.login(nombre,contraseña)
            print(msg)

        elif opcion == "3":
            print("Hasta luego.")
            break

        else:
            print("Opcion invalida intente nuevamente")
        