
# EJERCICIO 1: Transformar cadenas

text = "Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."

# Separando el texto en oraciones
text_separado = text.split('. ')
# print(text_separado)

# Creando una lista con las palabras clave
palabras_clave = ["average", "temperature", "distance"]

# Recorriendo la cadena con un ciclo for
for oracion in text_separado:
    for palabra_clave in palabras_clave:
        if palabra_clave in oracion:
            # Remplacando C por Celsius
            print(oracion.replace(' C', ' Celsius'))
            break


# EJERCICIO 2: Formateando Cadenas

# Datos que se guardan en las siguiente variables
name = "Moon"
gravity = 0.00162 
planet = "Earth"

# Plantilla estatica (plantilla vieja)
"""
title = f'Gravity Fact about {name}'
# print(title)
theme = f'{"-"*100} \nPlanet Name: {planet} \nGravity on {name}: {gravity * 1000} m/s2'
template = f'\n{title.title()}\n{theme}\n'
#print(template)
"""

# Nueva plantilla
nueva_plantilla = "\nGravity Fact about {name} \n-------------------------------------\nPlanet name: {planet}\nGravity on {planet}: {gravity} m/s2"
print(nueva_plantilla.format(name=name, planet=planet, gravity=gravity*1000))

# Probando la plantilla con diferentes datos
planet = 'Marte '
gravity  = 0.00143
name = 'Ganímedes'

print(nueva_plantilla.format(name=name, planet=planet, gravity=gravity*1000))