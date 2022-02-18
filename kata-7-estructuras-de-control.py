# KATA 7 -ESTRUCTURAS DE CONTROL

# Ejercicio 1

# Declarando las variables de la entrada y la lista
new_planet = ""
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    
    new_planet = input("Ingrese un nuevo planeta o la palabra done para salir: ")

# Ejercicio 2
# Mostrando los elementos de la lista
print("\n *** Mostrando los planetas ingresados: ")
for planet in planets:
    print(planet)