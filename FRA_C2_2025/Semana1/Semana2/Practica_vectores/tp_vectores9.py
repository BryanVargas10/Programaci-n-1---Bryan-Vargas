#Intercambiar elementos pares por ceros:
#Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array
#resultante

numeros = [0,0,0,0,0,0,0,0,0,0]

print("Cargá 10 números:")
for i in range(len(numeros)):
    numeros[i] = int(input(f"Número {i+1}: "))

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numeros[i] = 0

print("Array con pares reemplazados por 0:")
for i in range(len(numeros)):
    print(numeros[i])
