# CADENAS
from ntpath import join
from traceback import print_tb


print("********** Cadenas **********")
# En Python, las cadenas son inmutables.
# Las cadenas pueden ir entre commilassimples, dobles o triples. 
# Pero es importante tener en cuenta que si la cadena que usamos tiene numeros o caracteres especiales o esta entre comillas. 
# Debemos usar una forma diferente de comillas a las del propio texto, por ejemplo

cadena = 'The "near side" is the part of the Moon that faces the Earth'

print(cadena)

cadena1 = "We only see about 60% of the Moon's surface"
print(cadena1)

# Si no realizamos esta alternación entre comillas,a la hora de ejecutar el programa
# Python nos puede aarrojar errores 

# Si la cadena contiene comiilas simples y dobles, es necesario utilizar comilla triples, para evitar errores
# Ejemplo:
cadena2 = """We only see about 60% of the Moon's surface, this is known as the "near side"."""
print(cadena2)
print("")
print("")

# Texto multilínea
print("********** Texto multilínea **********")
print("")
# Formas de definir varías líneas de texto como una sola variable, con el uso de las siguientes caracteres
# 1: \n
# 2: """
# 3: Utilizando varios prints 

# Ejemplos de uso:
# \n
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound.\n\n"
print(multiline)

# """
multiline = """Facts about the Moon:
...  There is no atmosphere.
...  There is no sound."""
print(multiline)

# Métodos de string en Python
print("\n\n********** Métodos string en Python **********")
# Los métodos de cadena forman parte del tipo str

# Método split()
print("\n *** Método para dividir una cadena: split()")
# Este método crea una ista de cada palabra o número que está separado por un espacio
temperatures = '''Daylight: 260 F
... Nighttime: -280 F'''
print(temperatures.split())

print("Dividiendo la cadena por espacios")
print(temperatures.split('\n'))

print("\n *** Método para encontrar una cadena dentro de una cadena: find()")
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""

print("Buscando la palabra Moon, de la siguiente cadena " + "'" + temperatures + "'")
print(temperatures.find('Moon')) # -1
# En este caso el método find regresara -1, ya que no se encontro la cadena Moon, dentro de la cadena de
# de la variable temperatures

# En el siguiente ejemplo se busca la palabra Mars, y se encontrar en la cadena
# Entonces, en este caso el método find regresa la posición de donde inicia la palabra
print("\nBuscando la palabra Mars, de la siguiente cadena " + "'" + temperatures + "'")
print(temperatures.find('Mars')) # 68


# Método count()
print("\n *** Método para contar cuantas veces se encuentra una cadena dentro de otra: count()")
print("Las veces que se encuentra la palabra Mars en la cadena de la variable temperatures: " + str(temperatures.count('Mars')))
print("Las veces que se encuentra la palabra Moon en la cadena de la variable temperatures: " + str(temperatures.count('Moon')))

# Método lower()
print("\n *** Método para pasar la cadena a minúsculas: lower()")
print(temperatures.lower())


# Método upper()
print("\n *** Método para pasar la cadena a mayúsculas: upper()")
print(temperatures.upper())


# Método replace()
print("\n *** Método para pasar transformar texto: replace()")
print("Texto original: \n'Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.'")
print("Texto reemplazando la palabra Celsius: " + 'Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.'.replace('Celsius', 'C') )


# Método join()
print("\n *** Método para pasar unir cadenas de una lista texto: join()")
moon_facts = ['The Moon is drifting away from the Earth.', 'On average, the Moon is moving about 4cm every year']
print('\n'.join(moon_facts))


# Formatos de cadenas en Python
print("\n\n********** Formatos de cadenas en Python **********")

# Formato con signo de porcentaje
print("\n *** Formato con signo de porcentaje (%s)")
mass_percentage = '1/6'
print('On the Moon, you would weigh about %s of your weight on Earth' % mass_percentage)

print("\nEjemplo con multiples valores con el signo de porcentaje")
print("""Both sides of the %s get the same amount of sunlight,
    but only one side is seen from %s because
    the %s rotates around its own axis when it orbits %s.""" % ('Moon', 'Earth', 'Moon', 'Earth'))


# El formato del porcentaje es fácil de usar con un valor, pero cuando queremos dar formato a la cadena
# con más de una variable, no es tan eficiente y da poca claridad, por este motivo, se recomienda en estos casos
# usar alguno de las dos siguientes formas...

# Formato con signo de porcentaje
print("\n *** Formato con el método format()")
mass_percentage = '1/6'
print('On the Moon, you would weigh about {} of your weight on Earth'.format(mass_percentage))

# Usando el método format con identificadores númericos
print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))

# Usando el método format con alias
print("""You are lighter on the {moon}, because on the {moon} 
... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))

# Cadenas con f
print("\n *** Cadenas con f ")
# Las cadenas f son menos detalladas que cualquier opción de formato
# En este caso, el uso de la expresión no requiere una llamada a una función.
print(f'On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth')