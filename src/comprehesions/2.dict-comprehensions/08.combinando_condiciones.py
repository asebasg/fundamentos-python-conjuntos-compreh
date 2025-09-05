# Crear un diccionario con nombres en mayúsculas y notas redondeadas
estudiantes = [
    {"nombre": "Ana", "nota": 7.8},
    {"nombre": "Carlos", "nota": 7.2},
    {"nombre": "Elena", "nota": 8.7}
]
nombre_nota_formateado = {
    estudiante["nombre"].upper(): round(estudiante["nota"])
    for estudiante in estudiantes
}
print(nombre_nota_formateado)  # {'ANA': 8, 'CARLOS': 7, 'ELENA': 9}