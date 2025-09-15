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