# KATA 8 - DICCIONARIOS

# Ejercicio 1
print("\n\n *** Ejercicio 1")
# Creando el diccionario

planet = {
    'name' : 'Mars',
    'moons' : 2
}

# Mostrando los datos del planeta
print("El planeta ", planet['name'], " tiene ", planet['moons'], " lunas")

# Agregando otro diccionario
print("\nSe han agregado nuevos datos al diccionario")
planet['circunferencia (km)'] = {'polar' : 6752, 'equatorial' : 6792}

# Imprimiendo el nombre del planeta con su circunferencia polar
print(planet['name'], " tiene una circunferencia polar de ", planet['circunferencia (km)']['polar'], " km")

# Ejercicio 2: Programación dinámica con diccionarios

# Diccionario con las lunas por cada planeta
print("\n\n *** Ejercicio 2")
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# Calculando el número de lunas
total_moons = 0

for moon in planet_moons.values():
    total_moons += moon

print("Número totales de lunas de los planetas", total_moons) 
# Total de lunas: 214

planets = len(planet_moons.keys())
average = total_moons / planets
print("El promedio de las lunas por planeta es: ", average) 
# Promedia de las lunas: 17.8333

