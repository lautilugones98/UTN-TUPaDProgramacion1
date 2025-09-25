# TP 3 - Estructuras Condicionales

# 1) Mayor de edad
edad = int(input("1) Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

# 2) Nota aprobada
nota = float(input("\n2) Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Solo números pares
num = int(input("\n3) Ingrese un número par: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Categorías por edad
edad = int(input("\n4) Edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Validar contraseña 8–14 caracteres
pw = input("\n5) Ingrese contraseña: ")
if 8 <= len(pw) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Sesgo de distribución
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
m = mean(numeros_aleatorios)
med = median(numeros_aleatorios)
mod = mode(numeros_aleatorios)

print("\n6) Lista generada:", numeros_aleatorios)
print("Media:", m, "Mediana:", med, "Moda:", mod)

if m > med > mod:
    print("Sesgo positivo")
elif m < med < mod:
    print("Sesgo negativo")
else:
    print("Sin sesgo")

# 7) Frase termina en vocal
frase = input("\n7) Ingrese una frase: ")
if frase[-1].lower() in "aeiou":
    print(frase + "!")
else:
    print(frase)

# 8) Transformar nombre según opción
nombre = input("\n8) Ingrese su nombre: ")
opcion = input("1: MAYÚSCULAS, 2: minúsculas, 3: Capitalizado -> ")
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")

# 9) Clasificación de terremoto
magnitud = float(input("\n9) Magnitud: "))
if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

# 10) Estación del año
hemis = input("\n10) Hemisferio (N/S): ").upper()
mes = int(input("Mes (1-12): "))
dia = int(input("Día (1-31): "))

if   (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    norte, sur = "Invierno", "Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    norte, sur = "Primavera", "Otoño"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    norte, sur = "Verano", "Invierno"
else:
    norte, sur = "Otoño", "Primavera"

print("Estación:", norte if hemis == "N" else sur)
