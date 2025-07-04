from datetime import datetime
import matplotlib.pyplot as plt
import random
import time
import interfaz
import re
# ================= FUNCIONES DE VALIDACIÓN =================
def entrada_valida_direccion():
    patron = re.compile(r'^[A-Za-z0-9 ]+$')  # Nota el espacio dentro de los corchetes
    while True:
        direccion = input(
            "Ingrese la dirección del cliente: "
        ).strip()
        if patron.fullmatch(direccion):
            return direccion
        else:
            print("Entrada inválida. Solo se permiten letras, números y espacios.")
def entrada_valida_letras(mensaje):
    while True:
        nombre = input(mensaje).strip()
        if all(part.isalpha() for part in nombre.split()) and 3 <= len(nombre.replace(" ", "")) <= 30:
            return nombre
        print("❌ Entrada inválida. Solo letras y espacios permitidos (4 a 30 caracteres sin contar espacios).")
def entrada_valida_decimal(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("❌ El valor debe ser mayor que 0.")
        except ValueError:
            print("❌ Entrada inválida. Ingrese un número decimal.")

def entrada_valida_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("❌ El número debe ser mayor que 0.")
        except ValueError:
            print("❌ Entrada inválida. Ingrese un número entero.")

def seleccionar_mes(numero):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    return meses[(numero - 1) % 12]

def explicar_instalacion_libreria():
    print("\n===== INSTALACIÓN DE LA LIBRERÍA matplotlib =====")
    print("Para que el gráfico funcione correctamente, debe instalar la librería matplotlib.")
    print("📦 Pasos para instalar matplotlib:")
    print("1. Abra la terminal o símbolo del sistema (cmd).")
    print("2. Escriba el siguiente comando y presione Enter:")
    print("   pip install matplotlib")
    print("⚠️ Si el comando 'pip' no funciona, asegúrese de que Python esté agregado al PATH.")
    print("   También puede intentar con:")
    print("   python -m pip install matplotlib")
    print("✅ Una vez instalado, podrá visualizar los gráficos sin problemas.")

# ================= ENTRADA DE DATOS INICIALES =================
def iniciar_reporte():
    global nombre_cliente, direccion, capacidad_planta, numero_mes
    global produccion_energetica, produccion_acumulada_total, fac_acumulada_total
    global nombre_mes_actual, nombre_mes_anterior
    global PRECIO_KW

    # ================= ENTRADA DE DATOS INICIALES =================
    nombre_cliente = entrada_valida_letras("Ingrese el nombre del cliente: ")
    direccion = entrada_valida_direccion()
    capacidad_planta = entrada_valida_decimal("Ingrese la capacidad de producción de la planta (en kW): ")
    numero_mes = entrada_valida_entero("Ingrese el número total de meses de operación de la planta: ")

    # ================= CÁLCULOS =================
    PRECIO_KW = 0.15
    efiencia = capacidad_planta * 0.2
    horas_solares = 4.5
    produccion_dia = efiencia * horas_solares
    produccion_mes = produccion_dia * 30

    produccion_energetica = []
    produccion_acumulada_total = 0

    for _ in range(numero_mes):
        valor = random.uniform(produccion_mes * 0.95, produccion_mes * 1.05)
        produccion_energetica.append(valor)
        produccion_acumulada_total += valor

    fac_acumulada_total = produccion_acumulada_total * PRECIO_KW
    nombre_mes_actual = seleccionar_mes(numero_mes)
    nombre_mes_anterior = seleccionar_mes(numero_mes - 1)

    # ================= MENÚ PRINCIPAL =================
    menu()

# Evita ejecución automática al importar
if __name__ == "__main__":
    iniciar_reporte()

def encabezado():
    print("=" * 63)
    print("       REPORTE RESUMIDO DE PRODUCCIÓN DE PLANTA SOLAR")
    print("=" * 63)
    print("Nombre del proveedor: Ing. Milton Ruiz")
    print("Departamento: Ventas")
    print("Teléfono: +(505) 22512800")
    print("Celular: +(505) 8631 7616")
    print("Email: sclientes@sencomca.com")
    print("Dirección: km 6 Carretera Norte")
    print("=" * 63)

# ================= FUNCIONES DE REPORTE =================
def mostrar_reporte_en_pantalla():
    fecha_actual = datetime.now()
    dia, mes_fecha, anio = fecha_actual.day, fecha_actual.month, fecha_actual.year
    encabezado()
    print("Fecha de emisión del reporte: {}/{}/{}".format(dia, mes_fecha, anio))
    print("Cliente: {}".format(nombre_cliente))
    print("Ubicación: {}".format(direccion))
    print("Capacidad de la planta: {:.2f} kW".format(capacidad_planta))
    print("Producción acumulada hasta {}: {:.2f} kWh".format(nombre_mes_actual, produccion_acumulada_total))
    print("Corte del mes anterior ({}): {:.2f} kWh".format(nombre_mes_anterior, produccion_acumulada_total - produccion_energetica[-1]))
    print("Producción del mes actual ({}): {:.2f} kWh".format(nombre_mes_actual, produccion_energetica[-1]))
    print("A facturar: ${:.2f}".format(produccion_energetica[-1] * PRECIO_KW))
    print("Facturación acumulada hasta {}: ${:.2f}".format(nombre_mes_actual, fac_acumulada_total))
    print("* Este valor no incluye IVA *")
    print("=" * 63)

def guardar_reporte_en_txt():
    with open("reporte_{}.txt".format(nombre_cliente.replace(" ", "_")), "w",encoding='utf-8') as archivo:
        fecha_actual = datetime.now()
        dia, mes_fecha, anio = fecha_actual.day, fecha_actual.month, fecha_actual.year
        archivo.write("=" * 63 + "\n")
        archivo.write("       REPORTE RESUMIDO DE PRODUCCIÓN DE PLANTA SOLAR\n")
        archivo.write("=" * 63 + "\n")
        archivo.write("Fecha de emisión del reporte: {}/{}/{}\n".format(dia, mes_fecha, anio))
        archivo.write("Cliente: {}\n".format(nombre_cliente))
        archivo.write("Ubicación: {}\n".format(direccion))
        archivo.write("Capacidad de la planta: {:.2f} kW\n".format(capacidad_planta))
        archivo.write("Producción acumulada hasta {}: {:.2f} kWh\n".format(nombre_mes_actual, produccion_acumulada_total))
        archivo.write("Producción del mes actual ({}): {:.2f} kWh\n".format(nombre_mes_actual, produccion_energetica[-1]))
        archivo.write("Facturación acumulada: ${:.2f}\n".format(fac_acumulada_total))
        archivo.write("* Este valor no incluye IVA *\n")
    print("✅ Reporte guardado como archivo de texto.")

def calcular_recuperacion_inversion():
    inversion = entrada_valida_decimal("Ingrese el monto de la inversión (en dólares): ")
    facturacion_mensual_prom = fac_acumulada_total / numero_mes
    if facturacion_mensual_prom == 0:
        print("❌ La facturación mensual promedio es 0, no se puede calcular la recuperación.")
        return
    meses_recuperacion = inversion / facturacion_mensual_prom
    print(f"\n📈 La inversión de ${inversion:.2f} se recuperaría en aproximadamente {meses_recuperacion:.1f} meses.")

def graficar_produccion():
    nombres_meses = [seleccionar_mes(i + 1) for i in range(numero_mes)]
    plt.figure(figsize=(10, 5))
    plt.bar(nombres_meses, produccion_energetica, color='skyblue')
    plt.title("Producción energética mensual")
    plt.xlabel("Mes")
    plt.ylabel("Producción (kWh)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# ================= MENÚ =================
def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Ver reporte en pantalla")
        print("2. Guardar reporte en archivo de texto")
        print("3. Calcular recuperación de inversión")
        print("4. Ver gráfico de producción mensual (para ver el grafico recuerde tener instlado la libreria matplotib)")
        print("5. ¿como instalar la libreria matplotlib?")
        print("6. salir")
        

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            print("\n"*10)
            mostrar_reporte_en_pantalla()
            time.sleep(15)
        elif opcion == "2":
            guardar_reporte_en_txt()
        elif opcion == "3":
            calcular_recuperacion_inversion()
            time.sleep(15)
        elif opcion == "6":
            print("\n👋 Gracias por usar el sistema. Hasta pronto.")
            break
        elif opcion == "5":
            explicar_instalacion_libreria()
        elif opcion == "4":
            graficar_produccion()
        else:
            print("❌ Opcion no válida. Intente nuevamente.")
        interfaz.limpieza()
