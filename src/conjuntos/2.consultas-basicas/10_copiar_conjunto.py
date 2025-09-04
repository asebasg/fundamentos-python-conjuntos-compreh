# copy(): Crea una copia superficial del conjunto.
original = {1, 2, (3, 4)}
copia = original.copy()
original.add(5)
print(original)  # {1, 2, (3, 4), 5}
print(copia)     # {1, 2, (3, 4)} - No se ve afectado por cambios en el original
