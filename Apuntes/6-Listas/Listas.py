# MÓDULO 6 - LISTAS

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print(planets)

# Para acceder a los elementos, se debe de hacer mediante índices, de la siguiente manera
print("\n *** Accediendo a los elementos de la lista mediante índices")
print('The first planet is', planets[0])
print('The second planet is', planets[1])
print('The third planet is', planets[2])

# NOTA: Tosos los índices inician en 0

# Para modificar los elementos de una lista, se hace de la siguiente manera
print("\n *** Modificando valores de la lista")
planets[3] = 'Red Planet'
print('Mars is also known as', planets[3])

# Para saber la longitud de una lista
print("\n *** Obteniendo la longitud de la lista con la función len()")
number_of_planets = len(planets)
print('There are', number_of_planets, 'planets in the solar system.')

# Las listas en Python son dinámicas
print("\n *** Agregando valores a la lista con la función append()")
# Cabe mencionar que al usar esta función, los valores se van a ir 
# agregando al final de la lista
planets.append('Pluto')
number_of_planets = len(planets)
print('There are actually', number_of_planets, 'planets in the solar system.')


# Elimiando valores de la lista
print("\n *** Eliminando valores de la lista con la función pop()")
# Cabe mencionar que al usar esta función, los valores que se elimina el
# último elemento de la lista
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print('No, there are definitely', number_of_planets, 'planets in the solar system.')

# índices Negativos
print("\n *** Accediendo a los elementos mediante índices negativos")
# Los índices negativos comienzan al final de la ilsta y trabajan hacía atrás.
# Si usamos el índice -1, nos regresa el último elemento de la lista
# Si usamos el índice -2, nos regresa el penúltimo elemento de la lista
# Ejemplos:
print('The last planet is', planets[-1])
print('The penultimate planet is', planets[-2])


# Buscando valores en una list con la función index
print("\n *** Buscando valores en la lista con el método index()")
# Si la función index encuentra el valor buscado, devuele el índice donde se encuentra dicho valor
# De lo contrario, devolvera -1
# Ejemplo
jupiter_index = planets.index('Jupiter')
print('Jupiter is the', jupiter_index + 1, 'planet from the sun')

# Almacenar números en listas
print("\n *** Creando una lista con números")
gravity_on_planets = [0.378, 0.907, 1, 0.379, 2.36, 0.916, 0.889, 1.12]


bus_weight = 12650 # in kilograms, on Earth

print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('On Mercury, a double-decker bus weighs', bus_weight * gravity_on_planets[0], 'kg')

print("\n *** Usando la función max() y min()")
# min() y max() con listas
# Para obtener el valor mínimo y máximo de una lista se pueden usar las funciones
# min() y max() respectivamente.
# Ejemplo
print('The lightest a bus would be in the solar system is', bus_weight * min(gravity_on_planets), 'kg')
print('The heaviest a bus would be in the solar system is', bus_weight * max(gravity_on_planets), 'kg')

# Slice list 
print("\n *** Slice: obtener un fragmento de la lista")
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets_before_earth = planets[0:2]
print(planets_before_earth) # ['Mercury', 'Venus']
# Obteniendo el resto de los elementos de la lista
planets_after_earth = planets[3:8]
print(planets_after_earth) 

# Uniendo listas
print("\n *** Uniendo listas con el operador +")
amalthea_group = ['Metis', 'Adrastea', 'Amalthea', 'Thebe']
galilean_moons = ['Io', 'Europa', 'Ganymede', 'Callisto']

regular_satellite_moons = amalthea_group + galilean_moons
print('The regular satellite moons of Jupiter are', regular_satellite_moons)

# Ordenando los elementos de una lista con el método sort()
print("\n *** Ordenando los elementos de la lista con el método sort()")
# Ejemplo
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

print("Ordenando los elementos de la liste de forma inversa")
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
