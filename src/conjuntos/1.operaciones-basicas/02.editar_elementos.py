# update(): Añade múltiples elementos de una vez. Puede recibir cualquier iterable (lista, tupla, otro conjunto, etc.).
lenguajes = {"Python", "Java"}
nuevos_lenguajes = ["Go", "Rust", "TypeScript"]
lenguajes.update(nuevos_lenguajes)
print(lenguajes)  # {'Python', 'Java', 'Go', 'Rust', 'TypeScript'}