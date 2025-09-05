# Crear una lista con los cuadrados de los números del 0 al 9
cuadrados = []
for numero in range(10):
    cuadrados.append(numero ** 2)

print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# El mismo resultado con list comprehension
cuadrados = [numero ** 2 for numero in range(10)]
print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Obtener los numeros del 1 al 9
# Con bucle tradicional
pares = []
for numero in range(10):
    if numero % 2 == 0:
        pares.append(numero)

print(pares)  # [0, 2, 4, 6, 8]

# Con list comprehension
pares = [numero for numero in range(10) if numero % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]