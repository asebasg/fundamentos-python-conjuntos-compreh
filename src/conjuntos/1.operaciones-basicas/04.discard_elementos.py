# discard(): Similar a remove(), pero no lanza error si el elemento no existe.
animales = {"perro", "gato", "conejo"}
animales.discard("pájaro")  # No existe, pero no genera error
print(animales)  # {'perro', 'gato', 'conejo'}