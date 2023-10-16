
# Empezar aquí la resolución del ejercicio
nombre_completo_1 = str(input("nombre completo del padre,madre o tutor/a: "))
nombre_completo_2 = str(input("nombre completo del padre,madre o tutor/a: "))
nombre = str(input("Nombre del hijo/a: "))

nombre_1, apellido_1 = nombre_completo_1.split(" ")
nombre_2, apellido_2 = nombre_completo_2.split(" ")
hijo = nombre + " " + apellido_1 + " " + apellido_2
print(hijo)