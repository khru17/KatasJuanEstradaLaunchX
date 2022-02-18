# MÓMUDLO 9 - FUNCIONES

# Funciones sin argumentos
print("\n *** Funciones sin argumentos")
# Para crear una función, se debe usr la palabra clave def
# seguida de un nombre, paréntrsis y despu+es el cuerpo con el código de función:

# Ejemplo de una función sin argumentos:
def rocket_parts():
    # La función regresa una cadena
    return 'payload, propellant, structure' 

# LLamando a la función rocket_parts()
output =  rocket_parts()

# En Python, si una función no devuelve explícitamente un valor,
# devuelve implícitamente None
print(output)

# Si necesitas usar el valor de una función, esa función debe devolver el valor explícitamente. 
# De lo contrario; se devolverá None.

# Argumentos opcionales y requeridos

# Las funciones integradas están disponibles de inmediato, 
# por lo que no es necesario importarlas explícitamente

# Funciones con argumentos
print("\n *** Funciones con argumentos")

# Ejemplo de una función que necesita argumentos
def distance_from_earth(destination):
    if destination == 'Moon':
        return '238,855'
    else:
        return 'Unable to compute to that destination'

print(distance_from_earth('Moon'))

print(distance_from_earth('Saturn'))

# Funciones con varios argumentos
print("\n *** Funciones con varios argumentos")

# Ejemplo
print("Función con dos argumentos")
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print(days_to_complete(238855, 75))

# Funciones como argumentos
print("\n *** Funciones como argumentos")

# Ejemplo
total_days = days_to_complete(238855, 75)
print(round(total_days))


# Uso de argumentos de palabra clave en Python
print("\n *** Uso de argumentos de palabra clave en Python")

from datetime import timedelta, datetime
"""
def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime('Arrival: %A %H:%M')

print(arrival_time())
"""

# Combinación de argumentos y argumentos de palabra clave
print("\n *** Combinación de argumentos y argumentos de palabra clave")
# A veces, una función necesita una combinación de argumentos de palabra clave y argumentos. 
# En Python, esta combinación sigue un orden específico. 
# Los argumentos siempre se declaran primero, seguidos de argumentos de palabra clave
def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f'{destination} Arrival: %A %H:%M')

print(arrival_time('Moon', hours=0.13))

# Argumentos de variable
print("\n *** Argumentos de variable")
# Ejemplo
def variable_length(*args):
    print(args)


variable_length()
variable_length('one', 'two')
variable_length(None)

print("\nOtre ejemplo de una función con argumentos variables")
# Otro ejemplo
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f'Total time to launch is {total_minutes} minutes'
    else:
        return f'Total time to launch is {total_minutes/60} hours'

print(sequence_time(4, 14, 18))
print(sequence_time(4, 14, 48))


# Argumentos de palabra clave variable
print("\n *** Argumentos de palabra clave variable")

# Ejemplo
def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day='Wednesday', pilots=3)

# Otro ejemplo
print("\nOtro ejemplo de una función con argumentos de palabra clave variables")
def crew_members(**kwargs):
    print(f'{len(kwargs)} astronauts assigned for this mission:')
    for title, name in kwargs.items():
        print(f'{title}: {name}')


crew_members(captain='Neil Armstrong', pilot='Buzz Aldrin', command_pilot='Michael Collins')

# Nos debemos asegurar que se ingresen palabras clave repetidas
# Si no, nos arrojara un error
crew_members(captain='Neil Armstrong', pilot='Buzz Aldrin', pilot='Michael Collins')