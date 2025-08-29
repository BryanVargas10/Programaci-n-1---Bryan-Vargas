#1. Refactorización en funciones
#● Crear funciones para:
#○ mostrar_atracciones() → muestra el menú de atracciones.
#○ puede_subir(edad, atraccion) → devuelve True/False según si puede acceder a la atracción.
#○ calcular_precio(atraccion) → devuelve el precio de la atracción.
#○ registrar_visita() → pide datos del visitante, procesa las atracciones elegidas y retorna el
#resumen.
#○ mostrar_resumen(resumen) → imprime en pantalla la información del visitante.




def mostrar_atracciones():
    print("Atracciones disponibles:")
    print("1 - Montaña Rusa (Edad mínima: 12) - $1500")
    print("2 - Casa del Terror (Edad mínima: 6) - $1200")
    print("3 - Carrusel (Edad mínima: 0) - $800")


def puede_subir(edad, atraccion):
    if atraccion == 1 and edad >= 12:
        return True
    elif atraccion == 2 and edad >= 6:
        return True
    elif atraccion == 3:
        return True
    else:
        return False


def calcular_precio(atraccion):
    if atraccion == 1:
        return 1500
    elif atraccion == 2:
        return 1200
    elif atraccion == 3:
        return 800
    else:
        return 0


def registrar_visita():
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    
    mostrar_atracciones()
    cantidad = int(input("¿Cuántas atracciones quieres usar?: "))
    
    atracciones_elegidas = []
    atracciones_usadas = []
    total_pago = 0
    
    for i in range(cantidad):
        eleccion = int(input(f"Elige la atracción {i+1} (1-3): "))
        atracciones_elegidas.append(eleccion)
        if puede_subir(edad, eleccion):
            atracciones_usadas.append(eleccion)
            total_pago += calcular_precio(eleccion)
            print("✅ Puedes subir a esta atracción.")
        else:
            print(" No puedes subir a esta atracción.")
    
    
    if len(atracciones_usadas) >= 3:
        descuento = total_pago * 0.10
        total_pago -= descuento
        print(f"🎉 Se aplicó un descuento del 10%: -${descuento:.0f}")
    
    resumen = {
        "nombre": nombre,
        "edad": edad,
        "atracciones_elegidas": atracciones_elegidas,
        "atracciones_usadas": atracciones_usadas,
        "total_pago": total_pago
    }
    return 

