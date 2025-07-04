import usuarios
import reporte
import interfaz
import os
os.system("cls" if os.name == "nt" else "clear")
if __name__ == "__main__":
    interfaz.bienvenida()
    interfaz.barra_de_carga()
    if usuarios.inicio():
        interfaz.limpieza()
        reporte.iniciar_reporte()
    else:
        print("👋 Saliendo del programa.")