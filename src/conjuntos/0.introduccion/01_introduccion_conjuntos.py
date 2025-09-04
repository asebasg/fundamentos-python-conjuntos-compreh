""" Conjuntos basicos """
colores = {"rojo", "verde", "azul", "rojo"}
print(colores)  # {'verde', 'azul', 'rojo'}

numeros = set([1, 2, 3, 2, 1])
print(numeros)  # {1, 2, 3}

usuarios = set(["ana", "carlos", "ana", "elena", "carlos"])
print(usuarios)  # {'ana', 'elena', 'carlos'}

# Verificación de pertenencia eficiente
frutas = {"manzana", "naranja", "plátano"}
print("manzana" in frutas)  # True
print("uva" in frutas)      # False