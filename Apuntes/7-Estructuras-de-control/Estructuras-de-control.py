# MÓDULO 7 - ESTRUCTURAS DE CONTROL

# COCLI WHILE
# El ciclo while realiza una operación mientras una determinada condición es True

# Creamos la variable que almacena el texto
user_input = ''
# Creamos la lista que almacena cada uno de los textos que el usuario ingresa
inputs = []

# Ejemplo del ciclo while con un if
while user_input.lower() != 'done':
    # Verificamos si hay un valor en user_input
    if user_input:
        # Almacenamos ese valor en la lista
        inputs.append(user_input)
    # Capturamos un nuevo valor
    user_input = input('Enter a new value, or done when done: ')


# CICLO FOR
# Python tiene muchos tipos que se pueden recorrer en ciclo. Estos tipos se conocen como iterables
# Las listas de Python son iterables y se pueden usar con un ciclo for. Se usa un ciclo for con objetos 
# iterables que va a recorrer en ciclo un número conocido de veces, una vez para cada elemento del objeto iterable.
from time import sleep

countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
    sleep(1)
print("Blast off!! 🚀")

