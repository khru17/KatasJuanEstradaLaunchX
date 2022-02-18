# MÓDULO 8 - ADMINISTRAR DATOS CON DICCIONARIOS

# Los diccionarios de Python permiten trabajar con conjuntos de datos relacionados
# Un diccionario es una colección de pares clave-valor
# Se puede crear un diccionario vacío y agregar valores más adelante, o bien rellenarlo en el momento de la creación.

# Creando un diccionario
planet = {
    'name': 'Earth',
    'moons': 1
}


# Para acceder a los valores de un diccionario, se hace uso del método get
print("\n *** Accediendo a los valores del diccionario mediante el método get con la clave")
print(planet.get('name'))
print("Otra manera de acceder a un valor de un diccionario, podemos usar []")
print(planet['name'])

# Hay una diferencia principal entre usar get y corchetes, que es: 
# Si una clave no está disponible, get devuelve None y [ ] genera un error KeyError
# Ejemplo:
"""
wibble = planet.get('wibble') # Regresa None
wibble = planet['wibble'] # Arroja un KeyError
"""

# Actualizando los valores del diccionario
print("\n *** Actualizando los valores del diccionario con el método update")
# Actualizando el valor de la clave "name" a "Makemake"
planet.update({'name': 'Makemake'})
print(planet['name'])

print("También se pueden actualizar los valores usando corchetes")
print("Actualizando nuevamente el valor de 'name' a: ")
planet['name'] = 'Makemake-1'
print(planet['name'])

# También podemos actualizar varios valores del diccionario de la siguiente forma haciendo uso del método
# update y corchetes:
 # Usando update
"""
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Usando corchetes
planet['name'] = 'Jupiter'
planet['moons'] = 79
"""

planet['name'] = 'Jupiter'
# Adición y eliminación de claves
# Agregando una nueva clave al diccionario
print("\n *** Agregando una nueva clave y valor al diccionario")
planet['orbital period'] = 4333
print(planet)

# Eliminando una clave
print("\n *** Eliminando la clave y valor anterior del diccionario")
planet.pop('orbital period')
print(planet)

# Diccionarios más complejos
# Los diccionarios pueden almacenar cualquier tipo de valor, incluidos otros diccionarios
print("\n *** Añadiendo un diccionario en otro diccionario")
# Añadimos los datos
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(planet)

# Obteniendo valores de un diccionario dentro de otro
print(f"{planet['name']} polar diameter: {planet['diameter (km)']['polar']}")

# Salida: Jupiter polar diameter: 133709

# Recuperación de todas las claves y valores mediante el método keys()
print("\n *** Obteniendo las claves y valores mediante el método keys()")
print("En este caso tenemos el siguiente diccionario: ")
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
print(rainfall)

# Imprimiendo los valores del diccionario
print("\n *** Imprimendo todos los valores del diccionario con un ciclo for y el método keys()")
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

# Determinando la existencia de una clave en un diccionario con la función in
print("\n *** Determinando la existencia de una clave en un diccionario con la función in")

# Si 'december' existe en rainfall
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1
# Como december si existe, el valor será 3.1

print('december: ', rainfall['december'])

# Recuper todos los valores de un diccionario con el método values()
print("\n *** Recuper todos los valores de un diccionario con el método values()")
#Total de precipitaciones 0
total_rainfall = 0

# Para cada valor en los valores de rainfall
for value in rainfall.values():
    # El total de las precipitaciones será igual a ese mismo + el valor que se está iterando
    total_rainfall = total_rainfall + value

# Muestra 'Hay un total de precipitaciones (el valor total) en centímetros en el último cuarto (haciendo referencia al cuarto del año)
print(f'There was {total_rainfall}cm in the last quarter')

# Salida:
# There was 10.8cm in the last quarter