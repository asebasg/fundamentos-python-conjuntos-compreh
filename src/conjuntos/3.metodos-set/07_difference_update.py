# difference_update(): Elimina del conjunto original los elementos que están en otro conjunto.
todos_cursos = {"Python", "Java", "SQL", "JavaScript", "C++"}
cursos_completados = {"Python", "SQL"}
# Elimina los cursos completados de la lista total
todos_cursos.difference_update(cursos_completados)
print(todos_cursos)  # {'Java', 'JavaScript', 'C++'}
