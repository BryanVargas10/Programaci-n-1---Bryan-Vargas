# Sistema de gestión de biblioteca con listas estáticas

# Listas estáticas (20 posiciones)
titulos = [""] * 20
ejemplares = [0] * 20
cantidad = 0   # cantidad actual de libros cargados


def cargar_titulos():
    global cantidad
    while cantidad < 20:
        titulo = input("Ingrese el título del libro (o ENTER para terminar): ").strip()
        if titulo == "":
            break
        copias = int(input(f"Ingrese la cantidad de copias de '{titulo}': "))
        titulos[cantidad] = titulo
        ejemplares[cantidad] = copias
        cantidad += 1
    print("Carga finalizada.\n")


def mostrar_catalogo():
    print("\n--- Catálogo completo ---")
    for i in range(cantidad):
        print(f"{titulos[i]} → {ejemplares[i]} copias")
    print()


def consultar_disponibilidad():
    titulo = input("Ingrese el título a consultar: ").strip()
    for i in range(cantidad):
        if titulos[i].lower() == titulo.lower():
            print(f"'{titulos[i]}' tiene {ejemplares[i]} copias disponibles.\n")
            return
    print("El libro no se encuentra en el catálogo.\n")


def listar_agotados():
    print("\n--- Libros agotados ---")
    encontrado = False
    for i in range(cantidad):
        if ejemplares[i] == 0:
            print(titulos[i])
            encontrado = True
    if not encontrado:
        print("No hay libros agotados.")
    print()


def agregar_titulo():
    global cantidad
    if cantidad >= 20:
        print("No se pueden agregar más títulos (límite de 20 alcanzado).\n")
        return
    titulo = input("Ingrese el nuevo título: ").strip()
    copias = int(input("Ingrese la cantidad de copias: "))
    titulos[cantidad] = titulo
    ejemplares[cantidad] = copias
    cantidad += 1
    print(f"'{titulo}' agregado al catálogo.\n")


def actualizar_ejemplares():
    titulo = input("Ingrese el título a actualizar: ").strip()
    for i in range(cantidad):
        if titulos[i].lower() == titulo.lower():
            print(f"Cantidad actual: {ejemplares[i]}")
            cambio = int(input("Ingrese el nuevo número de ejemplares: "))
            ejemplares[i] = cambio
            print("Cantidad actualizada.\n")
            return
    print("El libro no se encuentra en el catálogo.\n")


def menu():
    while True:
        print("----- MENÚ -----")
        print("1. Cargar títulos y ejemplares")
        print("2. Mostrar catálogo completo")
        print("3. Consultar disponibilidad")
        print("4. Listar títulos agotados")
        print("5. Agregar un nuevo título")
        print("6. Actualizar ejemplares (préstamo/devolución)")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cargar_titulos()
        elif opcion == "2":
            mostrar_catalogo()
        elif opcion == "3":
            consultar_disponibilidad()
        elif opcion == "4":
            listar_agotados()
        elif opcion == "5":
            agregar_titulo()
        elif opcion == "6":
            actualizar_ejemplares()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")


# Programa principal
menu()
