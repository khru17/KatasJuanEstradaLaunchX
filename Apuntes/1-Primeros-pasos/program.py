# Ejemplo se un programa en Python
""" 
sum = 1 + 2
print(sum)
"""

# Función print()
"""
print('Hola desde la consola')
"""

# Variables
"""
sum = 1 + 2 
product = sum * 2
print(product) #6
"""

# Tipos de datos
# Para saber el tipo de un dato, podemos usar la función type()
"""
distancia_a_alfa_centauri = 4.367
print(type(distancia_a_alfa_centauri))
"""

# Operadores
"""
Operadores basicos
+ : sumas
- : resta
/ : división
* : multiplicación
"""

# Operadores de asignación
"""
= : asignación de valor
x += 2 : incrementa 2 al valor de x
x -= 2 : resta 2 al valor de x
x /= 2 : divide el valor de x entre 2
x *= 2 : multiplica el valor de x por 2
"""

# Fechas
"""
# Para poder trabajar con fechas es importante importar la biblioteca datetime, de la siguiente manera
from datetime import date
# Obteniendo la fecha de hoy y mostrandola en pantalla 
print(date.today())
"""

# Conversion de tipo de datos

# En este caso se convertira la fecha obtenida en un string, para poder ser mostrada 
"""
from datetime import date
print("Toda's date is: " + str(date.today()))
"""

# Entrada del usuario

# Para obtener alguna cadena de texto 
"""
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: "+ name)
"""

# Obteniendo numeros como entrada
print("Calculadora")
firs_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(firs_number)+int(second_number))