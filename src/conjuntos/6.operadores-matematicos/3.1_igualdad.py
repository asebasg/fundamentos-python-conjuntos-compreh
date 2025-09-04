# == (igualdad): Comprueba si dos conjuntos contienen exactamente los mismos elementos.

conjunto_a = {1, 2, 3}
conjunto_b = {3, 1, 2}  # Mismo contenido, diferente orden
conjunto_c = {1, 2, 3, 4}

print(conjunto_a == conjunto_b)  # True
print(conjunto_a == conjunto_c)  # False
