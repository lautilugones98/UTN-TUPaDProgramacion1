# Ejercicio 1
print("Hola Mundo!")

# Ejercicio 3
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
lugar = input("Lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

# Ejercicio 3
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
lugar = input("Lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

# Ejercicio 4
import math
radio = float(input("Radio del círculo (en unidades): "))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f"Área: {area:.4f}")
print(f"Perímetro: {perimetro:.4f}")

# Ejercicio 5
segundos = float(input("Ingrese cantidad de segundos: "))
horas = segundos / 3600.0
print(f"{segundos} segundos equivalen a {horas:.6f} horas.")

# Ejercicio 6
n = int(input("Ingresa un número para ver su tabla de multiplicar: "))
print(f"Tabla del {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

    # Ejercicio 7
a = int(input("Ingrese el primer entero (no 0): "))
b = int(input("Ingrese el segundo entero (no 0): "))
if a == 0 or b == 0:
    print("Ambos números deben ser distintos de 0.")
else:
    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Multiplicación: {a * b}")
    print(f"División (a / b): {a / b}")
    print(f"División (b / a): {b / a}")

    # Ejercicio 8
peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros (ej: 1.75): "))
if altura <= 0:
    print("Altura inválida.")
else:
    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc:.2f}")

# Ejercicio 9
c = float(input("Temperatura en °C: "))
f = c * 9/5 + 32
print(f"{c} °C equivalen a {f:.2f} °F")

