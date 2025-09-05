# Encadenamientos

grupo_a = {1, 2, 3, 4, 5}
grupo_b = {4, 5, 6, 7}
grupo_c = {1, 5, 7, 9}

# Elementos que están en grupo_a y grupo_b, pero no en grupo_c
resultado = grupo_a.intersection(grupo_b).difference(grupo_c)
print(resultado)  # {4}
