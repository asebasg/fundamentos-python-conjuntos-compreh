# < (subconjunto propio): Comprueba si el primer conjunto es subconjunto propio del segundo (todos los elementos están en el segundo y los conjuntos son diferentes).
conjunto_a = {1, 2}
conjunto_b = {1, 2, 3}
conjunto_c = {1, 2}

print(conjunto_a < conjunto_b)  # True - subconjunto propio
print(conjunto_a < conjunto_c)  # False - son iguales
