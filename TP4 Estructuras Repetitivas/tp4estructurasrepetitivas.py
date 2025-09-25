# =========================
# Práctico 4: Estructuras Repetitivas
# =========================

# 1) Números del 0 al 100
print("Ejercicio 1: Números del 0 al 100")
for i in range(101):
    print(i)
print("\n" + "="*40 + "\n")

# 2) Contar cantidad de dígitos
print("Ejercicio 2: Contar dígitos de un número")
num = int(input("Ingresa un número entero: "))
cantidad_digitos = len(str(abs(num)))
print("Cantidad de dígitos:", cantidad_digitos)
print("\n" + "="*40 + "\n")

# 3) Sumar números entre dos valores
print("Ejercicio 3: Sumar números entre dos valores (excluyendo los extremos)")
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
suma = sum(range(min(a, b)+1, max(a, b)))
print("Suma de los números intermedios:", suma)
print("\n" + "="*40 + "\n")

# 4) Sumar números hasta ingresar 0
print("Ejercicio 4: Sumar números hasta ingresar 0")
total = 0
while True:
    num = int(input("Ingresa un número (0 para terminar): "))
    if num == 0:
        break
    total += num
print("Total acumulado:", total)
print("\n" + "="*40 + "\n")

# 5) Juego adivinar número
print("Ejercicio 5: Juego de adivinar un número")
import random
numero = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == numero:
        print(f"¡Correcto! Numero de intentos: {intentos}")
        break
print("\n" + "="*40 + "\n")

# 6) Números pares entre 0 y 100 en orden decreciente
print("Ejercicio 6: Números pares entre 0 y 100 decrecientes")
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)
print("\n" + "="*40 + "\n")

# 7) Sumar números desde 0 hasta n
print("Ejercicio 7: Sumar números desde 0 hasta n")
n = int(input("Ingresa un número entero positivo: "))
suma = sum(range(n + 1))
print("Suma de los números:", suma)
print("\n" + "="*40 + "\n")

# 8) Clasificar 100 números
print("Ejercicio 8: Contar pares, impares, positivos y negativos")
pares = impares = positivos = negativos = 0
for _ in range(100):
    num = int(input("Ingresa un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")
print("\n" + "="*40 + "\n")

# 9) Calcular media de 100 números
print("Ejercicio 9: Calcular la media de 100 números")
total = 0
for _ in range(100):
    num = int(input("Ingresa un número: "))
    total += num
media = total / 100
print("Media de los números:", media)
print("\n" + "="*40 + "\n")

# 10) Invertir los dígitos de un número
print("Ejercicio 10: Invertir dígitos de un número")
num = input("Ingresa un número: ")
print("Número invertido:", num[::-1])
print("\n" + "="*40 + "\n")