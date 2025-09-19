#Comparar dos arrays:
#Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento
#y mostrar un mensaje indicando si son o no iguales

a = [0,0,0,0,0]
b = [0,0,0,0,0]

print("Cargá el primer array:")
for i in range(len(a)):
    a[i] = int(input(f"A[{i+1}]: "))

print("Cargá el segundo array:")
for i in range(len(b)):
    b[i] = int(input(f"B[{i+1}]: "))

iguales = True
for i in range(len(a)):
    if a[i] != b[i]:
        iguales = False
        break

if iguales:
    print("Los arrays son iguales")
else:
    print("Los arrays NO son iguales")
