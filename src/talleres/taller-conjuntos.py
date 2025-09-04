print("=== PROGRAMA: ANÁLISIS DE ESTUDIANTES POR ASIGNATURA ===\n")

# Definir los tres conjuntos de estudiantes
# 1. Conjunto de estudiantes que cursan matemáticas (5 estudiantes)
# Escribe aquí tu código
estudiantes_matematicas = {"Sebastian", "Ana", "Nicolas", "Sofia", "Marta"}

# 2. Conjunto de estudiantes que cursan física (5 estudiantes)
# Escribe aquí tu código
estudiantes_fisica = {"Nicolas", "Sofia", "Sebastian", "Juan", "Laura"}

# 3. Conjunto de estudiantes que cursan programación (5 estudiantes)
# Escribe aquí tu código
estudiantes_programacion = {"Sebastian", "Ana", "Angel", "Patricia", "Angelica"}

print("=== CONJUNTOS INICIALES ===")
print(f"Estudiantes de Matemáticas: {estudiantes_matematicas}")
print(f"Estudiantes de Física: {estudiantes_fisica}")
print(f"Estudiantes de Programación: {estudiantes_programacion}")

print("\n=== ANÁLISIS DE INTERSECCIONES Y DIFERENCIAS ===")

# 1. Los estudiantes que cursan las tres asignaturas
# Escribe aquí tu código usando operadores de conjuntos
tres_asignaturas = {}
tres_asignaturas |= estudiantes_matematicas, estudiantes_fisica, estudiantes_programacion

print(f"Estudiantes que cursan las tres asignaturas: {tres_asignaturas}")

# 2. Los estudiantes que cursan matemáticas y física, pero no programación
# Escribe aquí tu código usando operadores de conjuntos


print(f"Estudiantes que cursan matemáticas y física, pero no programación: {mat_fis_no_prog}")

# 3. Los estudiantes que solo cursan una asignatura
# Escribe aquí tu código para cada asignatura individualmente




# Unir los tres conjuntos de estudiantes que solo cursan una asignatura
# Escribe aquí tu código


print(f"Estudiantes que solo cursan una asignatura: {solo_una_asignatura}")

# 4. Todos los estudiantes únicos (el conjunto total)
# Escribe aquí tu código usando operadores de conjuntos


print(f"Total de estudiantes únicos: {todos_estudiantes}")
print(f"Número total de estudiantes: {len(todos_estudiantes)}")