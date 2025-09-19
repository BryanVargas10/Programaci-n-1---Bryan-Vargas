#Buscar un valor:
#Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array.
#Informar la posición en caso afirmativo, o indicar que no se encuentra.

numeros = [0,0,0,0,0,0,0,0,0,0]

print("Cargá 10 números:")
for i in range(len(numeros)):
    numeros[i] = int(input(f"Número {i+1}: "))

buscado = int(input("Ingresá el número a buscar: "))

posicion = -1
for i in range(len(numeros)):
    if numeros[i] == buscado:
        posicion = i
        break

if posicion != -1:
    print(f"El número {buscado} está en la posición {posicion}")
else:
    print(f"El número {buscado} NO se encuentra en el array")
