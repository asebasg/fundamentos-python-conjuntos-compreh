# difference(): Devuelve un nuevo conjunto con elementos que están en el primer conjunto pero no en el segundo.
inventario = {"laptop", "teléfono", "tablet", "auriculares"}
vendidos = {"laptop", "auriculares"}
disponibles = inventario.difference(vendidos)
print(disponibles)  # {'teléfono', 'tablet'}
