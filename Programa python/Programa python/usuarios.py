import os
import pwinput

def cargar_usuarios():
    usuarios = {}
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if len(partes) == 2:
                    usuario, clave = partes
                    usuarios[usuario] = clave
    return usuarios

def registrar_usuarios():
    usuarios = cargar_usuarios()
    while True:
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        if nombre_usuario in usuarios:
            print("❌ Ese nombre de usuario ya existe. Intente con otro.")
            continue
        clave_usuario = pwinput.pwinput("Ingrese la contraseña: ", mask="*")
        confirmar = input("¿Desea guardar los cambios? (si/no): ").strip().lower()
        if confirmar == "si":
            with open("usuarios.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"{nombre_usuario},{clave_usuario}\n")
            print("✅ Usuario registrado con éxito.\n")
            break
        else:
            print("Registro cancelado.\n")
            break


def inicio_sesion():
    usuarios = cargar_usuarios()
    if not usuarios:
        print("⚠️ No hay usuarios registrados. Por favor, registre uno primero.")
        return False

    usuario = input("Usuario: ")
    intentos = 0
    while intentos < 3:
        clave = pwinput.pwinput("Contraseña: ", mask="*")
        if usuario in usuarios and usuarios[usuario] == clave:
            print("✅ Acceso permitido.\n")
            print(f"Bienvenid@ {usuario}")
            return True
        else:
            print("❌ Usuario o contraseña incorrectos.\n")
            intentos += 1
    print("🚫 Acceso denegado tras 3 intentos fallidos.\n")
    return False

def inicio():
    while True:
        print("\n" + "=" * 60)
        print(" INICIO DE SESIÓN ")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        print("=" * 60)
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            registrar_usuarios()
        elif opcion == "2":
            if inicio_sesion():
                return True  # para que sirva el menu
        elif opcion == "3":
            return False
        else:
            print("Opción inválida, intente de nuevo.\n")