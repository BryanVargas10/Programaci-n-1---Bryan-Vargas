#Mayor y su posición:
#Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se
#encuentra.

numeros = [0,0,0,0,0,0,0]

print("Cargá 7 números:")
for i in range(len(numeros)):
    numeros[i] = int(input(f"Número {i+1}: "))

mayor = numeros[0]
posicion = 0

for i in range(len(numeros)):
    if numeros[i] > mayor:
        mayor = numeros[i]
        posicion = i

print(f"El mayor es {mayor} y está en la posición {posicion}")
