#Función para buscar la primera aparición de un valor:
#Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar
#la posición de la primera aparición de ese número o -1 si no se encuentra.

def buscar_primera_aparicion(numeros, buscado):
    for i in range(len(numeros)):
        if numeros[i] == buscado:
            return i
    return -1

# Programa principal
lista = [0,0,0,0,0]

print("Cargá 5 números:")
for i in range(len(lista)):
    lista[i] = int(input(f"Número {i+1}: "))

n = int(input("Número a buscar: "))

pos = buscar_primera_aparicion(lista, n)

if pos != -1:
    print(f"El número {n} está en la posición {pos}")
else:
    print(f"El número {n} NO se encuentra en el array")
