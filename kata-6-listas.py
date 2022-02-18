# KATA 6 - LISTAS
# Ejercicio 1: Crear y usar listas de Python

from xml.sax.saxutils import prepare_input_source


planetas = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']

print("El número de planetas de la lista son ",  len(planetas))

print("Agregando a la lista el planeta a Pluto (Plutón)")
planetas.append('Pluto')
print(planetas[-1], "es el último planeta de la lista")


# Ejercicio 2: Trabajando con datos de una lista

# Solicitando al usuario el nombre del un planeta

planeta = input("Ingrese el nombre de un planeta, iniciando con mayúcula ")

# Obteniendo el índice del planeta ingresad
planeta_index = planetas.index(planeta)

# Mostrando los planetas más cercanos al sol a partir del planeta ingresado
print("Estos son los planetas más cercanos de " + planeta  + " son:")
print(planetas[0:planeta_index])

# Mostrando los planetas más lejanos al sol a partir del planeta ingresado
print("Y los planetas más lejanos de "+ planeta  + " son:")
print(planetas[planeta_index+1:])