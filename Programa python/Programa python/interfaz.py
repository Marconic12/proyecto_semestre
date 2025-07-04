import os
from pyfiglet import Figlet
import time
import sys
def bienvenida():
    fuente  = Figlet(font="slant")  
    texto = fuente.renderText('BIEVENID@S')    
    # Centrar cada línea
    columnas = os.get_terminal_size().columns
    for linea in texto.splitlines():
        print(linea.center(columnas))    
    print("🌞 Monitoreo inteligente de energía renovable 🌞".center(columnas))
    time.sleep(3)
    os.system("cls" if os.name == "nt" else "clear")
def barra_de_carga(tiempo_total=3, pasos=30):
    print("🔄 Cargando...", end="", flush=True)
    for i in range(pasos):
        time.sleep(tiempo_total / pasos)
        sys.stdout.write("█")
        sys.stdout.flush()
    print(" ✅ Listo\n")
    os.system("cls" if os.name == "nt" else "clear")
def limpieza():
    os.system("cls")