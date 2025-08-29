#1. Escribir una función llamada saludar(nombre) que reciba un nombre como parámetro e imprima un saludo. Luego, el programa debe pedir el nombre del usuario y llamar a la función.

def saludar(nombre):
    print("Hola", nombre, "bienvenido!")

nombre_usuario = input("Ingresa tu nombre: ")
saludar(nombre_usuario)

#2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma, resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la función.
def operaciones(num1, num2):
    print("Suma:", num1 + num2)
    print("Resta:", num1 - num2)
    print("Multiplicación:", num1 * num2)

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
operaciones(a, b)
#3. Definir una función area_triangulo que reciba la base y la altura de un triángulo y devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado. Fórmula: area = (b * h) / 2.
def area_triangulo(base, altura):
    return (base * altura) / 2

b = float(input("Ingresa la base del triángulo: "))
h = float(input("Ingresa la altura del triángulo: "))
print("El área del triángulo es:", area_triangulo(b, h))

#4. Crear una función buscar_mayor que reciba tres números y devuelva los tres números ordenados de mayor a menor. Luego, el programa debe pedir los números y mostrar los números ordenados.
def buscar_mayor(num1, num2, num3):
    lista = [num1, num2, num3]
    lista.sort(reverse=True)  
    return lista

n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))

resultado = buscar_mayor(n1, n2, n3)
print("Los números ordenados de mayor a menor son:", resultado)

#5. Definir una función es_par(numero) que reciba un número y devuelva True si es par y False si es impar. Luego, el programa debe pedir un número y mostrar si es par o impar usando la función.
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

num = int(input("Ingresa un número: "))

if es_par(num):
    print("El número es par.")
else:
    print("El número es impar.")

#6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva cuántas horas y minutos sobran.
def convertir_minutos(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

m = int(input("Ingresa la cantidad de minutos: "))
h, resto = convertir_minutos(m)
print("Equivale a", h, "horas y", resto, "minutos.")

#7. Escribir una función verificar_acceso(edad) que reciba la edad de una persona y determine si es mayor de edad (18 años o más) devolviendo un booleano. Luego, el programa debe pedir la edad al usuario y mostrar un mensaje apropiado.

def verificar_acceso(edad):
    if edad >= 18:
        return True
    else:
        return False


ed = int(input("Ingresa tu edad: "))

if verificar_acceso(ed):
    print("Acceso permitido, eres mayor de edad.")
else:
    print("Acceso denegado, eres menor de edad.")

#8. Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el programa debe pedir el año de nacimiento del usuario y mostrar la edad calculada.

def calcular_edad(anio_nacimiento):
    anio_actual = 2025
    edad = anio_actual - anio_nacimiento
    return edad


anio = int(input("Ingresa tu año de nacimiento: "))
edad_calculada = calcular_edad(anio)
print("Tu edad es:", edad_calculada)
