# symmetric_difference(): Crea un nuevo conjunto con elementos que están en cualquiera de los conjuntos, pero no en ambos.
ciencias = {"física", "química", "biología", "matemáticas"}
artes = {"literatura", "música", "pintura", "matemáticas"}
exclusivos = ciencias.symmetric_difference(artes)
print(exclusivos)  # {'física', 'química', 'biología', 'literatura', 'música', 'pintura'}
