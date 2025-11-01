import random


# 1) Lista con las notas de 10 estudiantes
notas = [7, 8, 5, 9, 10, 6, 4, 7, 8, 9]
print("\n1) Lista de notas:", notas)

promedio = sum(notas) / len(notas)
print("Promedio:", promedio)
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

# 2) Lista de productos
productos = ["Pan", "Leche", "Huevos", "Arroz", "Fideos"]
print("\n2) Productos cargados:", productos)

productos_ordenados = sorted(productos)
print("Productos ordenados alfabéticamente:", productos_ordenados)

producto_a_eliminar = "Arroz"
productos_ordenados.remove(producto_a_eliminar)
print(f"Lista actualizada (sin '{producto_a_eliminar}'):", productos_ordenados)

# 3) Lista con 15 números enteros al azar entre 1 y 100
numeros = [random.randint(1, 100) for _ in range(15)]
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("\n3) Números generados:", numeros)
print("Lista de pares:", pares)
print("Lista de impares:", impares)
print(f"Cantidad de pares: {len(pares)} | Cantidad de impares: {len(impares)}")


# 4) Eliminar elementos repetidos
lista_repetidos = [1, 3, 5, 3, 1, 7, 9, 5]
lista_sin_repetidos = list(set(lista_repetidos))
print("\n4) Lista original:", lista_repetidos)
print("Lista sin repetidos:", lista_sin_repetidos)

# 5) Lista de estudiantes
estudiantes = ["Ana", "Juan", "Luz", "Pablo", "Sofía", "Mateo", "Valen", "Nico"]
print("\n5) Estudiantes presentes:", estudiantes)

a_agregar = "Lautaro"
a_eliminar = "Pablo"

estudiantes.append(a_agregar)
if a_eliminar in estudiantes:
    estudiantes.remove(a_eliminar)
print("Lista final actualizada:", estudiantes)


# 6) Rotar lista hacia la derecha
nums = [10, 20, 30, 40, 50, 60, 70]
rotada = [nums[-1]] + nums[:-1]
print("\n6) Lista original:", nums)
print("Lista rotada a la derecha:", rotada)


# 7) Matriz de temperaturas mínimas y máximas (7x2)

temperaturas = [
    [10, 20], [12, 21], [9, 18], [8, 19], [11, 22], [7, 17], [13, 23]
]

minimas = [t[0] for t in temperaturas]
maximas = [t[1] for t in temperaturas]
prom_min = sum(minimas) / len(minimas)
prom_max = sum(maximas) / len(maximas)

amplitudes = [maximas[i] - minimas[i] for i in range(7)]
dia_mayor_amplitud = amplitudes.index(max(amplitudes)) + 1

print("\n7) Temperaturas (mín, máx):", temperaturas)
print(f"Promedio mínimas: {prom_min:.2f} | Promedio máximas: {prom_max:.2f}")
print(f"Día con mayor amplitud térmica: Día {dia_mayor_amplitud}")


# 8) Matriz de notas de 5 estudiantes en 3 materias
notas_estudiantes = [
    [7, 8, 6],
    [9, 10, 8],
    [6, 7, 5],
    [8, 8, 9],
    [5, 6, 7]
]

promedios_estudiantes = [sum(fila)/len(fila) for fila in notas_estudiantes]
promedios_materias = [sum(col)/len(notas_estudiantes) for col in zip(*notas_estudiantes)]

print("\n8) Notas (5x3):")
for i, fila in enumerate(notas_estudiantes, 1):
    print(f"Estudiante {i}: {fila} - Promedio: {promedios_estudiantes[i-1]:.2f}")

print("Promedio por materia:", [round(x, 2) for x in promedios_materias])


# 9) Tablero de Ta-Te-Ti (3x3)
tateti = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

jugadas = [(0, 0, "X"), (1, 1, "O"), (0, 1, "X"), (2, 2, "O"), (0, 2, "X")]

for fila, col, simbolo in jugadas:
    tateti[fila][col] = simbolo

print("\n9) Tablero final de Ta-Te-Ti:")
for fila in tateti:
    print(fila)


# 10) Ventas de 4 productos durante 7 días (4x7)
ventas = [
    [10, 12, 8, 15, 20, 9, 11],
    [5, 7, 6, 8, 9, 7, 10],
    [14, 13, 15, 17, 16, 18, 20],
    [9, 8, 10, 11, 12, 9, 10]
]

# Total por producto
total_producto = [sum(fila) for fila in ventas]
# Total por día
total_dia = [sum(col) for col in zip(*ventas)]

print("\n10) Ventas (4 productos x 7 días):")
for i, fila in enumerate(ventas, 1):
    print(f"Producto {i}: {fila} - Total: {total_producto[i-1]}")

print(f"Día con mayores ventas totales: Día {total_dia.index(max(total_dia)) + 1}")
print(f"Producto más vendido en la semana: Producto {total_producto.index(max(total_producto)) + 1}")
