#Invertir orden:
#Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero.
numeros = [0,0,0,0,0,0]

print("Cargá 6 números:")
for i in range(len(numeros)):
    numeros[i] = int(input(f"Número {i+1}: "))

print("Array invertido:")
for i in range(len(numeros)-1, -1, -1):
    print(numeros[i])
